import random
import timeit
import json
import rstr
import os

from os.path import dirname, join

# TLD list from ICANN
with open(join(dirname(__file__), "../tld_list.json")) as f:
    tld_list = json.load(f)

# Schemes from IANA
with open(join(dirname(__file__), "../scheme_list.json")) as f:
    schemes = json.load(f)


class myUrl():
    def __init__(self):
        self.chars = 'qwertyuioplkjhgfdsazxcvbnm1234567890-.'


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
        
        if not os.path.exists('tests'):
            os.makedirs('tests')

        existing_files = os.listdir('tests')
        existing_indexes = []
        for filename in existing_files:
            index = int(filename.split('_')[1].split('.')[0])
            existing_indexes.append(index)
        next_index = max(existing_indexes, default=-1) + 1

        for element in lis:
            filename = f"tests/test_{next_index}.txt"
            with open(filename, "w") as file:
                file.write(element)
            next_index += 1
        

        return lis
