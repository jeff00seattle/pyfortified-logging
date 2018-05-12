#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace logging_fortified

import sys
from pygments.token import Error
from logging_fortified import (LoggerJsonLexer)
from pprintpp import pprint

num = 10
showall = False
ignerror = False
lexer = None
options = {}
profile = False
profsort = 4


def main():
    lx = LoggerJsonLexer()
    lno = 1
    debug_lexer = True

    text = '{"asctime": "2016-09-17 16:16:14 -0700", "levelname": "INFO", "name": "abc_def_ghi", ' \
           '"version": "0.0.0.0", "message": "Upload Config", "download_path": "tmp/download.json", "timeout": 1200}'
    tokens = []
    states = []

    def show_token(tok, state):
        reprs = list(map(repr, tok))
        print('   ' + reprs[1] + ' ' + ' ' * (29 - len(reprs[1])) + reprs[0], end=' ')
        if debug_lexer:
            print(' ' + ' ' * (29 - len(reprs[0])) + ' : '.join(state) if state else '', end=' ')
        print()

    for type, val in lx.get_tokens(text):
        pprint({'type': type, 'val': val})

        lno += val.count('\n')
        if type == Error and not ignerror:
            print('Error parsing on line', lno)
            if not showall:
                print('Previous tokens' + (debug_lexer and ' and states' or '') + ':')
                for i in range(max(len(tokens) - num, 0), len(tokens)):
                    if debug_lexer:
                        show_token(tokens[i], states[i])
                    else:
                        show_token(tokens[i], None)
            print('Error token:')
            l = len(repr(val))
            print('   ' + repr(val), end=' ')
            if debug_lexer and hasattr(lx, 'ctx'):
                print(' ' * (60 - l) + ' : '.join(lx.ctx.stack), end=' ')
            print()
            print()
            return 1
        tokens.append((type, val))
        if debug_lexer:
            if hasattr(lx, 'ctx'):
                states.append(lx.ctx.stack[:])
            else:
                states.append(None)
        if showall:
            show_token((type, val), states[-1] if debug_lexer else None)
    return 0


if __name__ == '__main__':
    ret = main()
    sys.exit(bool(ret))
