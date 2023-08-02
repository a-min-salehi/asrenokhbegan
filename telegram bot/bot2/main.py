from pyrogram import *
from pyrogram.types import *
from pyromod import listen
from database import DataBase

bot = Client(
    "my_bot",
    api_id="your api id",
    api_hash="put your api hash here",
    bot_token="put your bot token here"
)

main_list = ReplyKeyboardMarkup(keyboard=[
    ['والپیپر HD 🖼️', 'بخش ویژه ⚡️', 'زیر مجموعه گیری']
],
    resize_keyboard=True)

channel = -1001660564154


async def refreal(client, message):
    ID = message.from_user.id
    this_user = DataBase().return_user(ID)
    if this_user[3] == None:
        await bot.send_message(
            ID,
            f"""
            کاربر گرامی شما باید از لینک زیر 2 نفر زیر مجموعه بگیرید :
            https://t.me/kaasaandaanBot?start={ID}
            
            تعداد نفراتی که تا کنون اضافه نمودید = 0
            
            """
        )
    elif this_user[4] == None:
        await bot.send_message(
            ID,
            f"""
            کاربر گرامی شما باید از لینک زیر 2 نفر زیر مجموعه بگیرید :
            https://t.me/kaasaandaanBot?start={ID}

            تعداد نفراتی که تا کنون اضافه نمودید = 1

            """
        )
    else:
        await bot.send_message(ID, "کاربر گرامی  شما تا کنون 2 زیر مجموعه را با موفقیت اضافه کرده اید")


async def special(client, message):
    ID = message.from_user.id
    members = await bot.get_chat_members(channel)
    members_list = [i.user.id for i in members]
    if ID in members_list:
        await bot.send_message(ID, "درسته !")
    else:
        await bot.send_message(ID,
                               f"  \n کاربر گرامی برای استفاده از این بخش باید در کانال ما عضو باشید : \n @channel_de_test ")


async def wallpaper(client, message):
    ID = message.from_user.id
    this_user = DataBase().return_user(ID)
    if this_user[4] is not None:
        await bot.send_photo(ID, "download.jpg", caption="Caption")
    else:
        await bot.send_message(ID, "کاربر گرامی برای استفاده از این بخش شما باید 2 زیر مجموعه داشته باشید")


@bot.on_message()
async def main(client, message):
    ID = message.from_user.id
    text = message.text
    name = message.from_user.first_name
    username = message.from_user.username
    if text.startswith("/start"):
        db = DataBase()
        db.add_user(name, ID, username)
        await bot.send_message(ID, f" {name}سلام  ", reply_markup=main_list)

        host_id = int(text[7::])
        host_user = db.return_user(host_id)
        try:
            if host_user[3] == None:
                db.update_user(host_id, "client", ID)
                await bot.send_message(
                    host_id,
                    f"""
                    کاربر گرامی یک زیر مجموعه با نام {name}
                     username = @{username}
                     زیر مجموعه شما شد
                    """
                )
            elif (host_user[4] == None) & (host_user[3] != ID):
                db.update_user(host_id, "client2", ID)
                await bot.send_message(
                    host_id,
                    f"""
                    کاربر گرامی یک زیر مجموعه با نام {name}
                     username = @{username}
                     زیر مجموعه شما شد
                    """
                )
            else:
                pass
        except:
            pass
    elif text == 'بخش ویژه ⚡️':
        await special(client, message)
    elif text == 'زیر مجموعه گیری':
        await refreal(client, message)
    elif text == 'والپیپر HD 🖼️':
        await wallpaper(client, message)


bot.run()
