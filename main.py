import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN_API
from menu import mainkb, currencykb, cryptokb, about, compare_handler


# Main Function
async def main():
    bot = Bot(token=TOKEN_API)
    dp = Dispatcher()
    
    dp.include_routers(mainkb.router, currencykb.router, cryptokb.router, about.router, compare_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())
    