# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 00:04:23 2021

@author: goka
"""


import pafy 
# Download the Pluralsight 'we are one' video
# url of video 
# url = 'https://www.youtube.com/watch?v=nt3D26lrkho'

url = "https://www.youtube.com/watch?v=7S_tz1z_5bA"
# create video object
video = pafy.new(url)
# extract information about best resolution video available 
bestResolutionVideo = video.getbest()
# download the video
bestResolutionVideo.download()