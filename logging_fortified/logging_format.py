#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace logging_fortified


# @brief Logging Format ENUM
#
# @namespace logging_fortified.LoggingFormat
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
