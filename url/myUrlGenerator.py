import random

import json
import random
import rstr

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
        self.chars = 'qwertyuioplkjhgfdsazxcvbnm1234567890-'


    def tld(self, parent=None):
            return random.choice(tld_list)

    def scheme(self, parent=None):
        return random.choice(schemes) + "://"

    def body_generator(self, depth, parent=None):
        body_depth  = random.randrange(1, depth)
        body_text = ''
        for x in range(body_depth):
            new_char = random.choice(self.chars)
            body_text += new_char
        return body_text + '.'

    def phrase(self, depth, parent=None):
        path_depth  = random.randrange(1, depth)
        path_text = ''
        for x in range(path_depth):
            new_char = random.choice(self.chars)
            path_text += new_char
        return path_text

    def generateURL(self, number=1, depth=10, scheme=None, subdomain=None, body=None, tld=None, path=None):
        lis = []
        for x in range(number):
            up_scheme = scheme or self.scheme()
            curr_scheme = up_scheme.lower()
            curr_subdomain = subdomain or "www."
            curr_body = body or self.body_generator(depth)
            if curr_body[-1] != '.':
                curr_body += '.'
            up_tld = tld or self.tld()
            curr_tld = up_tld.lower()
            curr_path = '/' + self.phrase(depth)
            curr_url = curr_scheme + curr_subdomain + curr_body + curr_tld + curr_path
            lis.append(curr_url)

        return lis


urlGen = myUrl()
timeit.
urls = urlGen.generateURL(30, 20)
print(urls)

