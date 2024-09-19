import datetime

from telethon import TelegramClient, events
import test
import edit_video
download_path = "downloaded_video/"
upload_path = "video_tip_top/"
api_id = 25261509
api_hash = "a690894b4f2c3f5dfdbdaaaed8c12a29"
download_chat_id = -1002126759941
upload_chat_id = -1002006536487

client = TelegramClient('ha', api_id, api_hash)
newest_msg_id_source = 0


# -------------------------------------------------------------



async def UpLoadVid(client, gr):
    count = 0
    for vid_name in test.GetFileName():

        # print(f"editing {vid_name}")
        # edit_video.MovingText(vid_name)
        try:
            file_path = upload_path + str(vid_name)
            # channel = await client.get_entity(gr_name)
            print(f"uploading....: {vid_name}")
            print(f"time start: {datetime.datetime.now()}")
            await client.send_file(gr, file_path)
            print("upload successfully")
            count += 1
            print(f'{count} video uploaded')
            print(f"time end: {datetime.datetime.now()}")
        except Exception as err:
            print(f"Error: {err}")
            test.WriteUploadVidErr(gr)

# --------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------
