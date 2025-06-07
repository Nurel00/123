import os
import asyncio
from _pyrepl import commands

from dotenv import find_dotenv, load_dotenv
from aiogram import Dispatcher,Bot,types
from common.bot_cmds_list import private
from hendlers.user_panel.start_functions import start_functions_router

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_router(start_functions_router)

async def on_startup():
    print("_______men turdum bro________ ")

async def on_shutdown():
    print("________men uktadum bro_________ ")

async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private,scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot,allowed_updates=dp.resolve_used_update_types())
    
if __name__ == "__main__":
    asyncio.run(main())
    