# -*- coding: utf-8 -*-
"""
Pull pangrams from a variety of world languages for template testing.

A pangram is a phrase that includes every letter of an alphabet.

The list is drawn from the Web site of Markus Kuhn.
http://www.cl.cam.ac.uk/~mgk25/ucs/examples/quickbrown.txt
"""

PANGRAMS = {
    'en': 'The quick brown fox jumps over the lazy dog.',
    'da': 'Quizdeltagerne spiste jordbær med fløde, mens cirkusklovnen Wolther\
 spillede på xylofon.',
    'de': 'Falsches Üben von Xylophonmusik quält jeden größeren Zwerg.',
    'el': 'Γαζέες καὶ μυρτιὲς δὲν θὰ βρῶ πιὰ στὸ χρυσαφὶ ξέφωτο.',
    'es': 'El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y \
frío, añoraba a su querido cachorro.',
    'fr': "Portez ce vieux whisky au juge blond qui fume sur son île \
intérieure, à côté de l'alcôve ovoïde, où les bûches se consument dans l'âtre,\
 ce qui lui permet de penser à la cænogenèse de l'être dont il est question \
dans la cause ambiguë entendue à Moÿ, dans un capharnaüm qui, pense-t-il, \
diminue çà et là la qualité de son œuvre.",
    'ga': "D'fhuascail Íosa, Úrmhac na hÓighe Beannaithe, pór Éava agus \
Ádhaimh.",
    'hu': 'Árvíztűrő tükörfúrógép.',
    'is': 'Kæmi ný öxi hér ykist þjófum nú bæði víl og ádrepa.',
    'jp': """'いろはにほへとちりぬるを
  わかよたれそつねならむ
  うゐのおくやまけふこえて
  あさきゆめみしゑひもせす""",
    'he': '? דג סקרן שט בים מאוכזב ולפתע מצא לו חברה איך הקליטה.',
    'pl': 'Pchnąć w tę łódź jeża lub ośm skrzyń fig.',
    'ru': 'чащах юга жил бы цитрус? Да, но фальшивый экземпляр!',
    'tr': 'Pijamalı hasta, yağız şoföre çabucak güvendi.'
}


def get_pangram(language='en'):
    """
    Returns a pangram in the specified language. The default is English.
    """
    return PANGRAMS[language]


def get_html(pangram):
    """
    Renders the provided pangram in HTML by wrapping it in <p> tags.

    Linebreaks are replaced with <br> tags.
    """
    html = '<p>%s</p>' % pangram
    html = html.replace("\n", "<br>")
    return html
