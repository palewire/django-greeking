from django.test import TestCase
from django.template import Template, Context

class GreekingTemplateTagTests(TestCase):

    def render(self, t, **c):
        ctx = Context(c)
        out = Template(t).render(ctx)
        return ctx, out

    def testJabberwocky(self):
        """
        Tests the tag for pulling jabberwocky
        """
        from greeking.jabberwocky import *
        t = "{% load greeking %}{% jabberwocky %}"
        match = get_html(get_grafs())
        ctx, out = self.render(t, c=match)
        self.assertEqual(out, "")
        self.assertEqual(list(ctx["jabberwocky"]), [match])