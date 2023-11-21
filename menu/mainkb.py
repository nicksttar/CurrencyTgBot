from aiogram import Router
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, Message

from config import wellcome_message


# Router
router = Router()


# Menu kb
main_kb = InlineKeyboardBuilder()

btn1 = InlineKeyboardButton(text='Currency pairs', callback_data='currency')
btn2 = InlineKeyboardButton(text='Crypto currency', callback_data='crypto')
btn3 = InlineKeyboardButton(text='About', callback_data='about')
btn4 = InlineKeyboardButton(text='Exchange', callback_data='exchange', url='https://www.bestchange.com/')

main_kb.row(btn1, btn2, btn3, btn4)
main_kb.adjust(1)


@router.message(Command('start'))
async def start(message: Message):
    await message.answer(wellcome_message, reply_markup=main_kb.as_markup())
