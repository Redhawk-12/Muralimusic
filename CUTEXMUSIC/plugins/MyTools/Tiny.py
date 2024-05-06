import os
from PIL import Image
import cv2
from pyrogram import Client, filters
from CUTEXMUSIC import app

@app.on_message(filters.command("tiny"))
async def tiny_sticker(client, message):
    reply = message.reply_to_message
    if not (reply and reply.sticker):
        await message.reply("Please reply to a sticker")
        return
    kontol = await message.reply("Processing please wait")
    await kontol.edit_text("🐾")
    ik = await app.download_media(reply)
    im1 = Image.open("assets/cuteex.png")
    if ik.endswith(".tgs"):
        # Process for animated stickers (.tgs)
        ...
    elif ik.endswith(".webm"):
        # Special handling for .webm files
        vidcap = cv2.VideoCapture(ik)
        success, image = vidcap.read()
        if success:
            cv2.imwrite("frame.png", image)  # Save the first frame as PNG
            im = Image.open("frame.png")
            os.remove("frame.png")  # Cleanup
        else:
            await kontol.edit_text("Failed to process video file.")
            os.remove(ik)
            return
    elif ik.endswith((".gif", ".mp4")):
        # Process for GIF and MP4 files
        ...
    else:
        # Handling other image files directly
        im = Image.open(ik)
    
    # General resizing and composition for all image types
    z, d = im.size
    if z == d:
        xxx, yyy = 200, 200
    else:
        t = z + d
        a = z / t
        b = d / t
        aa = (a * 100) - 50
        bb = (b * 100) - 50
        xxx = 200 + 5 * aa
        yyy = 200 + 5 * bb
    k = im.resize((int(xxx), int(yyy)))
    k.save("k.png", format="PNG", optimize=True)
    im2 = Image.open("k.png")
    back_im = im1.copy()
    back_im.paste(im2, (150, 0))
    back_im.save("o.webp", "WEBP", quality=95)
    file = "o.webp"
    await app.send_document(message.chat.id, file, reply_to_message_id=message.id)
    await kontol.delete()
    os.remove(file)
    os.remove(ik)
    if os.path.exists("k.png"):
        os.remove("k.png")

