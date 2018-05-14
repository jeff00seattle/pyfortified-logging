#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace pyfortified_logging


# @brief Logging Format ENUM
#
# @namespace pyfortified_logging.LoggingFormat
class LoggingFormat(object):
    """Logging Format ENUM
    """
    STANDARD = "standard"
    JSON = "json"

    @staticmethod
    def validate(value):
        if not value or value is None:
            return False
        if value in [LoggingFormat.STANDARD, LoggingFormat.JSON]:
            return True
        return False
