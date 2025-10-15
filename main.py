from parser import Parser
from config import API_ID, API_HASH, TOKEN
import asyncio


# test chat - unitebroker
async def main():
    bot = Parser(API_ID, API_HASH)
    await bot.start()
    await bot.get_all_users('unitebroker')
    await bot.stop()


if __name__ == '__main__':
    asyncio.run(main())
