from aiogram import Router, F 
from aiogram.types import CallbackQuery, Message
from compare_function import compare


# Router
router = Router()


async def compare_handler(text: str, answer_func):
    try:
        a, b = text.split('/')
        await answer_func('Please wait...')
        await answer_func(compare(a, b))
    except Exception:
        try:
            numb, val1, to, val2 = text.split()
            await answer_func('Please wait...')
            await answer_func(compare(val1, val2, int(numb)))
        except Exception:
            await answer_func('Try again')


@router.message(F.text)
async def compare_text_handler(message: Message):
    await compare_handler(message.text, message.answer)

@router.callback_query(F.data)
async def compare_callback_handler(call: CallbackQuery):
    await compare_handler(call.data, call.message.answer)