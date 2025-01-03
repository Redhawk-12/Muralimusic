from CUTEXMUSIC import app
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
import random 
from PIL import Image, ImageDraw, ImageFont
import asyncio

get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)
# CREDIT - MEEEEE

bg_path = "assets/CLEFT.PNG"
font_path = "assets/font.ttf"


async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],
    first_name: str,
    username: Optional[str] = None,
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((1270, 1270))
        bg.paste(resized, (169, 627), resized)

    img_draw = ImageDraw.Draw(bg)

    img_draw.text(
        (1600, 750),
        text=f"Name: {first_name}",
        font=get_font(170, font_path),
        fill=(255, 255, 255),
    )
    img_draw.text(
        (1600, 1050),
        text=f"ID: {user_id}",
        font=get_font(170, font_path),
        fill=(255, 255, 255),
    )
    img_draw.text(
        (1600, 1350),
        text=f"Username: {username if username else 'None'}",
        font=get_font(170, font_path),
        fill=(255, 255, 255),
    )

    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path




@app.on_chat_member_updated(filters.group, group=20)
async def member_has_left(client: app, member: ChatMemberUpdated):

    if (
        not member.new_chat_member
        and member.old_chat_member.status not in {
            "banned", "left", "restricted"
        }
        and member.old_chat_member
    ):
        pass
    else:
        return

    user = (
        member.old_chat_member.user
        if member.old_chat_member
        else member.from_user
    )

    # Check if the user has a profile photo
    if user.photo and user.photo.big_file_id:
        try:
            # Add the photo path, caption, and button details
            photo = await app.download_media(user.photo.big_file_id)

            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user.id,
                first_name=user.first_name,
                username=user.username,
                profile_path=photo,
            )

            caption = f"**ᴀ ᴍᴇᴍʙᴇʀ ʟᴇғᴛ ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🥹\n\n✧══════•❁❀❁•══════✧\n╠╼➪ ✨ 𝐍𝐀𝐌𝐄 = {user.first_name}\n╠╼➪ 💫 𝐔𝐒𝐄𝐑 𝐈𝐃 = {user.id}\n╠╼➪  🎁 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 = @{user.username}\n✧══════•❁❀❁•══════✧\n\n๏sᴇᴇ ʏᴏᴜ sᴏᴏɴ ᴀɢᴀɪɴ..!**"
            button_text = " Kɪᴅɴᴀᴘ ᴍᴇ 🥹 "

            # Generate a deep link to open the user's profile
            deep_link = f"https://t.me/CuteXMusicBot?startgroup=new"

            # Send the message with the photo, caption, and button
            await client.send_photo(
                chat_id=member.chat.id,
                photo=welcome_photo,
                caption=caption,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(button_text, url=deep_link)]
                ])
            )

        except RPCError as e:
            print(e)
            return
    else:
        try:
            # If user has no profile photo, use the default image
            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user.id,
                first_name=user.first_name,
                username=user.username,
                profile_path="assets/NODP.PNG",
            )

            caption = f"**ᴀ ᴍᴇᴍʙᴇʀ ʟᴇғᴛ ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ 🥹\n\n✧══════•❁❀❁•══════✧\n╠╼➪ ✨ 𝐍𝐀𝐌𝐄 = {user.first_name}\n╠╼➪ 💫 𝐔𝐒𝐄𝐑 𝐈𝐃 = {user.id}\n╠╼➪  🎁 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 = @{user.username}\n✧══════•❁❀❁•══════✧\n\n๏sᴇᴇ ʏᴏᴜ sᴏᴏɴ ᴀɢᴀɪɴ..!**"
            button_text = " Kɪᴅɴᴀᴘ ᴍᴇ 🥹 "

            # Generate a deep link to open the user's profile
            deep_link = f"https://t.me/CutieXmusicBot?startgroup=new"

            # Send the message with the photo, caption, and button
            await client.send_photo(
                chat_id=member.chat.id,
                photo=welcome_photo,
                caption=caption,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(button_text, url=deep_link)]
                ])
            )

        except RPCError as e:
            print(e)
            return
    
