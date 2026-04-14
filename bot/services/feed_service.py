from aiohttp import ClientSession, ClientError, ClientConnectorError, ClientResponseError
from logging import error


class Fetch:

    def __init__(self):
        self.__last_guid__ = []


    @property
    def last_guid(self):
        return self.__last_guid__


    @last_guid.setter
    def last_guid(self, new_guid: str):
        self.__last_guid__.append(new_guid)


    async def __fetch_endpoint__(self, source: str):
        async with ClientSession() as session:
            try:
                async with session.get(source) as response:
                    return await response.json()

            except ClientResponseError as e:
                error(f"Error HTTP: {e.status} - {e.message}")
            except ClientConnectorError as e:
                error(f"Error Conection: {e}")
            except ClientError as e:
                error(f"Generic error aiohhtp: {e}")


    async def __smart_polling__(self, url: str):
        try:
            data = await self.__fetch_endpoint__(url) 
            new_posts = []
            guid = data.get("guid")

            if guid not in self.last_guid:
                new_posts.append(data)
                self.last_guid = guid 
                
                if len(self.last_guid) > 5:
                    oldest = self.last_guid.pop(0) if isinstance(self.last_guid, list) else None

            return new_posts  

        except Exception as e:
            error(f"Error in __smart_polling__ {url}: {e}")
            return []
