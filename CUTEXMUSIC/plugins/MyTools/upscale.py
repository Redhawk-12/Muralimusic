from CUTEXMUSIC import app
from pyrogram import client, filters
import base64
import requests
from pyrogram.enums import ChatAction
from config import LOG_GROUP_ID

@app.on_message(filters.command(["enhance", "upscale"]))
async def enchance(_, message):
      reply = message.reply_to_message
      user_id = message.from_user.id
  
      if not reply and (not reply.photo or not reply.sticker):
            return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴜᴘsᴄᴀʟᴇ ɪᴛ....😑")
      else:
           path = await reply.download(
             file_name=f"{user_id}.jpeg"
           )
        
           msg = await message.reply_text("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ......")
           with open(path, 'rb') as file:
                 photo = file.read()
             
           encoded_image_data = base64.b64encode(photo).decode('utf-8')
        
           url = 'https://apis-awesome-tofu.koyeb.app/api/remini?mode=enhance'
           headers = {
                 'accept': 'image/jpg',
                 'Content-Type': 'application/json' 
           }
           data = {
             "imageData": encoded_image_data 
           }
        
           try:
              response = requests.post(
                    url, 
                    headers=headers, 
                    json=data
              )
              await msg.edit(
                "ᴀʟᴍᴏsᴛ ᴅᴏɴᴇ......❣️"
              )
               
              path = f"@itz_cute_shivani_upscaled_{user_id}.png"
             
              with open(path, 'wb') as file:
                  file.write(response.content)
              
              if (await message.reply_document(
                   document=path, quote=True
              )):
                   await msg.delete()
                  
              
           except Exception as e:
                await app.send_message(LOG_GROUP_ID, f"an error occured in upscale \n\n{e}")
                await message.reply_text(
                    f"ꜱᴏʀʀʏ ᴛᴏᴅᴀʏ ꜱᴇʀᴠᴇʀ ɪꜱ ᴅᴇᴀᴅ ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴛᴏᴍᴏʀʀᴏᴡ 😴")
                return
           