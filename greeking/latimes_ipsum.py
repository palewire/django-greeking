# -*- coding: utf-8 -*-
"""
Create objects from past Los Angeles Times stories for use as boilerplate.
"""
from __future__ import absolute_import
import six
from . import lorem_ipsum
from . import placeholdit
from datetime import datetime


class Story(object):
    """
    A boilerplate story
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
        image_url,
        sources,
        credits,
        content
    ):
        self.slug = slug
        self.headline = headline
        self.byline = byline
        self.pub_date = pub_date
        self.canonical_url = canonical_url
        self.kicker = kicker
        self.description = description
        self.image_url = image_url
        self.sources = sources
        self.credits = credits
        self.content = content


class RelatedItem(object):
    """
    A condensed reference to a story.
    """
    def __init__(self, headline, url, image_url):
        self.headline = headline
        self.url = url
        self.image_url = image_url


def get_story():
    """
    Returns a boilerplate story as an object.
    """
    return Story(
        slug="la-data-latimes-ipsum",
        headline="This is not a headline",
        byline="This is not a byline",
        pub_date=datetime(2016, 1, 1, 0, 0, 0),
        canonical_url="http://www.example.com/",
        kicker="This is not a kicker",
        description=lorem_ipsum.COMMON_P.split(".")[0],
        image_url=placeholdit.get_url(1600, 900),
        sources="This is not a source line",
        credits="This is not a credit line",
        content=six.text_type('\n\n'.join(lorem_ipsum.paragraphs(6)))
    )


def get_related_items(count=4):
    """
    Returns the requested number of boiler plate related items as a list.
    """
    defaults = dict(
        headline="This is not a headline",
        url="http://www.example.com/",
        image_url=placeholdit.get_url(400, 400)
    )
    return [RelatedItem(**defaults) for x in range(0, count)]
