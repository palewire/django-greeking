from django.test import TestCase
from django.template import Template, Context
from django.utils.encoding import smart_unicode


class GreekingTemplateTagTests(TestCase):
    
    def render(self, t, **c):
        ctx = Context(c)
        out = Template(t).render(ctx)
        return ctx, out
    
    def testJabberwocky(self):
        """
        Tests the tag for pulling jabberwocky
        """
        from greeking.jabberwocky import get_grafs, get_html
        graph_range = range(1, 8)
        for graphs in graph_range:
            t = "{% load greeking_tags %}{% jabberwocky " + str(graphs) + " %}"
            ctx, out = self.render(t)
            match = get_html(get_grafs(graphs))
            self.assertEqual(out, match)
        
    def testPangrams(self):
        """
        Tests the tag for pulling pangrams
        """
        from greeking.pangrams import PANGRAMS, get_pangram, get_html
        languages = PANGRAMS.keys()
        for language in languages:
            t = "{% load greeking_tags %}{% pangram " + language + " %}"
            ctx, out = self.render(t)
            match = get_html(get_pangram(language))
            self.assertEqual(out, smart_unicode(match))
    
    def testGreekComments(self):
        """
        Tests the tag for pulling greek comments
        """
        from greeking import quotables
        t = "{% load greeking_tags %}{% greek_comment_list as comment_list %}"
        ctx, out = self.render(t)
        for comment in list(ctx['comment_list']):
            comment_dict = {
                'user_name': comment.user_name,
                'user_email': comment.user_email,
                'user_url': comment.user_url,
                'comment': comment.comment,
                'submit_date': comment.submit_date
            }
            match = quotables.HIPHOP[comment.comment_id]
            for k, v in comment_dict.items():
                self.assertEqual(v, match[k])
        
    def testPlaceKittens(self):
        """
        Tests the tag for pulling placekitten images.
        """
        t1 = "{% load greeking_tags %}{% placekitten 200 200 %}"
        ctx, out = self.render(t1)
        self.assertEqual(out, '<img src="http://placekitten.com/200/200/"/>')
        t2 = "{% load greeking_tags %}{% placekitten 200 200 gray %}"
        ctx, out = self.render(t2)
        self.assertEqual(out, '<img src="http://placekitten.com/g/200/200/"/>')

