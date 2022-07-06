# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
# getting subclip as video is large
# adding margin to the video
clip1 = VideoFileClip(
    "E:/College Stuff/SDMCET/8th Sem/Project/Application/frame_detection_v1/logs/differenceFrames.avi").subclip(0, 5).margin(10)
clip2 = VideoFileClip(
    "E:/College Stuff/SDMCET/8th Sem/Project/Application/frame_detection_v1/logs/reconstructed.avi").subclip(0, 5).margin(10)

# clips list
clips = [[clip1, clip2]]


# stacking clips
final = clips_array(clips)

# showing final clip
final.ipython_display(width=480)

os.system('vlc __temp__.mp4 --fullscreen --video-on-top --intf=dummy vlc://quit')
