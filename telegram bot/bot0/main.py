from pyrogram import *
from pyrogram.types import *
from pyromod import listen
from asyncio import sleep

bot = Client(
    "my_bot",
    api_id="your api id",
    api_hash="put your api hash here",
    bot_token="put your bot token here"
)

admin = 1532534642

m_admin_list = ReplyKeyboardMarkup(keyboard=[
    ['test', 'پاسخگویی 📩']
],
    resize_keyboard=True)

m_auser_list = ReplyKeyboardMarkup(keyboard=[
    ['Wallpaper 🏙', 'پشتیبانی 📩']
],
    resize_keyboard=True)

@bot.on_message(filters.private & filters.user(admin))
async def main(client, message):
    ID = message.from_user.id
    text = message.text
    name = message.from_user.first_name
    print(message)
    if text == "/start":
        await bot.send_message(ID, f" {name}سلام  ",reply_markup= m_admin_list)
    elif text == "پاسخگویی 📩":
        sender_id = await bot.ask(ID,"آیدی کاربر را وارد کنید : ")
        reply_message = await bot.ask(ID,"پاسخ خود را وارد کنید :")
        await bot.send_message(sender_id.text,reply_message.text)
    else:
        pass


@bot.on_message(filters.private)
async def main(client, message):
    ID = message.from_user.id
    text = message.text
    name = message.from_user.first_name
    print(message)
    if text == "/start":
        await bot.send_message(ID, f" {name}سلام  ",reply_markup= m_auser_list)
    elif text == "پشتیبانی 📩":
        text_request = await bot.ask(ID,"پیام خود را وارد کنید : ")
        full_txt = f"""
        ID = {ID}
        Name = {name}
        username = @{message.from_user.username}
        
        {text_request.text}
        """
        await bot.send_message(admin,full_txt)
    elif text == 'Wallpaper 🏙':
        await bot.send_photo(ID, "download.jpg", caption="Caption")
        my_message = (message.message_id) + 1
        await sleep(15)
        await bot.delete_messages(ID,my_message)


bot.run()
