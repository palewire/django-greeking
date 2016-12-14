# -*- coding: utf-8 -*-
"""
Create objects from past Los Angeles Times stories for use as boilerplate.
"""
from __future__ import absolute_import
import six
from . import placeholdit
from datetime import datetime
from django.utils import lorem_ipsum

#
# Objects
#


class Story(object):
    """
    A boilerplate story.
    """
    def __init__(
        self,
        slug,
        headline,
        byline,
        pub_date,
        canonical_url,
        kicker,
        description,
        sources,
        credits,
        content,
        image,
    ):
        self.slug = slug
        self.headline = headline
        self.byline = byline
        self.pub_date = pub_date
        self.canonical_url = canonical_url
        self.kicker = kicker
        self.description = description
        self.sources = sources
        self.credits = credits
        self.content = content
        self.image = image


class RelatedItem(object):
    """
    A condensed reference to a story.
    """
    def __init__(self, headline, url, image):
        self.headline = headline
        self.url = url
        self.image = image


class Image(object):
    """
    An image.
    """
    def __init__(self, url, credit, caption):
        self.url = url
        self.credit = credit
        self.caption = caption


class Quote(object):
    """
    A quote.
    """
    def __init__(self, quote, source):
        self.quote = quote
        self.source = source

#
# Retrieval methods
#


def get_story():
    """
    Returns a boiler plate story as an object.
    """
    return Story(
        slug="la-data-latimes-ipsum",
        headline="This is not a headline",
        byline="This is not a byline",
        pub_date=datetime.now(),
        canonical_url="http://www.example.com/",
        kicker="This is not a kicker",
        description=lorem_ipsum.COMMON_P.split(".")[0],
        sources="This is not a source",
        credits="This is not a credit",
        content=six.text_type('\n\n'.join(lorem_ipsum.paragraphs(6))),
        image=get_image(900)
    )


def get_related_items(count=4):
    """
    Returns the requested number of boiler plate related items as a list.
    """
    defaults = dict(
        headline="This is not a headline",
        url="http://www.example.com/",
        image=get_image(400, 400)
    )
    return [RelatedItem(**defaults) for x in range(0, count)]


def get_image(width, height=None, background_color="cccccc", random_background_color=False):
    """
    Returns image with caption, credit, and random background color as requested.
    """
    return Image(
        url=placeholdit.get_url(
            width,
            height=height,
            background_color=background_color,
            random_background_color=random_background_color
        ),
        credit="This is not an image credit",
        caption="This is not a caption"
    )


def get_quote():
    """
    Returns quote and its source.
    """
    return Quote(
        quote="This is not a pull quote",
        source="This is not a quote source"
    )
