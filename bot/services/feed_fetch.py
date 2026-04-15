from aiohttp import ClientSession, ClientError, ClientConnectorError, ClientResponseError
from logging import error


class Fetch:
    """
    The Fetch class will receive the request from the endpoint and
    send the new post request to be rendered in the embed.
    """

    def __init__(self):
        self.__last_guid__ = []


    @property
    def last_guid(self):
        return self.__last_guid__


    @last_guid.setter
    def last_guid(self, new_guid: str):
        self.__last_guid__.append(new_guid)


    async def _fetch_endpoint(self, source: str) -> dict:
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


    async def _smart_polling(self, url: str) -> list:
        """
        The smart_polling method will check every 60 minutes, which is the default time.
        In each iteration of this method, a new instance of the new_post list is created to store the new post,
        and its GUID is stored in __last_guid__ to avoid duplication.
        """
        try:
            data = await self._fetch_endpoint(url) 
            new_post = []
            guid = data.get("guid")

            if guid not in self.last_guid:
                new_post.append(data)
                self.last_guid = guid 
                
                if len(self.last_guid) > 5:
                    oldest = self.last_guid.pop(0) if isinstance(self.last_guid, list) else None

            return new_post  

        except Exception as e:
            error(f"Error in _smart_polling {url}: {e}")
            return []
