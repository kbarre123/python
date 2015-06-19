"""
http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/

To download the video from youtube:
$ youtube-dl XWX4GUYGQXQ -o tayne_source.mp4
"""

from moviepy.editor import *

clip = (VideoFileClip("tayne_source.mp4", audio=False)
		.subclip((1,40.5),(1,47))
		.resize(0.7)
		.fx( vfx.time_symmetrize ))

clip.write_gif("tayne_05.gif")
