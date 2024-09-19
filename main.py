from telethon import TelegramClient, events
import asyncio
import edit_video
import requests

download_path = "downloaded_video/"
upload_path = "edited_video/"
api_id = 24259180
api_hash = "63cf9778009838a7d48f75866a5b6fc9"
download_chat_id = -1002126759941
upload_chat_id = -1001996807858

client = TelegramClient('ha', api_id, api_hash)
newest_msg_id_source = 0


# -------------------------------------------------------------
async def SendMsg():
    chat = await client.get_entity(upload_chat_id)
    # Get the chat history
    messages = await client.get_messages(chat, limit=1)
    # Check if there is at least one message
    if messages:
        msg = messages[0]
        # url = f'https://alpha-one-cph1808.000webhostapp.com/index.php?msg_id={msg.id}'
        url = f'http://localhost:3000/index.php?msg_id={msg.id}'
        response = requests.get(url)

        # Check the response status code
        if response.status_code == 200:
            # Request was successful
            print('GET request was successful')
            # You can access the response content (e.g., HTML) using response.text

        else:
            print('GET request failed with status code:', response.status_code)

    else:
        print("No messages in the chat")
async def get_newest_message_id():
    global newest_msg_id_source
    # Replace 'chat_username' with the username or chat ID of the group
    chat = await client.get_entity(download_chat_id)

    # Get the chat history
    messages = await client.get_messages(chat, limit=1)

    # Check if there is at least one message
    if messages:
        # Get the ID of the newest message
        message = messages[0]
        # Check the type of the message using the message's type
        if CheckMsgMedia(message) == 1 and newest_msg_id_source < message.id:
            newest_msg_id_source = message.id
            print("msg video found")
            print(f"vid size: {message.video.size}")
            await DownLoadVid(message.video, newest_msg_id_source)
            await UpLoadVid(newest_msg_id_source)

    else:
        print("No messages in the chat")


def CheckMsgMedia(msg):
    if msg.video:
        return 1
    else:
        return 0


async def DownLoadVid(vid, vid_name):
    file_path = download_path + str(vid_name) + ".mp4"
    await client.download_media(vid, file=file_path)
    print("download file successfully")
    print("editing vid")
    edit_video.EditVid(vid_name)


async def UpLoadVid(vid_name):
    file_path = upload_path + str(vid_name) + "_edited.mp4"
    channel = await client.get_entity(upload_chat_id)
    print("uploading")
    await client.send_file(channel, file_path)
    print("upload successfully")

# --------------------------------------------------------------------------------

@client.on(events.NewMessage)
async def my_event_handler(event):
    # download and edit new video
    if download_chat_id == event.chat_id:
        asyncio.gather(get_newest_message_id())
        # await event.reply('hi!')
        print("replied")
    # send msg when edit complete
    if upload_chat_id == event.chat_id:
        await SendMsg()
client.start()

client.run_until_disconnected()

# -----------------------------------------------------------------------------------
