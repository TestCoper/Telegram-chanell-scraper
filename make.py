import asyncio
from pyrogram import Client

api_id = 19536838
api_hash = "2de75ac31d99e3648d968f7c96f6942d"


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
