# -*- coding: utf-8 -*-
"""
Utility functions for generating QuerySet object_lists that simulate data from django.contrib.comments
"""

import time
import datetime

def make_datetime(date_string):
    """Convert a string into a datetime object."""
    date_format = '%Y-%m-%d %H:%M'
    return datetime.datetime(*time.strptime(date_string, date_format)[0:5])

HIPHOP = {
1: {'user_name': 'Chuck D', 'user_email': 'chuck@publicenemy.com', 'user_url': 'http://lyricwiki.org/Public_Enemy:Rebel_Without_A_Pause', 'comment': "No matter what the name - we're all the same. Pieces in one big chess game. Yeah - the voice of power is in the house - go take a shower boy.", 'submit_date': make_datetime('1988-06-26 00:01'),},
2: {'user_name': 'Puff Daddy', 'user_email': 'diddy@badboy.com', 'user_url': 'http://www.seeklyrics.com/lyrics/Puff-Daddy/PE-2000.html', 'comment': "A bona fide playa, now who got the flavor. A non stop, rhythm rock, poetry sayer. I'm the life saver, the New York mayor. Before you try me, you better say your prayers.", 'submit_date': make_datetime('1999-12-31 23:59')},
3: {'user_name': 'Rakim', 'user_email': 'rakim@ericbforpresident.com', 'user_url': 'http://www.lyricstime.com/eric-b-rakim-lyrics-of-fury-lyrics.html', 'comment': "The scene of a crime every night at the show. The fiend of a rhyme on the mic that you know. It’s only one capable, breaks-the unbreakable, melodies-unmakable, pattern-unecscapable.", 'submit_date': make_datetime('1998-07-25 00:01')},
4: {'user_name': 'AZ', 'user_email': 'az@brooklyn.com', 'user_url': 'http://www.lyricsdepot.com/az/rather-unique.html', 'comment': "So it's gonna take more than your astrologist to knowledge this. A physiologist couldn't even figure out the exoticness. Raps demolishing certified the way I style it. My wordplay blaze with the rays of ultraviolence.", 'submit_date': make_datetime('1995-10-10 10:10')},
5: {'user_name': 'Missy Elliot', 'user_email': 'missy@underconstruction.com', 'user_url': 'http://www.lyricstime.com/missy-elliott-back-in-the-day-lyrics.html', 'comment': "British Knights and gold chains. Do the prep and cabbage patch. And wear your laces all fat. Back in the dayyyyyyyy, hey hey. Hip-Hop has chaaaanged.", 'submit_date': make_datetime('2002-11-12 00:01')}
}


class Quotable:
    """
    A dummy comment for use as template filler.
    
    Based on the models in django.contrib.comments.models
    """
    def __init__(self, comment_id, user_name, user_email, user_url, comment, submit_date):
        self.id = comment_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_url = user_url
        self.comment = comment
        self.submit_date = submit_date
        
    def print_comment(self):
        print "%s: %s" % (self.user_name, self.comment)


def get_comment_list():
    """
    Loop through a dictionary of dummy comments and pass them through the Quotable class.
    
    The idea is to simulate a Django queryset, which can then be passed into the template for greeking.
    """
    comment_list = []
    for k in HIPHOP.keys(): 
        q = Quotable(
                id=k,
                user_name=HIPHOP[k]['user_name'],
                user_email=HIPHOP[k]['user_email'],
                user_url=HIPHOP[k]['user_url'],
                comment=HIPHOP[k]['comment'],
                submit_date=HIPHOP[k]['submit_date'],
            )
        comment_list.append(q)
    return comment_list