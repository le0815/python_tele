import datetime

from telethon import TelegramClient, events
import asyncio
import test
from telethon.tl.types import InputMessagesFilterVideo

import edit_video
import requests

download_path = "15mb_vid/"
upload_path = "edited_video/"
api_id = 25261509
api_hash = "a690894b4f2c3f5dfdbdaaaed8c12a29"
# Ql & Public
download_chat_id = -1002006536487
upload_chat_id = -1001996807858

client = TelegramClient('ha', api_id, api_hash)
newest_msg_id_source = 0


# -------------------------------------------------------------
async def get_newest_message_id():
    # Replace 'chat_username' with the username or chat ID of the group
    chat = await client.get_entity(download_chat_id)

    # Get the chat history
    count = 0
    print("start finding video msg")
    async for msg in client.iter_messages(chat, None):
    # channel = await client.get_entity(download_chat_id)
    # messages = await client.get_messages(channel, limit=None)
    # for msg in messages:
        post_link = msg.id
        print(f"{post_link}")
        test.WriteFile(post_link)



async def DownLoadVid(vid, vid_name):
    file_path = download_path + str(vid_name) + ".mp4"
    await client.download_media(vid, file=file_path)
    print(f"download file successfully: {vid_name}")

# --------------------------------------------------------------------------------

@client.on(events.NewMessage)
async def my_event_handler(event):
    # download and edit new video
    if -1002126759941 == event.chat_id:
        asyncio.gather(get_newest_message_id())
        # await event.reply('hi!')
        print("replied")

client.start()

client.run_until_disconnected()

# -----------------------------------------------------------------------------------
