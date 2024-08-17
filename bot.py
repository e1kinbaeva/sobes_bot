from aiogram import Bot, Dispatcher, types, executor
from config import token
import random

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Я загадал число от 1 до 3 угадайте")

@dp.message_handler()
async def number_handler(message: types.Message):
            random_1 = random.randint(1,3)
            if message.text.isdigit():
                user_number = int(message.text)
                if user_number == random_1:
                    await message.reply('Поздравляю! Ты угадал/a!')
                    await message.reply('Начать новую игру /start ')

                else:
                    await message.reply('Неправильно! Попробуй снова! - /start ')
            else:
                await message.answer("Пожалуйста, отправьте число.")


executor.start_polling(dp)

