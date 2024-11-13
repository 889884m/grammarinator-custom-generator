import json
import random

from os.path import dirname, join

from grammarinator.runtime import UnlexerRule, UnparserRuleContext

from HTMLGenerator import HTMLGenerator


with open(join(dirname(__file__), 'tld_list.json')) as f:
    tld_list = json.load(f)


class customUrlGenerator(urlGenerator):
    tld_list = tld_list  # Class attribute to hold the TLD list

    # Customize the function generated from the htmlTagName parser rule to produce valid tag names.
    def htmlTagName(self, parent=None):
        with UnparserRuleContext(gen=self, name='tld', parent=parent) as rule:
            current = rule.current
            name = random.choice(tld_list)
            current.src += name
            return current

