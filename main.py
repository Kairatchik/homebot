# main.py
from aiogram import types, Dispatcher, Bot, executor
from decouple import config
import logging

token = config("TOKEN")

bot = Bot(token=token)
dp = Dispatcher(bot)


Admins = [904268457, ]


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    print('Обработчик старта')
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}\n'
                                f'Твой телеграм ID - {message.from_user.id}\n')

    await message.answer(text='Привет')

@dp.message_handler(commands="mem")
async def mem_handler(message: types.Message):
    # photo = open('media/img.png', 'rb')

    with open('media/img.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=photo)


@dp.message_handler()
async def echo_handler(message: types.Message):
    try:
        number = float(message.text)
        await message.answer(str(number ** 2))
    except ValueError:
        await message.answer(message.text)
        
    
@dp.message_handler()
async def echo_handler(message:types.Message):
    await message.answer(message.text)




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)