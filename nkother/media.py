# encoding: utf-8
'''
Created on 2017年11月15日

@author: niko
'''
"""
这是一个电影类
"""
import webbrowser

class Movie():
    """这是一个电影类
    """

    def __init__(self, title, storyline, imglink, movielink):
        '''
        Constructor
        '''
        self.title = title
        self.storyline = storyline
        self.poster_image_url = imglink
        self.trailer_youtube_url = movielink
    
    def show_trailer(self):
        """这是一个电影对象 
        """
        webbrowser.open(self.movielink);