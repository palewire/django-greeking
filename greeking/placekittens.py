# -*- coding: utf-8 -*-
"""
Utility for generating placeholder kitten images
"""
BASE_URL = 'http://placekitten.com/%(width)s/%(height)s/'

def get_url(width, height):
    return BASE_URL % dict(width=width, height=height)
