""
This is a telegram chat bot with ChatGPT under the hood!

1. Paste your Telegram Bot Token and ChatGPT API Key
2. Run the code and open the bot in telegram.
  - wanna run 24/7 -> upload to a server and run there
"""

import openai
from aiogram import Bot, Dispatcher, executor, types

# create bot with @BotFather and copy Token
bot = Bot(token='6641221916:AAFu7q2BSiiqIp6VBGcyMt1TOaGERxLRYh0')
dp = Dispatcher(bot)

api_key = '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' # https://platform.openai.com/accoun>
openai.api_key = api_key


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply('Hey! This Chat Bot is using ChatGPT and was developed by kit4py. Enjoy!')


@dp.message_handler()
async def gpt(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003", # text-davinci-003 text-ada-001 -> select model to use
        prompt=message.text,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    await message.reply(response.choices[0].text)


if __name__ == '__main__':
    executor.start_polling(dp)