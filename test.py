import os
import time


# Replace with the path to your file

def CheckFileExits(vid_name):
    file_path = f'downloaded_video/{vid_name}.mp4'
    if os.path.exists(file_path):
        return 1
    else:
        return 0


def GetFileName():
    folder_path = 'video_tip_top'  # Replace with the path to your folder
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    # Print the list of file names
    return files


def WriteFile(vid_name):
    f = open('link_tele.txt', 'a')
    f.write(f'https://t.me/test_bot_sex_2/{vid_name}\n')
    f.close()


def WriteLog(gr_name, cmt):
    f = open('join_group_log.txt', 'a')
    f.write(f'{gr_name} - {cmt}\n')
    f.close()


def GetNameGroup():
    f = open('list_tele_group.txt', 'r')
    list_link = f.readlines()
    private_link = []
    public_link = []
    for link in list_link:
        # private group
        if (link.find('joinchat/') != -1):
            value = link[link.find('joinchat/') + 9: len(link) - 1]
            private_link.append(value)
        # public group
        else:
            value = link[link.find('t.me/') + 5: len(link) - 1]
            public_link.append(value)
    f.close()
    dict_link = {
        'public_link': public_link,
        'private_link': private_link
    }
    return dict_link


# a = GetNameGroup()
# for value in a:
#     if value == 'public_link':
#         print(f"{value} : {a.get(value)}")
#         for idx in a.get(value):
#             print(idx)

def WriteJoinedGr(gr_name):
    f = open('joined_group.txt', 'a')
    f.write(f'{gr_name}\n')
    f.close()

def WriteUploadVidErr(gr_name):
    f = open('upload_vid_err.txt', 'a')
    f.write(f'{gr_name}\n')
    f.close()

def CheckGrJoined(gr_name):
    f = open('joined_group.txt', 'r')
    for name in f.readlines():
        if gr_name == name[:len(name) - 1]:
            f.close()
            return 1
    f.close()
    return 0

