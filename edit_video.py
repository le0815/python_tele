from moviepy.editor import *
from vectortween.Mapping import Mapping


def EditVid(vid_name):
    vid = VideoFileClip(f"downloaded_video/{vid_name}.mp4")
    logo = ImageClip("img/download.jpeg")
    logo = logo.set_position(("left", "top")).set_duration(vid.duration)
    video = CompositeVideoClip([vid, logo])
    # Write the resulting video to a file
    video.write_videofile(f"edited_video/{vid_name}_edited.mp4")


def Translate(t, width, height, speed):
    # start at top-right
    start_pos = (350, 350)
    # end at top-left
    end_pos = (0, 0)
    # cal loca of tex base on time
    x = int(start_pos[0] + t / speed * (end_pos[0] - start_pos[0]))
    y = int(start_pos[1] + t / speed * (end_pos[1] - start_pos[1]))
    return x, y


def ResizeVid(vid_name):
    vid = VideoFileClip(f"downloaded_video/{vid_name}")
    # background of the vid
    black_img = ImageClip("img/black_color.jpg")
    black_img = black_img.set_duration(vid.duration)
    # cal ratio of the vid
    width, height = vid.size
    # if vid width > 450px
    if width > 450:
        new_height = (450 / width) * height
        video = vid.resize((450, new_height))
    else:
        new_width = (600 / height) * width
        video = vid.resize((new_width, 600))
    video = CompositeVideoClip([black_img, video.set_position('center')])
    return video


def MovingText(vid_name):
    vid = VideoFileClip(f"downloaded_video/{vid_name}")
    duration = vid.duration  # duration
    duration /= 2
    video_width, video_height = vid.size
    text = TextClip("Watches more on Lick-xxx.com", fontsize=50, color='white')
    start_position = (video_width, 0)  # Top-right corner
    end_position = (0, 0)  # Top-left corner
    text_clip = text.set_position(lambda t: (
        (1 - t / duration) * start_position[0] + (t / duration) * end_position[0],
        (1 - t / duration) * start_position[1] + (t / duration) * end_position[1]
    ))

    final = ResizeVid(vid_name)
    final = CompositeVideoClip([final, text_clip.set_duration(vid.duration)])
    final.write_videofile(f"edited_video/_edited_{vid_name}")




