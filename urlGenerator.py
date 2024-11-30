# Generated by Grammarinator 23.7.post111+gb0dbdcd

from math import inf
from grammarinator.runtime import *

class urlGenerator(Generator):


    def start(self, parent=None):
        with UnparserRuleContext(self, 'start', parent) as rule:
            current = rule.current
            self.url(parent=current)
        return current

    def url(self, parent=None):
        with UnparserRuleContext(self, 'url', parent) as rule:
            current = rule.current
            self._reserve(4, self.scheme, parent=current)
            self._reserve(3, self.subdomain, parent=current)
            self._reserve(1, self.body, parent=current)
            self.tld(parent=current)
            with QuantifierContext(rule, 0, 0, 1, urlGenerator._quant_sizes[1], 0) as quant0:
                while quant0():
                    with QuantifiedContext(rule):
                        current = rule.current
                        self.path(parent=current)
            current = rule.current
        return current

    def body(self, parent=None):
        with UnparserRuleContext(self, 'body', parent) as rule:
            current = rule.current
            self._reserve(1, self.TEXT, parent=current)
            self.T__0(parent=current)
        return current

    def tld(self, parent=None):
        with UnparserRuleContext(self, 'tld', parent) as rule:
            current = rule.current
            with AlternationContext(rule, 0, urlGenerator._alt_sizes[1], 0, urlGenerator._alt_conds[1]) as alt0:
                current = rule.current
                choice0 = alt0()
                if choice0 == 0:
                    self.T__1(parent=current)
                elif choice0 == 1:
                    self.T__2(parent=current)
                elif choice0 == 2:
                    self.T__3(parent=current)
                elif choice0 == 3:
                    self.T__4(parent=current)
                elif choice0 == 4:
                    self._reserve(1, self.phrase, parent=current)
                    self.T__0(parent=current)
            current = rule.current
        return current

    def path(self, parent=None):
        with UnparserRuleContext(self, 'path', parent) as rule:
            current = rule.current
            with AlternationContext(rule, 0, urlGenerator._alt_sizes[2], 0, urlGenerator._alt_conds[2]) as alt0:
                current = rule.current
                choice0 = alt0()
                if choice0 == 0:
                    self._reserve(1, self.T__5, parent=current)
                    self.phrase(parent=current)
                elif choice0 == 1:
                    self._reserve(3, self.T__5, parent=current)
                    self._reserve(2, self.phrase, parent=current)
                    self.path(parent=current)
            current = rule.current
        return current

    def phrase(self, parent=None):
        with UnparserRuleContext(self, 'phrase', parent) as rule:
            current = rule.current
            with AlternationContext(rule, 0, urlGenerator._alt_sizes[3], 0, urlGenerator._alt_conds[2]) as alt0:
                current = rule.current
                choice0 = alt0()
                if choice0 == 0:
                    self.TEXT(parent=current)
                elif choice0 == 1:
                    self._reserve(1, self.TEXT, parent=current)
                    self.phrase(parent=current)
            current = rule.current
        return current

    def TEXT(self, parent=None):
        with UnlexerRuleContext(self, 'TEXT', parent) as rule:
            current = rule.current
            with AlternationContext(rule, 0, urlGenerator._alt_sizes[0], 0, urlGenerator._alt_conds[0]) as alt0:
                current = rule.current
                choice0 = alt0()
                if choice0 == 0:
                    with QuantifierContext(rule, 0, 1, inf, urlGenerator._quant_sizes[0], 0) as quant0:
                        while quant0():
                            with QuantifiedContext(rule):
                                current = rule.current
                                current.src += self._model.charset(current, 0, urlGenerator._charsets[1])
                    current = rule.current
                elif choice0 == 1:
                    with QuantifierContext(rule, 1, 1, inf, urlGenerator._quant_sizes[0], 0) as quant1:
                        while quant1():
                            with QuantifiedContext(rule):
                                current = rule.current
                                current.src += self._model.charset(current, 1, urlGenerator._charsets[2])
                    current = rule.current
                elif choice0 == 2:
                    current.src += self._model.charset(current, 2, urlGenerator._charsets[1])
                    self.TEXT(parent=current)
                elif choice0 == 3:
                    current.src += self._model.charset(current, 3, urlGenerator._charsets[2])
                    self.TEXT(parent=current)
            current = rule.current
        return current

    def scheme(self, parent=None):
        with UnparserRuleContext(self, 'scheme', parent) as rule:
            current = rule.current
            with AlternationContext(rule, 0, urlGenerator._alt_sizes[4], 0, urlGenerator._alt_conds[2]) as alt0:
                current = rule.current
                [self.T__6, self.T__7][alt0()](parent=current)
            current = rule.current
        return current

    def subdomain(self, parent=None):
        with UnparserRuleContext(self, 'subdomain', parent) as rule:
            current = rule.current
            self.T__8(parent=current)
        return current

    def T__0(self, parent=None):
        with UnlexerRuleContext(self, 'T__0', parent, True) as rule:
            current = rule.current
            current.src += '.'
        return current

    def T__1(self, parent=None):
        with UnlexerRuleContext(self, 'T__1', parent, True) as rule:
            current = rule.current
            current.src += 'com'
        return current

    def T__2(self, parent=None):
        with UnlexerRuleContext(self, 'T__2', parent, True) as rule:
            current = rule.current
            current.src += 'org'
        return current

    def T__3(self, parent=None):
        with UnlexerRuleContext(self, 'T__3', parent, True) as rule:
            current = rule.current
            current.src += 'net'
        return current

    def T__4(self, parent=None):
        with UnlexerRuleContext(self, 'T__4', parent, True) as rule:
            current = rule.current
            current.src += 'gov'
        return current

    def T__5(self, parent=None):
        with UnlexerRuleContext(self, 'T__5', parent, True) as rule:
            current = rule.current
            current.src += '/'
        return current

    def T__6(self, parent=None):
        with UnlexerRuleContext(self, 'T__6', parent, True) as rule:
            current = rule.current
            current.src += 'https://'
        return current

    def T__7(self, parent=None):
        with UnlexerRuleContext(self, 'T__7', parent, True) as rule:
            current = rule.current
            current.src += 'http://'
        return current

    def T__8(self, parent=None):
        with UnlexerRuleContext(self, 'T__8', parent, True) as rule:
            current = rule.current
            current.src += 'www.'
        return current


    _default_rule = start

    _rule_sizes = {
        'start': RuleSize(3, 5),
        'url': RuleSize(2, 5),
        'body': RuleSize(1, 2),
        'tld': RuleSize(1, 1),
        'path': RuleSize(2, 2),
        'phrase': RuleSize(1, 1),
        'TEXT': RuleSize(0, 0),
        'scheme': RuleSize(1, 1),
        'subdomain': RuleSize(1, 1),
        'T__0': RuleSize(0, 0),
        'T__1': RuleSize(0, 0),
        'T__2': RuleSize(0, 0),
        'T__3': RuleSize(0, 0),
        'T__4': RuleSize(0, 0),
        'T__5': RuleSize(0, 0),
        'T__6': RuleSize(0, 0),
        'T__7': RuleSize(0, 0),
        'T__8': RuleSize(0, 0),
    }

    _alt_sizes = (
        (RuleSize(0, 0), RuleSize(0, 0), RuleSize(1, 1), RuleSize(1, 1)),  # 0
        (RuleSize(1, 1), RuleSize(1, 1), RuleSize(1, 1), RuleSize(1, 1), RuleSize(2, 2)),  # 1
        (RuleSize(2, 2), RuleSize(3, 4)),  # 2
        (RuleSize(1, 1), RuleSize(2, 2)),  # 3
        (RuleSize(1, 1), RuleSize(1, 1)),  # 4
    )

    _alt_conds = (
        (1, 1, 1, 1),  # 0
        (1, 1, 1, 1, 1),  # 1
        (1, 1),  # 2
    )

    _quant_sizes = (
        RuleSize(0, 0),  # 0
        RuleSize(3, 2),  # 1
    )

    _charsets = (
        Generator._charset(((0x20, 0x7f), )),  # 0
        Generator._charset(((0x61, 0x7b), )),  # 1
        Generator._charset(((0x30, 0x3a), )),  # 2
    )