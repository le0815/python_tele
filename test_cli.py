import datetime
import random
import time
import upload_vid_tele
import telethon
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
download_chat_id = -1002126759941
upload_chat_id = -1002006536487

client = TelegramClient('khanh_chi', api_id, api_hash)
newest_msg_id_source = 0


# -------------------------------------------------------------
async def JoinGroup():
    dict_link = test.GetNameGroup()
    # dict_link = {
    #     'public_link': ['laugaiviet'],
    #     'private_link': []
    # }
    # try:
    #     chat = await client.get_entity('QOEuIFQqvhE0ZjAx')
    #     await client(JoinChannelRequest(chat))
    # ca
    #     print(err.seconds)
    count = 0
    count_success = 0
    count_failure = 0
    count_gr = 0
    for link in dict_link:
        # join private group
        if link == 'private_link':
            for idx in dict_link.get(link):
                print(f"private: {idx} - {datetime.datetime.now()}")
                # check if gr has joined -> skip
                if test.CheckGrJoined(idx) == 0:
                    try:
                        await client(ImportChatInviteRequest(idx))
                        # sleep 61s to avoid ban
                        time_sleep = 61
                        print(f'sleep time: {time_sleep}')
                        time.sleep(time_sleep)
                        gr = await client.get_entity(idx)
                        # sleep 61s to avoid ban
                        time_sleep = 61
                        print(f'sleep time: {time_sleep}')
                        time.sleep(time_sleep)
                        count_success += 1
                        print(f'success join private: {idx}, count_success : {count_success}')
                        await upload_vid_tele.UpLoadVid(client, gr)
                    # banned for fast request
                    except telethon.errors.rpcerrorlist.FloodWaitError as err:
                        count_failure += 1
                        print(f'failed join private: {idx}, count_failure : {count_failure}')
                        test.WriteLog(idx, 'got banned')
                        print("write log ok")
                        print(f"got banned -> sleep in: {err.seconds}")
                        time.sleep(err.seconds)
                    # user name invalid
                    except telethon.errors.rpcerrorlist.UsernameInvalidError as err:
                        count_failure += 1
                        print(f"Invalid name: {err.message}")
                        print(f'failed join private: {idx}, count_failure : {count_failure}')
                        test.WriteLog(idx, 'invalid name')
                        print("write log ok")
                    # need admin to approve
                    except telethon.errors.rpcerrorlist.InviteRequestSentError as err:
                        count_failure += 1
                        print(f"requested to admin: {err.message}")
                        print(f'failed join private: {idx}, count_failure : {count_failure}')
                        test.WriteLog(idx, 'requested to admin')
                        print("write log ok")
                    # other exception
                    except Exception as err:
                        count_failure += 1
                        print(f"other exception: {err}")
                        print(f'failed join private: {idx}, count_failure : {count_failure}')
                        test.WriteLog(idx, f'{err}')
                        print("write log ok")
                else:
                    print(f'this gr has joined: {idx}')
                    try:
                        gr = await client.get_entity(idx)
                        # sleep 61s to avoid ban
                        time_sleep = 61
                        print(f'sleep time: {time_sleep}')
                        time.sleep(time_sleep)
                        await upload_vid_tele.UpLoadVid(client, gr)
                        count += 1
                        print(f"count: {count} - {datetime.datetime.now()}")
                        continue
                    except Exception as err:
                        print(f'got an err: {err}')
                count += 1
                print(f"count: {count} - {datetime.datetime.now()}")
                # sleep randomly 61s to avoid ban
                time_sleep = 61
                print(f'sleep time: {time_sleep}')
                time.sleep(time_sleep)
        # join public group
        else:
            for idx in dict_link.get(link):
                print(f"public: {idx} - {datetime.datetime.now()}")
                # check if gr has joined -> skip
                if test.CheckGrJoined(idx) == 0:
                    try:
                        gr = await client.get_entity(idx)
                        # sleep randomly 61s to avoid ban
                        time_sleep = 61
                        print(f'sleep time: {time_sleep}')
                        time.sleep(time_sleep)
                        await client(JoinChannelRequest(gr))
                        count_success += 1
                        print(f'success join public: {idx}, count_success : {count_success}')
                        test.WriteJoinedGr(idx)
                        # sleep randomly 61s to avoid ban
                        time_sleep = 61
                        print(f'sleep time: {time_sleep}')
                        time.sleep(time_sleep)
                        await upload_vid_tele.UpLoadVid(client, gr)
                    # banned for fast request
                    except telethon.errors.rpcerrorlist.FloodWaitError as err:
                        count_failure += 1
                        print(f'failed join public: {idx}, count_failure : {count_failure}')
                        test.WriteLog(idx, 'got banned')
                        print("write log ok")
                        print(f"got banned -> sleep in: {err.seconds}")
                        time.sleep(err.seconds)
                    # usr_name invalid
                    except telethon.errors.rpcerrorlist.UsernameInvalidError as err:
                        count_failure += 1
                        print(f"Invalid name: {err.message}")
                        print(f'failed join public: {idx}, count_failure : {count_failure}')
                        test.WriteLog(idx, 'invalid name')
                        print("write log ok")
                    # need admin approve
                    except telethon.errors.rpcerrorlist.InviteRequestSentError as err:
                        count_failure += 1
                        print(f"requested to admin: {err.message}")
                        print(f'failed join public: {idx}, count_failure : {count_failure}')
                        test.WriteLog(idx, 'requested to admin')
                        print("write log ok")
                    # other exception
                    except Exception as err:
                        count_failure += 1
                        print(f"other exception: {err}")
                        print(f'failed join public: {idx}, count_failure : {count_failure}')
                        test.WriteLog(idx, f'{err}')
                        print("write log ok")
                else:
                    print(f'this gr has joined: {idx}')
                    try:
                        gr = await client.get_entity(idx)
                        # sleep randomly 61s to avoid ban
                        time_sleep = 61
                        print(f'sleep time: {time_sleep}')
                        time.sleep(time_sleep)
                        await upload_vid_tele.UpLoadVid(client, gr)
                        count += 1
                        print(f"count: {count} - {datetime.datetime.now()}")
                        continue
                    except Exception as err:
                        print(f'got exception: {err}')
                count += 1
                print(f"count: {count} - {datetime.datetime.now()}")
                # sleep randomly 61s to avoid ban
                time_sleep = 61
                print(f'sleep time: {time_sleep}')
                time.sleep(time_sleep)


# --------------------------------------------------------------------------------


with client:
    client.loop.run_until_complete(JoinGroup())

# -----------------------------------------------------------------------------------
