import random
import time
import json
from config import LOG_GROUP_ID
import requests
import random 
from pyrogram.errors import MediaCaptionTooLong
from CUTEXMUSIC import app
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InputMediaPhoto

# CHAT GPT 4 & 5 ADDED 
# BY MURALI
# ALL FIXED 
BUTTON = InlineKeyboardMarkup(
       [
              [
                     InlineKeyboardButton(
                            text=f"〆 ᴄʟᴏsᴇ 〆",
                            callback_data="close",
                    )
              ]
       ]
)              

LEN_TEXT = [
"Hello How Can i Assist You Today ",
"Hello My Name is Murali Ai How Can i Help You ",
"Yes?",
" YES HOW CAN I HELP YOU "
" U CAN ASK ME ANYTHING IM ALWAYS AVAILABLE HERE ",
       " Tell Me More About your self ",
       "hello",
       " Ji Boliye ",
       "tho Kese he aap log",
]

API_KEY = [
"5198e8e03dmsh8964c5e124e2423p1465fcjsn24fee55d765b",
"0ebcdc50dbmshe65ff123652b7b4p1c40d9jsn4ab1f1712db4",
"6cc113b9f1msh1f244a6defb90dep1b6531jsn4c0e887cd642",
"eacee98f87msh41aee31eb23ba55p1490f2jsn2121da163166",
"0f49257511mshf15d0a693448b21p139a7cjsna7fc4fcdf307",
"ec29045c74mshd5bd965c6c9e063p18719djsn97b6e224cf92",
"d95a67dfddmsh71a7421e9a5a26dp170571jsn59930db0013d",
"6abf3cae92msh2baa3aac2ed1b56p1d276ejsne4f75a9afb3d",
"c211e9f49dmshd6b2b7c73a126a4p1cbffajsndbd7e05975d6",
"2aa80696b0mshd6c0ad0df2a015ep15b691jsnc97f5740422f",
]


url = "https://nandha-api.onrender.com/ai/bard"

async def send_to_gpt(api_url: str, query: str) -> tuple:
    try:
        response = requests.get(f"{api_url}/{query}")
        response.raise_for_status()
        data = response.json()
        return data.get("content", "No response from the API."), data.get("images", False)
    except requests.exceptions.RequestException as e:
        return None, f"Request error: {e}"
    except Exception as e:
        return None, f"An error occurred: {str(e)}"

@app.on_message(filters.command(["chatgpt", "ai", "ask", "gpt"], prefixes=["+", ".", "/", "", "$", "&"]))
async def zzchat_gpt(bot, message):
    try:
        chat_id = message.chat.id
        message_id = message.id
        await bot.send_chat_action(chat_id, ChatAction.TYPING)
        if message.reply_to_message:
            Msg = message.reply_to_message.text
        else:
            Msg = " ".join(message.command[1:])
        if message.reply_to_message:
            Msg = message.reply_to_message.text + " " + Msg

        api_response, images = await send_to_gpt(url, Msg)

        medias = []
        bard = str(api_response)
        if images:
            if len(images) > 1:
                for image_url in images:
                    medias.append(InputMediaPhoto(media=image_url, caption=None))

                medias[-1] = InputMediaPhoto(media=images[-1], caption=bard)

                try:
                    await app.send_media_group(chat_id=chat_id, media=medias, reply_to_message_id=message_id)
                    return
                except Exception as e:
                    await app.send_message(LOG_GROUP_ID, f"An error occurred in gpt 3.5: {str(e)}")
            elif len(images) == 1:
                image_url = images[0]
                try:
                    await message.reply_photo(photo=image_url, caption=bard, reply_markup=BUTTON)
                    return
                except MediaCaptionTooLong:
                    await message.reply_text(bard, reply_markup=BUTTON)
                except Exception as e:
                    await app.send_message(LOG_GROUP_ID, f"An error occurred in gpt 3.5: {str(e)}")
            else:
                pass
        else:
            try:
                await message.reply_text(bard)
            except Exception as e:
                await app.send_message(LOG_GROUP_ID, f"An error occurred in gpt 3.5: {str(e)}")
    except Exception as e:
        await app.send_message(LOG_GROUP_ID, f"An unhandled exception occurred: {str(e)}")

               

                





zurl = "https://chatgpt-42.p.rapidapi.com/gpt4"
zheaders = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": random.choice(API_KEY),
    "X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
}


async def Chatgpt4api(query):
    payload = {
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ],
        "web_access": False
    }
    response = requests.post(zurl, json=payload, headers=zheaders)
    return response.json().get('result', '')


@app.on_message(filters.command(["gpt4", "chatgpt4"]))
async def chatgpt4(bot, message):
    query = " ".join(message.command[1:])
    
    if not query:
        await message.reply_text("Please give any query.")
        return
    
    result = await Chatgpt4api(query)
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await message.reply_text(result, reply_markup=BUTTON)

# Chat gpt 5



url5 = "https://chatgpt-gpt5.p.rapidapi.com/ask"
headers5 = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": random.choice(API_KEY),
    "X-RapidAPI-Host": "chatgpt-gpt5.p.rapidapi.com"
}

FUNNY = [
" i love you ",
" hello ",
"hmm",
"hii ",
" hey ",
]

def chatgpt5(query):
    payload = {
        "query": query
    }
    response = requests.post(url5, json=payload, headers=headers5)
    return response.json().get('response', '')


@app.on_message(filters.command(["Chatgpt5", "gpt5"]))
async def gpt5_command_handler(bot, message):
    try:
        query = " ".join(message.command[1:])
        
        if not query:
            query = random.choice(FUNNY)
            await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
            await message.reply_text(f"{message.from_user.mention} {chatgpt5(query)}")
        else:
            gpt5_response = chatgpt5(query)
            await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
            await message.reply_text(gpt5_response, reply_markup=BUTTON)
    except Exception as e:
        await app.send_message(LOG_GROUP_ID, f"An error occurred in gpt 5: {str(e)}")

# Gemimi Ai



Gurl = "https://chatgpt-42.p.rapidapi.com/chatbotapi"

Gheaders = {
	"content-type": "application/json",
	"X-RapidAPI-Key": random.choice(API_KEY),
	"X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
}

@app.on_message(filters.command(["Gemini", "bard"]))
async def gemini_command_handler(bot, message):
    try:
        if len(message.command) < 2:
            await message.reply_text(random.choice(LEN_TEXT))
            return
        
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        user_message = " ".join(message.command[1:])
        
        
        payload = {
	"bot_id": "OEXJ8qFp5E5AwRwymfPts90vrHnmr8yZgNE171101852010w2S0bCtN3THp448W7kDSfyTf3OpW5TUVefz",
	"messages": [
		{
			"role": "user",
			"content": user_message
		}
	],
	"user_id": "",
	"temperature": 0.9,
	"top_k": 5,
	"top_p": 0.9,
	"max_tokens": 256,
	"model": "matag2.0"
}

        
        response = requests.post(Gurl, json=payload, headers=Gheaders)
        
        
        if response.ok:
            result = response.json().get('result')
            await message.reply_text(result, reply_markup=BUTTON)
        else:
            await message.reply_text("Failed to get response from the API.")
    except Exception as e:
        print(f"Error: {e}")
               
