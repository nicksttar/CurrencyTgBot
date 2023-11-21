from aiogram import F, Router
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from menu.mainkb import main_kb
from config import wellcome_message, currency_kb_text


# Router
router = Router()


# Currency Pairs kb 
# cp - currency pairs
currency_kb = InlineKeyboardBuilder()

cp1 = InlineKeyboardButton(text='EUR/USD', callback_data='EUR/USD') 
cp2 = InlineKeyboardButton(text='USD/JPY', callback_data='USD/JPY') 
cp3 = InlineKeyboardButton(text='GBP/USD', callback_data='GBP/USD') 
cp4 = InlineKeyboardButton(text='AUD/USD', callback_data='AUD/USD') 
cp5 = InlineKeyboardButton(text='USD/CHF', callback_data='USD/CHF') 
cp6 = InlineKeyboardButton(text='USD/CAD', callback_data='USD/CAD') 
back_btn = InlineKeyboardButton(text='Menu', callback_data='menu')

currency_kb.row(cp1, cp2, cp3, cp4, cp5, cp6, back_btn)
currency_kb.adjust(2)


@router.callback_query(F.data =='currency')
async def currency(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(currency_kb_text, reply_markup=currency_kb.as_markup())

@router.callback_query(F.data =='menu')
async def menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(wellcome_message, reply_markup=main_kb.as_markup())
