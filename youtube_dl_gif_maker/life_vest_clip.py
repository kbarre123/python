"""
http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/
"""

from moviepy.editor import *

def time_symetrize(clip):
	""" Returns the clip played forwards then backwards. In case
	you are wondering, vfx (short for Video FX) is loaded by
	>>> from moviepy.editor import * """
	return concatenate([clip, clip.fx( vfx.time_mirror )])

clip = (VideoFileClip("tommy_boy.mp4", audio=False)
		.subclip((1,14.2),(1,14.9))
		.resize(0.3)
		.speedx(0.75)
		.fx( time_symetrize ))

clip.write_gif("tommy_boy_vest_wiggle.gif")
