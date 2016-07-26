# -*- coding: utf-8 -*-
"""
Create objects from past Los Angeles Times stories for use as boilerplate.
"""
from datetime import datetime
from placeholdit import get_url as get_placeholdit_url


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
        slug="fi-20973_1_microsoft-access",
        headline="FoxPro 2.5 Is Fast and Easy to Use",
        byline="<a href='http://www.latimes.com/la-bio-richard-oreilly-staff.html'>Richard O'Reilly</a>",
        pub_date=datetime(1993, 4, 9, 0, 0, 0),
        canonical_url="http://articles.latimes.com/print/1993-04-09/business/fi-20973_1_microsoft-access",
        kicker="Computer File",
        description="Compared to Microsoft's other database program, FoxPro 2.5 for Windows is faster and a better choice.",
        image_url=get_placeholdit_url(1600, 900),
        sources="Times research",
        credits="Richard O'Reilly",
        content="""Microsoft's FoxPro 2.5 for Windows is an important upgrade of its predecessor, but you might not believe it at first because it looks a lot like the program it replaces.

That program is FoxPro 2.0, a powerhouse DOS database program acquired by Microsoft last year in the purchase of Fox Software. Rather than give the Windows version a fancy graphics look, Microsoft chose to make it look quite similar to the DOS predecessor.

In addition to the Windows version of FoxPro 2.5, there's also a version for DOS, each priced at $495, although upgrade and promotional prices are available. The Windows version offers some advantages for database development and can retrieve data from large files almost as fast as the DOS version, so it should be the more popular of the two. Both versions are faster than FoxPro 2.0.

Compared to Microsoft's other database program, Access, which was designed from the ground up as a Windows program, FoxPro 2.5 for Windows is faster and a better choice for developing data applications that will be used by many people in a department or throughout a company. It's also easy to use, even for database beginners.

But for the beginner who will only occasionally do database development, Access is probably easier because of its step-by-step "cue cards," which lead you through commonly performed tasks.

The relational database structure and programming language used in FoxPro is compatible with dBASE III and IV, also called "Xbase" compatible.

It will use existing data and programming code from other Xbase programs.

A proprietary data access system that FoxPro designers named "Rushmore" is what gives the program its blazing speed. Microsoft says applications where multiple users access multiple tables run two to three times faster in the new version.

I found FoxPro 2.5 to be nearly twice as fast as Microsoft Access in retrieving and sorting data from a large file containing about 50,000 records. It was also faster than Paradox for Windows, although direct comparisons were hampered by differences in the way you invoke sorting in the two programs.

FoxPro 2.5 for Windows also appeared to be significantly faster than Paradox for Windows. In published speed comparisons between the DOS versions of FoxPro and Paradox, FoxPro has been the winner.

A number of design features make FoxPro 2.5 for Windows easy to use. One is the way it uses a "dialogue box" on the screen to build a data query.

It is called "relational query by example," and no matter how complex the selection criteria are, it is easily done. You can have the results displayed on the screen or stored in a new data table or printed in a report or on labels.

Printing to labels is made much easier because the formats of more than 50 popular Avery label sizes are built into the program.

Users new to FoxPro can run the program from menus and dialogue boxes. But in the background, programming language commands are being created.

They are displayed in a small window in one corner of the screen, where you are free to ignore them or study them as a prelude to learning the programming language.

Applications can be created without doing any programming, and others who use the applications don't even have to know how to use FoxPro. All the tasks they need to perform can be invoked from menus.

Applications developed in the Windows version can be "transported" into a format suitable for DOS, and vice versa.

Microsoft also plans to make FoxPro available on Macintosh and computers running the UNIX operating system, and translation to and from those versions will also be available.

That means FoxPro 2.5 for Windows can be used to develop applications for all of the most popular personal computers and workstation computers found in businesses."""
    )


def get_related_items(count=4):
    """
    Returns the requested number of related items as a list.
    """
    defaults = dict(
        headline="This is not a headline",
        url="http://www.example.com",
        image_url=get_placeholdit_url(400, 400)
    )
    return [RelatedItem(**defaults) for x in range(0, count)]
