from aiogram import Router, F
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from menu.mainkb import main_kb
from config import wellcome_message, crypto_kb_text


# Router
router = Router()


# cryptokb
crypto_kb = InlineKeyboardBuilder()


btc_usd = InlineKeyboardButton(text='BTC/USD', callback_data='BTC/USD')
eth_usd = InlineKeyboardButton(text='ETH/USD', callback_data='ETH/USD')
xrp_usd = InlineKeyboardButton(text='XRP/USD', callback_data='XRP/USD')
ltc_usd = InlineKeyboardButton(text='LTC/USD', callback_data='LTC/USD')
doge_usd = InlineKeyboardButton(text='DOGE/USD', callback_data='DOGE/USD')
eth_usd = InlineKeyboardButton(text='ETC/USD', callback_data='ETC/USD')
back_btn = InlineKeyboardButton(text='Back', callback_data='menu')

crypto_kb.row(btc_usd, eth_usd, xrp_usd, ltc_usd, doge_usd, eth_usd, back_btn)
crypto_kb.adjust(2)


@router.callback_query(F.data =='crypto')
async def currency(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(crypto_kb_text, reply_markup=crypto_kb.as_markup())

@router.callback_query(F.data =='menu')
async def menu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(wellcome_message, reply_markup=main_kb.as_markup())
