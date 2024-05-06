from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from CUTEXMUSIC import app 

def get_pypi_info(package_name):
    try:
        # Construct the PyPI API URL for the package
        api_url = f"https://pypi.org/pypi/{package_name}/json"

        # Sending a request to the PyPI API
        response = requests.get(api_url)

        # Check if the response is successful
        if response.status_code == 200:
            # Extracting information from the API response
            pypi_info = response.json()
            return pypi_info
        else:
            return None
    except Exception as e:
        print(f"Error fetching PyPI information: {e}")
        return None

@app.on_message(filters.command("pypi", prefixes="/"))
async def pypi_info_command(client, message):
    try:
        # Get the package name from the command
        package_name = message.command[1]

        # Getting information from PyPI
        pypi_info = get_pypi_info(package_name)

        if pypi_info:
            # Creating a message with PyPI information
            info_message = f"ᴅᴇᴀʀ {message.from_user.mention} \n " \
                           f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴘᴀᴋᴀɢᴇ ᴅᴇᴛᴀɪʟs \n\n " \
                           f"ᴘᴀᴋᴀɢᴇ ɴᴀᴍᴇ ➪ {pypi_info['info']['name']}\n\n" \
                           f"ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ ➪ {pypi_info['info']['version']}\n\n" \
                           f"ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➪ {pypi_info['info']['summary']}\n\n" \
                           f"ᴘʀᴏJᴇᴄᴛ ᴜʀʟ ➪ {pypi_info['info']['project_urls']['Homepage']}"

            
            cute_button = InlineKeyboardButton(
                text="〆 ᴄʟᴏsᴇ 〆",
                callback_data="close",
            )

            
            close_markup = InlineKeyboardMarkup([[cute_button]])

            # Sending the PyPI information back to the user with the inline button
            await message.reply_text(info_message, reply_markup=close_markup)
        else:
            # Handling the case where package information is not found
            await message.reply_text(f"Package '{package_name}' not found \n please dont try again later .")

    except IndexError:
        # Handling the case where the command is not provided with a package name
        await message.reply_text("Please provide a package name after the /pypi command.")

