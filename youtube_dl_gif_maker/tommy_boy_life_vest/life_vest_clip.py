"""
http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/

To download the video from youtube:
$ youtube-dl HWrjBBXjjhM -o tommy_boy_source.mp4
"""

from moviepy.editor import *

clip = (VideoFileClip("tommy_boy_source.mp4", audio=False)
		.subclip((1,14.2),(1,14.8))
		.resize(0.3)
		.speedx(0.75)
		.fx( vfx.time_symmetrize ))

clip.write_gif("tommy_boy_vest_wiggle.gif")
