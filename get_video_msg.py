import datetime

from telethon import TelegramClient, events
import asyncio
import test
from telethon.tl.types import InputMessagesFilterVideo

import edit_video
import requests

download_path = "video_tip_top/"
upload_path = "edited_video/"
api_id = 25261509
api_hash = "a690894b4f2c3f5dfdbdaaaed8c12a29"
# Ql & Public
download_chat_id = -1002019264027
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
    async for msg in client.iter_messages(chat, None, reverse=True):
        if msg.video:
            print(f'msg video found: {msg.id}')
            # if vid bigger than 15mb -> continue
            if msg.video.size > 150 * 10**5:
                print("vid too large")
                continue
            # if vid is existed -> continue
            if test.CheckFileExits(msg.id) == 1:
                count += 1
                print("this vid has downloaded")
                print(f"count: {count}")
                continue
            print(f"count: {count}")
            print("downloading")
            print(f"time start: {datetime.datetime.now()}")
            await DownLoadVid(msg.video, msg.id)
            print("download successfully")
            print(f"time end: {datetime.datetime.now()}")
            count += 1
        if count == 1000:
            print("1000 vid downloaded")
            return


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
