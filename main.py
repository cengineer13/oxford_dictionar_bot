import logging
from aiogram import Bot, Dispatcher, executor, types
from oxfordLookup import getDefinition #oxford Api function
from googletrans import Translator

translator = Translator()

# Configure logging
logging.basicConfig(level=logging.INFO)

API_TOKEN = '5537937036:AAESHaSf7CffrixUcnEj2R9nUUDaYdp8cGU'
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Welcome to oxford dictionary!. Please send the word")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):

    await message.reply("Yordam qismi")

@dp.message_handler()
async def tarjima(message: types.Message):
    lang = translator.detect(message.text).lang #detect language of income text
    #if more than two words return translated  sentence
    if len(message.text.split()) > 1:
        dest = 'uz' if lang == 'en' else 'en'

        await message.reply(translator.translate(message.text, dest=dest).text)

    else:
        if lang == 'en':
            word = message.text
            def_dict = getDefinition(word)
            #Agar so'z mavjud bo'lsa
            if def_dict:
                await message.reply(f"✏Word:   {word} \n📖Definitions: \n{def_dict['definitions']}")
                await message.answer_voice(def_dict.get('audio'))

            #Agar notogri soz yoki belgi kiritilsa
            else:
                await message.reply("😔 Bunday so'z topilmadi...")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)