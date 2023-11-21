from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import about_text


# Router
router = Router()

about_kb = InlineKeyboardBuilder()
back_btn = InlineKeyboardButton(text='Menu', callback_data='menu')
about_kb.add(back_btn)


@router.callback_query(F.data == 'about')
async def about(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(about_text, reply_markup=about_kb.as_markup())
    