from pyrogram import Client, filters
import requests
import io
from config import LOG_GROUP_ID
from CUTEXMUSIC import app 
import random 
from pyrogram.enums import ChatAction


API = [
"5198e8e03dmsh8964c5e124e2423p1465fcjsn24fee55d765b",
"0ebcdc50dbmshe65ff123652b7b4p1c40d9jsn4ab1f1712db4",
"6cc113b9f1msh1f244a6defb90dep1b6531jsn4c0e887cd642",
"eacee98f87msh41aee31eb23ba55p1490f2jsn2121da163166",
"0f49257511mshf15d0a693448b21p139a7cjsna7fc4fcdf307",
"ec29045c74mshd5bd965c6c9e063p18719djsn97b6e224cf92",
"6abf3cae92msh2baa3aac2ed1b56p1d276ejsne4f75a9afb3d",
"d95a67dfddmsh71a7421e9a5a26dp170571jsn59930db0013d",
"c211e9f49dmshd6b2b7c73a126a4p1cbffajsndbd7e05975d6",
"2aa80696b0mshd6c0ad0df2a015ep15b691jsnc97f5740422f",
]

url = "https://chatgpt-42.p.rapidapi.com/texttoimage"
headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": random.choice(API),
    "X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
}


def send_query_to_api(query):
    payload = {
        "text": query
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get('generated_image', '')


@app.on_message(filters.command(["ImageGen", "imggen"]))
async def genimg_command_handler(bot, message):
    try:
        query = " ".join(message.command[1:])
        
        if not query:
            await message.reply_text("ɢɪᴠᴇ sᴏᴍᴇ ǫᴜᴇʀʏ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ɪᴍᴀɢᴇ.")
            return
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        msg = await message.reply_text("ɪᴛ ᴛᴀᴋᴇs ᴜᴘᴛᴏ 𝟹𝟶 sᴇᴄᴏɴᴅs ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
        generated_image_url = send_query_to_api(query)
        image_response = requests.get(generated_image_url)
        if image_response.status_code == 200:
            image_stream = io.BytesIO(image_response.content)
            
            await message.reply_photo(image_stream, caption=f"ɪᴍᴀɢᴇ ɪs ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ {message.from_user.mention}\n\n||ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ {app.mention} ||" )
            await msg.delete()
        else:
            await message.reply_text("sᴏʀʀʏ ᴛᴏᴅᴀʏ sᴇʀᴠᴇʀ ɪs ᴅᴇᴀᴅ ᴘʟᴇᴀsᴇ ᴛʀʏ ᴛᴏᴍᴍᴏʀᴡ..")
           # await msg.delete()
    except Exception as e:
        await message.reply_text("sᴏʀʀʏ ᴛᴏᴅᴀʏ sᴇʀᴠᴇʀ ɪs ᴅᴇᴀᴅ ᴘʟᴇᴀsᴇ ᴛʀʏ ᴛᴏᴍᴍᴏʀᴡ.")
        await app.send_message(LOG_GROUP_ID, f"An error occurred in Image generation \n**Error:** {e}")





@app.on_message(filters.command("genimg"))
async def generate_image(client, message):
    if len(message.command) < 2:
        await message.reply_text("ɢɪᴠᴇ sᴏᴍᴇ ǫᴜᴇʀʏ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ɪᴍᴀɢᴇ.")
        return

    text = message.text.split("/genimg ", 1)[1].replace(" ", "+")
    
    url = f"https://aiimage.hellonepdevs.workers.dev/?prompt={text}"
    

    response = requests.get(url)
    x = await message.reply_text("ɪᴛ ᴛᴀᴋᴇs ᴜᴘᴛᴏ 𝟹𝟶 sᴇᴄᴏɴᴅs ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    data = response.json()
    image_url = data.get("image_url")
    await message.reply_photo(image_url, caption=f"Given Prompt = {text} \n\nɪᴍᴀɢᴇ ɪs ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ {message.from_user.mention}\n\n||ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ {app.mention} ||")   
    await x.delete()
        
