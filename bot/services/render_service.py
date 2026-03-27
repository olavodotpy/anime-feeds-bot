from aiohttp import ClientSession, ClientError, ClientConnectorError, ClientResponseError



class Fetch:

    def __init__(self):
        self.__new_post = list()
        self.__last_send_guid = list()

    async def _fetch_endpoint_(self, source: str):
        async with ClientSession() as session:
            try:
                async with session.get(source) as response:
                    return await response.json()

            except ClientResponseError as e:
                print(f"Error HTTP: {e.status} - {e.message}")
            except ClientConnectorError as e:
                print(f"Error Conection: {e}")
            except ClientError as e:
                print(f"Generic error aiohhtp: {e}")


    async def smart_polling(self, url: str):
        try:
            response = await self._fetch_endpoint_(url)

            for post in response:
                post_guid = post.get("guid")
                
                if post_guid in self.__last_send_guid:
                    return 

                if len(self.__last_send_guid) == 0 or post_guid not in self.__last_send_guid:

                    if len(self.__new_post) == 2:
                        self.__new_post.clear()
                        self.__last_send_guid.clear()

                    post["content"] = ""
                    post["description"] = ""

                    self.__new_post.append(post)
                    self.__last_send_guid.append(post_guid)

            return self.__new_post
        
        except Exception as e:
            print(f"Error {e}")
