from moviepy import *

video_clip = VideoFileClip("your_video.mp4")
video_clip.write_gif("output.gif", fps=10)