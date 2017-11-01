from moviepy.editor import *

img = []

for i in range(1, 492):
    img.append("dataset/strawberry/images/{}.jpg".format(i))
    pass

clips = [ImageClip(m).set_duration(0.1)
      for m in img]

concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile("test.mp4", fps=30)