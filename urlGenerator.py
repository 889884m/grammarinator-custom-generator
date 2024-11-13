# Generated by Grammarinator 23.7

import itertools

from math import inf
from grammarinator.runtime import *

class urlGenerator(Generator):


    def EOF(self, parent=None):
        pass
    EOF.min_depth = 0

    def start(self, parent=None):
        with RuleContext(self, UnparserRule(name='start', parent=parent)) as current:
            self.url(parent=current)
            self.EOF(parent=current)
            return current
    start.min_depth = 3

    def url(self, parent=None):
        with RuleContext(self, UnparserRule(name='url', parent=parent)) as current:
            self.scheme(parent=current)
            self.subdomain(parent=current)
            self.body(parent=current)
            self.tld(parent=current)
            if self._max_depth >= 3:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.path(parent=current)
            return current
    url.min_depth = 2

    def body(self, parent=None):
        with RuleContext(self, UnparserRule(name='body', parent=parent)) as current:
            self.TEXT(parent=current)
            UnlexerRule(src='.', parent=current)
            return current
    body.min_depth = 1

    def tld(self, parent=None):
        with RuleContext(self, UnparserRule(name='tld', parent=parent)) as current:
            with AlternationContext(self, [0, 0, 0, 0, 2], [1, 1, 1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    UnlexerRule(src='com', parent=current)
                elif choice0 == 1:
                    UnlexerRule(src='org', parent=current)
                elif choice0 == 2:
                    UnlexerRule(src='net', parent=current)
                elif choice0 == 3:
                    UnlexerRule(src='gov', parent=current)
                elif choice0 == 4:
                    self.phrase(parent=current)
                    UnlexerRule(src='.', parent=current)
            return current
    tld.min_depth = 0

    def path(self, parent=None):
        with RuleContext(self, UnparserRule(name='path', parent=parent)) as current:
            with AlternationContext(self, [2, 3], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    UnlexerRule(src='/', parent=current)
                    self.phrase(parent=current)
                elif choice0 == 1:
                    UnlexerRule(src='/', parent=current)
                    self.phrase(parent=current)
                    self.path(parent=current)
            return current
    path.min_depth = 2

    def phrase(self, parent=None):
        with RuleContext(self, UnparserRule(name='phrase', parent=parent)) as current:
            with AlternationContext(self, [1, 2], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    self.TEXT(parent=current)
                elif choice0 == 1:
                    self.TEXT(parent=current)
                    self.phrase(parent=current)
            return current
    phrase.min_depth = 1

    def TEXT(self, parent=None):
        with RuleContext(self, UnlexerRule(name='TEXT', parent=parent)) as current:
            with AlternationContext(self, [0, 0, 1, 1], [1, 1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    if self._max_depth >= 0:
                        for _ in self._model.quantify(current, 0, min=1, max=inf):
                            UnlexerRule(src=self._model.charset(current, 0, self._charsets[1]), parent=current)
                elif choice0 == 1:
                    if self._max_depth >= 0:
                        for _ in self._model.quantify(current, 1, min=1, max=inf):
                            UnlexerRule(src=self._model.charset(current, 1, self._charsets[2]), parent=current)
                elif choice0 == 2:
                    UnlexerRule(src=self._model.charset(current, 2, self._charsets[3]), parent=current)
                    self.TEXT(parent=current)
                elif choice0 == 3:
                    UnlexerRule(src=self._model.charset(current, 3, self._charsets[4]), parent=current)
                    self.TEXT(parent=current)
            return current
    TEXT.min_depth = 0

    def scheme(self, parent=None):
        with RuleContext(self, UnparserRule(name='scheme', parent=parent)) as current:
            with AlternationContext(self, [0, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                UnlexerRule(src=['https://', 'http://'][choice0], parent=current)
            return current
    scheme.min_depth = 0

    def subdomain(self, parent=None):
        with RuleContext(self, UnparserRule(name='subdomain', parent=parent)) as current:
            UnlexerRule(src='www.', parent=current)
            return current
    subdomain.min_depth = 0

    _default_rule = start

    _charsets = {
        0: list(itertools.chain.from_iterable([range(32, 127)])),
        1: list(itertools.chain.from_iterable([range(97, 123)])),
        2: list(itertools.chain.from_iterable([range(48, 58)])),
        3: list(itertools.chain.from_iterable([range(97, 123)])),
        4: list(itertools.chain.from_iterable([range(48, 58)])),
    }
