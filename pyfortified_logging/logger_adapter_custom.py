#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace pyfortified_logging

import copy
import logging

from .logging_levels import NOTE_NUM

class LoggerAdapterCustom(logging.LoggerAdapter):
    """
    An adapter for loggers which makes it easier to specify contextual
    information in logging output.
    """

    __logger_output = None
    __logger_file = None


    def __init__(self, logger_output, logger_path, *args, **kwargs):
        """
        Initialize the adapter
        """
        self.__logger_output = logger_output
        self.__logger_path = logger_path

        super(LoggerAdapterCustom, self).__init__(*args, **kwargs)

    @property
    def logging_output(self):
        return self.__logger_output

    @property
    def logger_path(self):
        return self.__logger_path

    def process(self, msg, kwargs):
        """
        Process the logging message and keyword arguments.
        """
        try:
            _kwargs = copy.deepcopy(kwargs)
        except TypeError:
            _kwargs = kwargs

        extra = _kwargs.get('extra')
        if extra:
            _kwargs['extra'].update({'version': self.extra['version']})
        else:
            _kwargs['extra'] = {'version': self.extra['version']}
        return msg, _kwargs

    def note(self, msg, *args, **kwargs):
        """
        Delegate an note call to the underlying logger.
        """
        self.log(NOTE_NUM, msg, *args, **kwargs)

    def getLevelName(self):
        return logging.getLevelName(self.getEffectiveLevel())