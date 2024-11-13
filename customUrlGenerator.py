import json
import random

from os.path import dirname, join

from grammarinator.runtime import RuleContext, UnparserRule, UnlexerRule

from urlGenerator import urlGenerator

# TLD list is from ICANN
with open(join(dirname(__file__), 'tld_list.json')) as f:
    tld_list = json.load(f)

# Schemes from IANA
with open(join(dirname(__file__), 'scheme_list.json')) as f:
    schemes = json.load(f)


class customUrlGenerator(urlGenerator):
    tld_list = tld_list  # Class attribute to hold the TLD list

    # Customize the function generated from the htmlTagName parser rule to produce valid tag names.
    def tld(self, parent=None):
        with RuleContext(self, UnparserRule(name='tld', parent=parent)) as current:
            name = random.choice(tld_list)
            UnlexerRule(src=name, parent=current)
            return current

    def scheme(self, parent=None):
         with RuleContext(self, UnparserRule(name='scheme', parent=parent)) as current:
            name = random.choice(schemes)
            name += "://"
            UnlexerRule(src=name, parent=current)
            return current

