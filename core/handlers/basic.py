from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await  bot.send_message(message.from_user.id, f'<b>Пртвет {message.from_user.first_name}. Рад тебя видеть!</b>')
    await message.answer(f'<s>Пртвет {message.from_user.first_name}. Рад тебя видеть!</s>')
    await message.reply(f'<tg-spoiler>Пртвет {message.from_user.first_name}. Рад тебя видеть!</tg-spoiler>')

async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично. Ты отправил картинку, я сохраню ее себе.')
    await bot.download_file(file.file_paht, 'photo.jpg')