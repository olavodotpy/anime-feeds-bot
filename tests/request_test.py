import asyncio
from aiohttp import ClientSession, ClientError, ClientConnectorError, ClientResponseError



class TestRequest:
    async def get_post(self, url: str = None):
        async with ClientSession() as session:
            try:
                async with session.get(url) as response:
                    return await response.json()

            except ClientResponseError as e:
                print(f"Error HTTP: {e.status} - {e.message}")
            except ClientConnectorError as e:
                print(f"Error Conection: {e}")
            except ClientError as e:
                print(f"Generic error aiohhtp: {e}")


async def main():
    obj = TestRequest()
    response = obj.get_post("http://127.0.0.1:8000/api/last/posts")
    guid = list()

    for data in await response:
        guid.append(data["guid"])

    print(guid)


asyncio.run(main())
