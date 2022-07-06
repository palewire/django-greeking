"""
Create objects from past Los Angeles Times stories for use as boilerplate.
"""
from datetime import datetime

from django.utils import lorem_ipsum

#
# Objects
#


class Story:
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


class Quote:
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
        content=str("\n\n".join(lorem_ipsum.paragraphs(6))),
    )


def get_quote():
    """
    Returns quote and its source.
    """
    return Quote(quote="This is not a pull quote", source="This is not a quote source")
