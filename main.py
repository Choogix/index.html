
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8327887897:AAFvap9nzXkFUgc46ao6Zgc5PZCpEHL09dw"
PAYMENT_TOKEN = "381764678:TEST:5e1a9c7b..."  # тестовый токен

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Покупка курса',
        description='Покупка курса по программированию',
        payload='invoice',
        provider_token=PAYMENT_TOKEN,
        currency='USD',
        prices=[types.LabeledPrice(label='Покупка курса', amount=5 * 100)]
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())










