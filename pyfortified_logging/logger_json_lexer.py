#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace pyfortified_logging

import pygments.lexer
import re
from pygments.token import (
    Text,
    Keyword,
    Name,
    String,
    Number,
    Punctuation,
    STANDARD_TYPES
)

STANDARD_TYPES.update({
    String.Double.Logger: 's2l',
    String.Double.Logger.Asctime: 's2la',
    String.Double.Logger.Curl: 's2lc',
    String.Double.Logger.Name: 's2ln',
    String.Double.Logger.Message: 's2lm',
    String.Double.Logger.Message.Success: 's2lms',
    String.Double.Logger.Message.Error: 's2lme',
    String.Double.Logger.Version.Multiverse: 's2lvm',
    String.Double.Logger.Version.Requests: 's2lvr',
    String.Double.Logger.Level.Info: 's2lli',
    String.Double.Logger.Level.Debug: 's2lld',
    String.Double.Logger.Level.Warning: 's2llw',
    String.Double.Logger.Level.Error: 's2lle',
    String.Double.Logger.Level.Critical: 's2llc'
})


class LoggerJsonLexer(pygments.lexer.RegexLexer):
    """
    For JSON data structures.

    .. versionadded:: 0.1
    """

    name = 'Logger JSON'
    aliases = ['json']
    filenames = ['*.json']
    mimetypes = ['application/json']

    flags = re.DOTALL

    # integer part of a number
    int_part = r'^\d*$'

    # fractional part of a number
    frac_part = r'\.\d+'

    # exponential part of a number
    exp_part = r'[eE](\+|-)?\d+'

    value_asctime = r'"\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d [\-|\+]\d\d\d\d"'

    value_level_info = r'"INFO"'
    value_level_debug = r'"DEBUG"'
    value_level_warning = r'"WARNING"'
    value_level_error = r'"ERROR"'
    value_level_critical = r'"CRITICAL"'

    attr_message = r'"message"'
    attr_message = r'"message"'

    tokens = {
        'whitespace': [(r'\s+', Text)],

        # represents a simple terminal value
        'simplevalue': [
            (r'(true|false|null)', Keyword.Constant),

            (int_part, Number.Integer),
            (value_asctime, String.Double.Logger.Asctime),
            (value_level_info, String.Double.Logger.Level.Info),
            (value_level_debug, String.Double.Logger.Level.Debug),
            (value_level_warning, String.Double.Logger.Level.Warning),
            (value_level_error, String.Double.Logger.Level.Error),
            (value_level_critical, String.Double.Logger.Level.Critical),
            (r'"[\w\:\s]*(Success)[\w\:\s]*"', String.Double.Logger.Message.Success),
            (r'"[\w\:\s]*(Fail|Error)[\w\:\s]*"', String.Double.Logger.Message.Error),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
        ],

        # the right hand side of an object, after the attribute name
        'json_attribute': [
            pygments.lexer.include('json_value'),
            (r':', Punctuation),
            # comma terminates the attribute but expects more
            (r',', Punctuation, '#pop'),
            # a closing bracket terminates the entire object, so pop twice
            (r'\}', Punctuation, ('#pop:2')),
        ],

        # a json object - { attr, attr, ... }
        'json_object': [
            pygments.lexer.include('whitespace'), (
                r'("name")(:)(\s+)(".+?")',
                pygments.lexer.bygroups(Name.Tag, Punctuation, Text, String.Double.Logger.Name), 'json_attribute'
            ), (
                r'("message")(:)(\s+)("[\w\:\s]*(Success)[\w\:\s]*")',
                pygments.lexer.bygroups(Name.Tag, Punctuation, Text, String.Double.Logger.Message.Success),
                'json_attribute'
            ), (
                r'("message")(:)(\s+)("[\w\:\s]*(Fail|Error)[\w\:\s]*")',
                pygments.lexer.bygroups(Name.Tag, Punctuation, Text, String.Double.Logger.Message.Error),
                'json_attribute'
            ), (
                r'("message")(:)(\s+)(".+?")',
                pygments.lexer.bygroups(Name.Tag, Punctuation, Text, String.Double.Logger.Message), 'json_attribute'
            ), (
                r'("request_curl"|"error_request_curl")(:)(\s+)(".+?")',
                pygments.lexer.bygroups(Name.Tag, Punctuation, Text, String.Double.Logger.Curl), 'json_attribute'
            ), (r'"(\\\\|\\"|[^"])*"', Name.Tag, 'json_attribute'), (r'\}', Punctuation, '#pop')
        ],

        # json array - [ value, value, ... }
        'json_array': [
            pygments.lexer.include('whitespace'),
            pygments.lexer.include('json_value'),
            (r',', Punctuation),
            (r'\]', Punctuation, '#pop'),
        ],

        # a json value - either a simple value or a complex value (object or array)
        'json_value': [
            pygments.lexer.include('whitespace'),
            pygments.lexer.include('simplevalue'),
            (r'\{', Punctuation, 'json_object'),
            (r'\[', Punctuation, 'json_array'),
        ],

        # the root of a json document would be a value
        'root': [pygments.lexer.include('json_value')],
    }
