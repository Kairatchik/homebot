# echo.py
from aiogram import types, Dispatcher
import random

async def echo_handler(message: types.Message):
    if message.text.lower() == "game":
        games = ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
        game = random.choice(games)
        await message.answer_dice(emoji=game)
    else:
        await message.answer(message.text)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_handler)
