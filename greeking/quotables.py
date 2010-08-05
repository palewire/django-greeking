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
    5: {'user_name': 'Butterfly', 'user_email': 'butterfly@9thwonder.org', 'user_url': 'http://www.lyricstime.com/digable-planets-rebirth-of-slick-cool-like-dat-lyrics.html', 'comment': "How was the buzz entire hip hop era? Was fresh and fat since they started sayin’ Audi. Cause funks made fat from right beneath my hoodie. The puba of the styles like Miles and shit. Like sixties funky worms with waves and perms. Just sendin’ chunky rhythms right down ya block. We be to rap what key be to lock.", 'submit_date': make_datetime('1993-09-27 00:01')},
    6: {'user_name': 'Phife Dawg', 'user_email': 'diggy@canikick.it', 'user_url': 'http://www.lyricstime.com/a-tribe-called-quest-award-tour-lyrics.html', 'comment': "Comin’ with more hits than the Braves and the Yankees. Livin’ mad phat like an oversized Bam-bi. The wackest crews try to dis, it makes me laugh. When my track record’s longer than a DC-20 aircraft. So next time that you think you want somethin’ here. Make somethin’ differ, take that garbage to St. Elsewhere.", 'submit_date': make_datetime('1993-11-09 00:01')},
    7: {'user_name': 'Del', 'user_email': 'funkee@sunnymeadowz.com', 'user_url': 'http://www.lyricstime.com/del-the-funky-homosapien-sunny-meadowz-lyrics.html', 'comment': "I sit and write scriptures by the old wishin’ well. Collect all my notes and sail a boat back to Berkeley. Tries fill my vibe ’cause my style is rather earthly. Some say it's wack but I ain’t tryin’ to hear it. As long as what I do contains my soul and my spirit.", 'submit_date': make_datetime('1991-10-22 00:01')},
    8: {'user_name': 'Notorious B.I.G.', 'user_email': 'bee.eye.gee@brooklyn.com', 'user_url': 'http://www.azlyrics.com/lyrics/notoriousbig/ilovethedough.html', 'comment': "Now we buy homes in unfamiliar places. Tito smile everytime he see our faces.", 'submit_date': make_datetime('1997-03-25 00:16')},
    9: {'user_name': 'Jay-Z', 'user_email': 'jigga@brooklyn.com', 'user_url': 'http://www.lyricsmode.com/lyrics/s/scarface/guess_whos_back_feat_jay_z_beanie_sigel.html', 'comment': "Face it y'all, y'all n----- playin' basic ball. I'm on the block like I'm eight feet tall.", 'submit_date': make_datetime('2002-08-06 05:00')},
    10: {'user_name': 'Skoob', 'user_email': 'skoob@brooklyn.com', 'user_url': 'http://www.musicsonglyrics.com/D/dasefxlyrics/dasefxrealhiphoplyrics.htm', 'comment': 'We the ruffest dream team, reign Supreme like a Cutlass. Get duckets, the dough. Can\'t touch the flow.', 'submit_date': make_datetime('1995-08-26 12:01') },
}



class Quotable:
    """
    A dummy comment for use as template filler.
    
    Based on the models in django.contrib.comments.models
    """
    def __init__(self, comment_id, user_name, user_email, user_url, comment, submit_date):
        self.comment_id = comment_id
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
                comment_id=k,
                user_name=HIPHOP[k]['user_name'],
                user_email=HIPHOP[k]['user_email'],
                user_url=HIPHOP[k]['user_url'],
                comment=HIPHOP[k]['comment'],
                submit_date=HIPHOP[k]['submit_date']
            )
        comment_list.append(q)
    return comment_list
