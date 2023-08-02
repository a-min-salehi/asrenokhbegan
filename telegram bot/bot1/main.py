from pyrogram import *
from pyrogram.types import *
from pyromod import listen
import requests
from deep_translator import GoogleTranslator
from khayyam import *

bot = Client(
    "my_bot",
    api_id="your api id",
    api_hash="put your api hash here",
    bot_token="put your bot token here"
)


w_api_code = "6db35e6f8a2380c39bca84def2efee2b"

main_list = ReplyKeyboardMarkup(keyboard=[
    ['تقویم روز ⏳', 'ترجمه 📖', 'آب و هوا 🌦']
],
    resize_keyboard=True)




async def weather(client, message):
    ID = message.from_user.id
    city = await bot.ask(ID, " نام شهر را وارد کنید : ")
    city_text = city.text
    translated = GoogleTranslator(source='auto', target="english").translate(text=city_text)
    api = f"http://api.openweathermap.org/data/2.5/weather?q={translated}&appid={w_api_code}"
    api_result = requests.get(api)
    api_response = api_result.json()
    condition = api_response['weather'][0]['main']
    temp = round(int (api_response['main']['temp']) - 273.15)
    humidity = api_response['main']['humidity']
    wind = api_response['wind']['speed']
    await bot.send_message(ID, f"""  آب و هوای {city_text}  به شرح زیر است : 
    {condition}
    🌦
    {temp}°C
    رطوبت هوا :
    {humidity}%
    وزش باد :
    {wind} km/h
    """)


async def translate(client, message):
    markup =InlineKeyboardMarkup(  [
        [InlineKeyboardButton(
            "English 🇺🇸 ",
            callback_data="english"
        ),
        InlineKeyboardButton(
                "Persian 🇹🇯 ",
                callback_data="persian"
            ),
        InlineKeyboardButton(
                "Arabic 🇸🇦 ",
                callback_data="arabic"
            ),
        ],
        [InlineKeyboardButton(
            "Spanish 🇪🇸 ",
            callback_data="spanish"
        ),
            InlineKeyboardButton(
                "Greek 🇬🇷 ",
                callback_data="greek"
            ),
            InlineKeyboardButton(
                "Russian 🇷🇺",
                callback_data="russian"
            ),
        ],
        [InlineKeyboardButton(
            "Chinese 🇨🇳 ",
            callback_data="chinese (simplified)"
        ),
            InlineKeyboardButton(
                "Portuguese 🇵🇹 ",
                callback_data="portuguese"
            ),
            InlineKeyboardButton(
                "Indian 🇮🇳 ",
                callback_data="hindi"
            ),
        ],
    ]
    )
    await bot.send_message(message.chat.id, " به کدام زبان ترجمه کنم ؟ ",reply_markup=markup)


async def time(client, message):
    ID = message.from_user.id
    await bot.send_message(ID,JalaliDatetime.now().strftime('%C'))


@bot.on_callback_query()
async def answer(client,call):
    ID = call.from_user.id
    data = call.data
    request = await bot.ask(ID, "متن خود را وارد کنید : ")
    await bot.send_message(ID, f" ترجمه به زبان {data} :")
    translated = GoogleTranslator(source='auto', target=data).translate(text=request.text)
    await bot.send_message(ID,translated)



@bot.on_message(filters.private)
async def main(client, message):
    ID = message.from_user.id
    text = message.text
    name = message.from_user.first_name
    if text == "/start":
        await bot.send_message(ID, f" {name}سلام  ", reply_markup=main_list )
    elif text == 'ترجمه 📖':
        await translate(client,message)
    elif text == 'آب و هوا 🌦':
        await weather(client,message)
    elif text == 'تقویم روز ⏳':
         await time(client, message)

bot.run()

