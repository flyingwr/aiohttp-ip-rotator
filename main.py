from dotenv import load_dotenv
load_dotenv()

from aiohttp_ip_rotator import RotatingClientSession

import asyncio
import os

async def main():
    key_id, key_secret = os.getenv("AWS_ACCESS_KEY_ID"), os.getenv("AWS_SECRET_ACCESS_KEY")
    
    async with RotatingClientSession("https://ipinfo.io",
                                     key_id, key_secret,
                                     wait_all_regions=False) as session:
        for _ in range(50):
            async with session.get("https://ipinfo.io/json") as response:
                print(await response.json())

if __name__ == "__main__":
    asyncio.run(main())