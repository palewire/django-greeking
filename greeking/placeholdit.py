# -*- coding: utf-8 -*-
"""
Utility for generating placeholder images from http://placehold.it/
"""
URL = 'http://placehold.it/%(width)sx%(height)s/%(bcolor)s/%(tcolor)s/'


def get_url(
    width, height=None, background_color="cccccc",
    text_color="969696", text=None
):
    """
    Craft the URL for a placeholder image.

    You can customize the background color, text color and text using
    the optional keyword arguments
    """
    # If height is not provided, presume it is will be a square
    if not height:
        height = width
    d = dict(
        width=width,
        height=height,
        bcolor=background_color,
        tcolor=text_color
    )
    url = URL % d
    if text:
        text = text.replace(" ", "+")
        url = url + "?text=" + text
    return url
