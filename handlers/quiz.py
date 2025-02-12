from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot

async def quiz(message: types.Message):
    with open('media/img.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo)

    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Далее', callback_data='button_1')

    keyboard.add(button)

    question = 'Какое время года?'

    answer = ['Лето', 'Зима', 'Осень', 'Весна']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='неверно',
        open_period=60,
        reply_markup=keyboard

    )

async def quiz_2(call: types.CallbackQuery):
    question = 'Dota2 or CS.GO'
    answer = ['Dota2', 'CS.GO', 'Valve']

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2
    )

def register_hundlers(dp: Dispatcher):
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, text='button_1')