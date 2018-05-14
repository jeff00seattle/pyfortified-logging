#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace pyfortified_logging

import datetime as dt
import json
import sys
from collections import OrderedDict

import pygments.formatters
import pygments.lexer
import pygments.style
import tzlocal
from pygments import highlight
from pythonjsonlogger import jsonlogger
from .logger_json_lexer import LoggerJsonLexer
from .logging_output import LoggingOutput

COLOR_SCHEME = {
    pygments.token.Token: ('darkgray', 'darkgray'),
    pygments.token.Whitespace: ('', ''),
    pygments.token.Comment: ('', ''),
    pygments.token.Comment.Preproc: ('', ''),
    pygments.token.Keyword: ('white', 'white'),
    pygments.token.Keyword.Constant: ('fuchsia', 'fuchsia'),
    pygments.token.Keyword.Type: ('white', 'white'),
    pygments.token.Operator.Word: ('', ''),
    pygments.token.Name.Builtin: ('', ''),
    pygments.token.Name.Function: ('', ''),
    pygments.token.Name.Namespace: ('', ''),
    pygments.token.Name.Class: ('', ''),
    pygments.token.Name.Exception: ('', ''),
    pygments.token.Name.Decorator: ('darkgray', 'darkgray'),
    pygments.token.Name.Variable: ('', ''),
    pygments.token.Name.Constant: ('', ''),
    pygments.token.Name.Attribute: ('', ''),
    pygments.token.Name.Tag: ('darkgray', 'darkgray'),
    pygments.token.String: ('lightgray', 'lightgray'),
    pygments.token.String.Double: ('lightgray', 'lightgray'),
    pygments.token.String.Double.Logger.Asctime: ('lightgray', 'lightgray'),
    pygments.token.String.Double.Logger.Name: ('teal', 'turquoise'),
    pygments.token.String.Double.Logger.Message: ('brown', 'yellow'),
    pygments.token.String.Double.Logger.Message.Success: ('darkgreen', 'green'),
    pygments.token.String.Double.Logger.Message.Error: ('red', 'red'),
    pygments.token.String.Double.Logger.Curl: ('darkgreen', 'green'),
    pygments.token.String.Double.Logger.Level.Info: ('white', 'white'),
    pygments.token.String.Double.Logger.Level.Debug: ('darkgreen', 'green'),
    pygments.token.String.Double.Logger.Level.Warning: ('brown', 'yellow'),
    pygments.token.String.Double.Logger.Level.Error: ('red', 'red'),
    pygments.token.String.Double.Logger.Level.Critical: ('*red*', '*red*'),
    pygments.token.Number: ('white', 'white'),
    pygments.token.Number.Integer: ('white', 'white'),
    pygments.token.Generic.Deleted: ('', ''),
    pygments.token.Generic.Inserted: ('', ''),
    pygments.token.Generic.Heading: ('', ''),
    pygments.token.Generic.Subheading: ('', ''),
    pygments.token.Generic.Error: ('red', 'red'),
    pygments.token.Error: ('red', 'red')
}


class LoggingJsonFormatter(jsonlogger.JsonFormatter):
    """
    A custom formatter to format logging records as json strings.
    extra values will be formatted as str() if nor supported by
    json default encoder
    """

    __logger_versions = {}

    def __init__(self, logger_name, logger_version, logger_output, *args, **kwargs):
        _logger_name = logger_name.split('.')[0]
        self.logger_output = logger_output
        if __name__ not in self.logger_versions:
            self.add_logger_version(_logger_name, logger_version)
        super(LoggingJsonFormatter, self).__init__(*args, **kwargs)

    @property
    def logger_versions(self):
        return self.__logger_versions

    @logger_versions.setter
    def logger_versions(self, value):
        self.__logger_versions = value

    def add_logger_version(self, logger_name, logger_version):
        self.__logger_versions.update({logger_name: logger_version})

    def get_logger_output(self):
        return self.logger_output

    def get_logger_version(self, logger_name):
        _logger_version = None
        logger_name_parts = logger_name.split('.')

        while len(logger_name_parts) > 0:
            _logger_name = '.'.join(logger_name_parts)
            _logger_version = self.logger_versions.get(_logger_name, None)

            if _logger_version is not None:
                break

            del logger_name_parts[-1]

        return _logger_version

    def converter(self, timestamp):
        tz = tzlocal.get_localzone()
        return dt.datetime.fromtimestamp(timestamp, tz)

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            return ct.strftime(datefmt)
        else:
            return ct.strftime("%Y-%m-%d %H:%M:%S %z")

    def jsonify(self, log_record):
        """Returns a json string of the log record."""
        log_record_clean = OrderedDict()
        for key, value in log_record.items():
            log_record_clean[key] = value[0] if value else None

        formatted_json = json.dumps(log_record_clean, default=self.json_default, cls=self.json_encoder)
        return formatted_json

    def format(self, record):
        """Formats a log record and serializes to json"""

        message_dict = {}
        if isinstance(record.msg, dict):
            message_dict = record.msg
            record.message = None
        else:
            record.message = record.getMessage()

        # only format time if needed
        if "asctime" in self._required_fields:
            record.asctime = self.formatTime(record, self.datefmt)

        # Display formatted exception, but allow overriding it in the
        # user-supplied dict.
        if record.exc_info and not message_dict.get('exc_info'):
            message_dict['exc_info'] = self.formatException(record.exc_info)

        try:
            log_record = OrderedDict()
        except NameError:
            log_record = {}

        self.add_fields(log_record, record, message_dict)
        log_record = self.process_log_record(log_record)
        log_record['version'] = self.get_logger_version(logger_name=log_record['name'])

        prefix_log = OrderedDict()
        extra_log = OrderedDict()

        for k, v in log_record.items():
            if k in ['asctime', 'levelname', 'name', 'version', 'message']:
                prefix_log[k] = v
            else:
                extra_log[k] = v

        extra_log_sorted = OrderedDict(sorted(extra_log.items()))

        log_record_ordered = OrderedDict()
        for k, e in prefix_log.items():
            log_record_ordered.setdefault(k, []).append(e)
        for k, e in extra_log_sorted.items():
            log_record_ordered.setdefault(k, []).append(e)

        formatted_json = self.jsonify(log_record_ordered)

        if (self.logger_output == LoggingOutput.STDOUT_COLOR or self.logger_output is None) \
                and sys.stdin.isatty():
            json_lexer = LoggerJsonLexer()
            term_formatter = pygments.formatters.TerminalFormatter(colorscheme=COLOR_SCHEME)

            return highlight(formatted_json, json_lexer, term_formatter).rstrip('\n')

        return formatted_json
