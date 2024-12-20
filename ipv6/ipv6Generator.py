# Generated by Grammarinator 23.7

import itertools

from math import inf
from grammarinator.runtime import *

class ipv6Generator(Generator):


    def EOF(self, parent=None):
        pass
    EOF.min_depth = 0

    def start(self, parent=None):
        with RuleContext(self, UnparserRule(name='start', parent=parent)) as current:
            self.ipv6address(parent=current)
            return current
    start.min_depth = 4

    def ipv6address(self, parent=None):
        with RuleContext(self, UnparserRule(name='ipv6address', parent=parent)) as current:
            with AlternationContext(self, [3, 4], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.full_address, self.ipv4_linked][choice0](parent=current)
            return current
    ipv6address.min_depth = 3

    def full_address(self, parent=None):
        with RuleContext(self, UnparserRule(name='full_address', parent=parent)) as current:
            with AlternationContext(self, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 1:
                    self.ipv6_comp_st(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 2:
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 3:
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 4:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 5:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 6:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 7:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 8:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                elif choice0 == 9:
                    self.ipv6_comp_st(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 10:
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 11:
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 12:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 13:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 14:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 15:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                elif choice0 == 16:
                    self.ipv6_comp_st(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 17:
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 18:
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 19:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 20:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 21:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                elif choice0 == 22:
                    self.ipv6_comp_st(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 23:
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 24:
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 25:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 26:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                elif choice0 == 27:
                    self.ipv6_comp_st(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 28:
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 29:
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 30:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                elif choice0 == 31:
                    self.ipv6_comp_st(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 32:
                    self.ipv6_comp(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 33:
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                elif choice0 == 34:
                    self.ipv6_comp_st(parent=current)
                    self.ipv6_end(parent=current)
                elif choice0 == 35:
                    self.ipv6_comp(parent=current)
                elif choice0 == 36:
                    self.ipv6_comp_st(parent=current)
            return current
    full_address.min_depth = 2

    def ipv4_linked(self, parent=None):
        with RuleContext(self, UnparserRule(name='ipv4_linked', parent=parent)) as current:
            with AlternationContext(self, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 1:
                    self.ipv6_comp_st(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 2:
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 3:
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 4:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 5:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 6:
                    self.ipv6_comp_st(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 7:
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 8:
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 9:
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 10:
                    self.ipv6_comp_st(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 11:
                    self.ipv6_comp(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 12:
                    self.ipv6_group(parent=current)
                    self.ipv6_comp(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 13:
                    self.ipv6_comp_st(parent=current)
                    self.ipv6_group(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 14:
                    self.ipv6_comp(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
                elif choice0 == 15:
                    self.ipv6_comp_st(parent=current)
                    self.ipv4_linker(parent=current)
                    self.ipv4_address(parent=current)
            return current
    ipv4_linked.min_depth = 3

    def ipv6_group(self, parent=None):
        with RuleContext(self, UnparserRule(name='ipv6_group', parent=parent)) as current:
            self.fourhex(parent=current)
            self.COLON(parent=current)
            return current
    ipv6_group.min_depth = 2

    def ipv6_comp(self, parent=None):
        with RuleContext(self, UnparserRule(name='ipv6_comp', parent=parent)) as current:
            self.fourhex(parent=current)
            self.DOUBLECOLON(parent=current)
            return current
    ipv6_comp.min_depth = 2

    def ipv6_comp_st(self, parent=None):
        with RuleContext(self, UnparserRule(name='ipv6_comp_st', parent=parent)) as current:
            self.DOUBLECOLON(parent=current)
            return current
    ipv6_comp_st.min_depth = 1

    def ipv6_end(self, parent=None):
        with RuleContext(self, UnparserRule(name='ipv6_end', parent=parent)) as current:
            self.fourhex(parent=current)
            return current
    ipv6_end.min_depth = 2

    def ipv4_linker(self, parent=None):
        with RuleContext(self, UnparserRule(name='ipv4_linker', parent=parent)) as current:
            self.IPV4LINK(parent=current)
            self.COLON(parent=current)
            return current
    ipv4_linker.min_depth = 1

    def ipv4_address(self, parent=None):
        with RuleContext(self, UnparserRule(name='ipv4_address', parent=parent)) as current:
            self.threeoct(parent=current)
            self.PERIOD(parent=current)
            self.threeoct(parent=current)
            self.PERIOD(parent=current)
            self.threeoct(parent=current)
            self.PERIOD(parent=current)
            self.threeoct(parent=current)
            return current
    ipv4_address.min_depth = 2

    def fourhex(self, parent=None):
        with RuleContext(self, UnparserRule(name='fourhex', parent=parent)) as current:
            with AlternationContext(self, [1, 1, 1, 1], [1, 1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    self.HEXDIGITNOZERO(parent=current)
                    self.HEXDIGIT(parent=current)
                    self.HEXDIGIT(parent=current)
                    self.HEXDIGIT(parent=current)
                elif choice0 == 1:
                    self.HEXDIGITNOZERO(parent=current)
                    self.HEXDIGIT(parent=current)
                    self.HEXDIGIT(parent=current)
                elif choice0 == 2:
                    self.HEXDIGITNOZERO(parent=current)
                    self.HEXDIGIT(parent=current)
                elif choice0 == 3:
                    self.HEXDIGITNOZERO(parent=current)
            return current
    fourhex.min_depth = 1

    def threeoct(self, parent=None):
        with RuleContext(self, UnparserRule(name='threeoct', parent=parent)) as current:
            with AlternationContext(self, [1, 1, 1], [1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    self.DECIMAL(parent=current)
                    self.DECIMAL(parent=current)
                    self.DECIMAL(parent=current)
                elif choice0 == 1:
                    self.DECIMAL(parent=current)
                    self.DECIMAL(parent=current)
                elif choice0 == 2:
                    self.DECIMAL(parent=current)
            return current
    threeoct.min_depth = 1

    def HEXDIGIT(self, parent=None):
        with RuleContext(self, UnlexerRule(name='HEXDIGIT', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[1]), parent=current)
            return current
    HEXDIGIT.min_depth = 0

    def HEXDIGITNOZERO(self, parent=None):
        with RuleContext(self, UnlexerRule(name='HEXDIGITNOZERO', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[2]), parent=current)
            return current
    HEXDIGITNOZERO.min_depth = 0

    def COLON(self, parent=None):
        with RuleContext(self, UnlexerRule(name='COLON', parent=parent)) as current:
            UnlexerRule(src=':', parent=current)
            return current
    COLON.min_depth = 0

    def DOUBLECOLON(self, parent=None):
        with RuleContext(self, UnlexerRule(name='DOUBLECOLON', parent=parent)) as current:
            UnlexerRule(src='::', parent=current)
            return current
    DOUBLECOLON.min_depth = 0

    def DECIMAL(self, parent=None):
        with RuleContext(self, UnlexerRule(name='DECIMAL', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[3]), parent=current)
            return current
    DECIMAL.min_depth = 0

    def PERIOD(self, parent=None):
        with RuleContext(self, UnlexerRule(name='PERIOD', parent=parent)) as current:
            UnlexerRule(src='.', parent=current)
            return current
    PERIOD.min_depth = 0

    def IPV4LINK(self, parent=None):
        with RuleContext(self, UnlexerRule(name='IPV4LINK', parent=parent)) as current:
            UnlexerRule(src='ffff', parent=current)
            return current
    IPV4LINK.min_depth = 0

    _default_rule = start

    _charsets = {
        0: list(itertools.chain.from_iterable([range(32, 127)])),
        1: list(itertools.chain.from_iterable([range(48, 58), range(97, 103)])),
        2: list(itertools.chain.from_iterable([range(49, 58), range(97, 103)])),
        3: list(itertools.chain.from_iterable([range(48, 58)])),
    }
