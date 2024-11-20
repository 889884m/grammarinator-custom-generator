import random

import json
import random

from os.path import dirname, join

# TLD list from ICANN
with open("/Users/brooke_s/grammarinator-custom-generator/tld_list.json") as f:
    tld_list = json.load(f)

# Schemes from IANA
with open("/Users/brooke_s/grammarinator-custom-generator/tld_list.json") as f:
    schemes = json.load(f)

### switch to calling ICANN api instead? That way list is up to date


class myUrl():
    def __init__(self):
        pass

    # Customize the function generated from the htmlTagName parser rule to produce valid tag names.
    def tld(self, parent=None):
        with RuleContext(self, UnparserRule(name='tld', parent=parent)) as current:
            name = random.choice(tld_list)
            UnlexerRule(src=name, parent=current)
            return current

    def scheme(self, parent=None):
        name = random.choice(schemes)
        name += "://"
        return current

    def phrase(self, parent=None):
        return "path"

    def generateURL(self, number, scheme=None, subdomain=None, body=None, tld=None, path=None):
        lis = []
        for x in range(number):
            scheme = scheme or self.scheme()
            subdomain = subdomain or "www."
            body = body or self.body_generator()
            tld = tld or self.tld()
            path = '/' + self.phrase()
            url = scheme + subdomain + body + tld + path

        return lis


urlGen = myUrl()
urls = urlGen.generateURL(4)