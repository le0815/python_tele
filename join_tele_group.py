import datetime
import random
import time

from telethon import TelegramClient, events, functions, errors
import asyncio

from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

import test

download_path = "15mb_vid/"
upload_path = "edited_video/"
api_id = 24259180
api_hash = "63cf9778009838a7d48f75866a5b6fc9"
# Ql & Public
download_chat_id = -1002006536487
upload_chat_id = -1001996807858

client = TelegramClient('khanh_chi', api_id, api_hash)
newest_msg_id_source = 0


# -------------------------------------------------------------
async def JoinGroup():

    dict_link = test.GetNameGroup()
    count = 0
    count_success = 0
    count_failure = 0
    for link in dict_link:
        # join private group
        if link == 'private_link':
            for idx in dict_link.get(link):
                print(f"private: {idx}")
                try:
                    await client(ImportChatInviteRequest(idx))
                    count_success += 1
                    print(f'success join private: {idx}, count_success : {count_success}')

                except Exception as e:
                    count_failure += 1
                    print(f'failed join private: {idx}, count_failure : {count_failure}')
                    print(f'\nerr(private): {e}')
                count += 1
                print(f"count: {count}")
                sleep_time = random.randint(1, 5)
                time.sleep(sleep_time)
        # join public group
        else:
            for idx in dict_link.get(link):
                print(f"public: {idx}")
                try:
                    chat = await client.get_entity(idx)
                    await client(JoinChannelRequest(chat))
                    count_success += 1
                    print(f'success join public: {idx}, count_success : {count_success}')
                except Exception as e:
                    count_failure += 1
                    print(f'failed join public: {idx}, count_failure : {count_failure}')
                    print(f'\nerr(public): {e}')
                count += 1
                print(f"count: {count}")
                sleep_time = random.randint(1, 5)
                time.sleep(sleep_time)


# --------------------------------------------------------------------------------

@client.on(events.NewMessage)
async def my_event_handler(event):
    # download and edit new video
    if -1002000463892 == event.chat_id:
        asyncio.gather(JoinGroup())
        # await event.reply('hi!')
        print("replied")


client.start()

client.run_until_disconnected()

# -----------------------------------------------------------------------------------
