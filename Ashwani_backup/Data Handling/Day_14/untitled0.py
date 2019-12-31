# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:36:15 2019

@author: BSDU ADMIN
"""
import pytube
video_url = 'https://www.youtube.com/watch?v=H2t7lknrK28' # paste here your Youube videos' url
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('C:\\Users\\BSDU ADMIN\\Desktop\\aj') # path, where to video download.
