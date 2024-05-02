from moviepy.editor import VideoFileClip

clip = VideoFileClip("path_for_video.mp4")
clip.write_gif("video.gif", fps=10)
