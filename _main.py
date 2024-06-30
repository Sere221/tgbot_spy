import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters.command import Command
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, ContentType
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types import Message
from aiogram.types.web_app_info import WebAppInfo

import _ip
import data
import eye_god as eg
import viki

logging.basicConfig(level=logging.INFO)

router = Router()
bot = Bot(token=data.bot)
dp = Dispatcher()
PRICE = types.LabeledPrice(label="Пожертвование", amount=500*100)
type_btn = ''


@dp.message(Command("start", "help"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Узнать свой IP"),
            types.KeyboardButton(text="Как это работает?")
        ],
        [
            types.KeyboardButton(text="Наш сайт", web_app=WebAppInfo(url="https://cv97944-django-iw3fu.tw1.ru/")),
            types.KeyboardButton(text="Пожертвование")
        ]
    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Я к вашим услугам", reply_markup=keyboard)


@dp.message(F.text.lower() == "пожертвование")
async def with_puree(message: types.Message):
    user_id = message.from_user.id
    await bot.send_invoice(user_id,
                           title="Подписка на бота",
                           description="Активация подписки на бота на 1 месяц",
                           provider_token=data.PAYMENT_TOKEN,
                           currency="rub",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")


@router.pre_checkout_query()
async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@router.message(F.content_types == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message):
    await message.answer('Оплата прошла успешно!')


@dp.message(F.text.lower() == "узнать свой ip")
async def with_puree(message: types.Message):
    await message.reply(_ip.get_my_ip())


@dp.message(F.text.lower() == "как это работает?")
async def without_puree(message: types.Message):
    await message.reply('Для пробитие номеров введите:\n'
                        '/ph 89999999999\n\n'
                        'Для пробитие по IP введите:\n'
                        '/ip 127.12.12.1\n\n'
                        'Для пробитие сайта по IP введите:\n'
                        '/hs vk.com\n\n'
                        'Есть что то нужно в википедии просто введите текст)')


@dp.message(Command("ph"))
async def get_phone(message: types.Message):
    text = message.text[3:]
    await message.reply(eg.get_phone(text))


@dp.message(Command("ip"))
async def get_ip(message: types.Message):
    text = message.text[4:]
    await message.reply(_ip.get_info_by_ip(text))


@dp.message(Command("hs"))
async def get_host(message: types.Message):
    text = message.text[4:]
    await message.reply(_ip.get_ip_by_hostname(text))


@dp.message(F.text)
async def get_p(message):
    await message.reply(viki.viki(message.text))


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())