#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace pyfortified_logging


# @brief Logging Output ENUM
#
# @namespace pyfortified_logging.LoggingOutput
class LoggingOutput(object):
    """Logging Output ENUM
    """
    STDOUT = "stdout"
    STDOUT_COLOR = "color"
    FILE = "file"

    @staticmethod
    def validate(value):
        if not value or value is None:
            return False
        if value in [LoggingOutput.STDOUT, LoggingOutput.STDOUT_COLOR, LoggingOutput.FILE]:
            return True
        return False
