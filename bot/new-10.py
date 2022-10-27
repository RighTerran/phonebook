import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
#from info import candy_bot
import random

#token = candy_bot.token
bot = Bot("5756055729:AAEQK6OhSt723NdySrHCUO-yK7vTI80tJx4")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)


class Form(StatesGroup):
    all_candys = 200
    max_candys = 28
    start = State()
    step = State()


@dp.message_handler(commands="start", state='*')
async def start_message(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton('game')
    item2 = types.KeyboardButton('help')
    markup.add(item1, item2)
    await message.answer(f"""Привет, {message.from_user.full_name}! 
Будем играть на конфеты!
Всего у нас есть {Form.all_candys} конфет.
За 1 ход можно взять не более {Form.max_candys} конфет.
Кто заберет последнюю, тот и выиграл!
Если готов, напиши 'game', если нужна подсказка, напиши 'help'""", reply_markup=markup)
    await Form.start.set()


@dp.message_handler(lambda message: message.text == "help", state='*')
async def game(message: types.Message):
    await message.answer(f'''Вот правила:
- Я играю против тебя.
- У нас {Form.all_candys} конфет.
- Ходим по очереди.
- Брать можно максимум {Form.max_candys} конфет.
- Кто забирает последнюю конфету, тот получает всё.''')


@dp.message_handler(lambda message: message.text == "game", state=Form.start)
async def game(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['all_candys'] = 200
    await Form.step.set()
    await message.answer('Сколько конфет возьмешь?')


@dp.message_handler(lambda message: message.text.isdigit(), state=Form.step)
async def user_step(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if int(message.text) > Form.max_candys or int(message.text) <= 0:
            await message.answer(f'Не более {Form.max_candys} и не меньше 1')
            await Form.step.set()
        elif int(message.text) > data['all_candys']:
            await message.answer(f"Всего осталось {data['all_candys']}!")
            await Form.step.set()
        else:
            data['all_candys'] -= int(message.text)
            if data['all_candys'] == 0:
                await message.answer('Поздравляю!!!')
                #AnimatedSticker.tgs
                await message.answer_sticker(r'CAACAgIAAxkBAAEGNX9jWWzBRxD-sA1Yr1X7BK6xxak49QACSgIAAladvQrJasZoYBh68CoE')
                await Form.start.set()
            else:
                await Form.step.set()
                await message.answer(f"Осталось {data['all_candys']} конфет.")
                bot_choice = data['all_candys'] % (Form.max_candys + 1)
                if bot_choice < 1:
                    if data['all_candys'] > Form.max_candys:
                        bot_choice = random.randint(1, Form.max_candys + 1)
                    #else:
                        #bot_choice = random.randint(1, data['all_candys'])
            data['all_candys'] -= bot_choice
            if data['all_candys'] == 0:
                await message.answer('Я забираю  все конфеты)')
                await Form.start.set()
            else:
                await message.answer(f"""Мой ход.
{bot_choice}.
Осталось {data['all_candys']}.
        Твой ход: """)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)