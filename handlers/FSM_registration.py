# FSM_registration.py
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSM_reg(StatesGroup):
    model = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    submit = State()


async def start_fsm_reg(message: types.Message):
    await FSM_reg.model.set()
    await message.answer('Введите модель товара: ')


async def load_model(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model'] = message.text

    await FSM_reg.next()
    await message.answer('Отправь размер товара')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSM_reg.next()
    await message.answer('Укажите категорию')



async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text


    await FSM_reg.next()
    await message.answer('Укажите цену товара:')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text


#     await FSM_reg.next()
#     await message.answer('Укажите свою почту')
#
#
# async def load_email(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['email'] = message.text


    await FSM_reg.next()
    await message.answer('Отправьте фотографию товара')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id


    await FSM_reg.next()
    await message.answer('Верные ли данные')
    await message.answer_photo(photo=data['photo'],
                               caption=f'model - {data["model"]}\n'
                                       f'size - {data["size"]}\n'
                                       f'category - {data["category"]}\n'
                                       # f'Дата рождения - {data["date_age"]}\n'
                                       f'price - {data["price"]}\n')

async def submit(message: types.Message, state: FSMContext):
    if message.text == 'да':
        async with state.proxy() as data:
            # Запись в базу
            await message.answer('Ваши данные в базе')

        await state.finish()

    elif message.text == 'нет':
        await message.answer('Хорошо, отменено!')
        await state.finish()

    else:
        await message.answer('Выберите да или нет')


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(start_fsm_reg, commands=['registration'])
    dp.register_message_handler(load_model, state=FSM_reg.model)
    dp.register_message_handler(load_size, state=FSM_reg.size)

    dp.register_message_handler(load_category, state=FSM_reg.category)
    dp.register_message_handler(load_price, state=FSM_reg.price)
    # dp.register_message_handler(load_email, state=FSM_reg.email)
    dp.register_message_handler(load_photo, state=FSM_reg.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_reg.submit)