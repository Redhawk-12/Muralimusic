from pyrogram import Client, filters
import requests
from CUTEXMUSIC import app 
import asyncio

limit = 5
api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
headers = {'X-Api-Key': 'Zg2rDIcq415hV5BMnHJTaQ==WO9Xuk9P89Qdx9X1'}



@app.on_message(filters.command(["jokes","joke"]))
async def jokes(client, message):
    response = requests.get(api_url, headers=headers)
    if response.status_code == requests.codes.ok:
        joke_data = response.json()
        joke_text = joke_data[0]['joke']
        x = await message.reply_text("generating an joke....")
        await asyncio.sleep(0.8)
        await message.reply_text(joke_text)
        await x.delete()
    else:
        await message.reply_text(f"Error: {response.status_code} {response.text}")
