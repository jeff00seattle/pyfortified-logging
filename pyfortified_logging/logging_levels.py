#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace pyfortified_logging

import logging

NOTE_NUM = 15
logging.NOTE = NOTE_NUM
logging.addLevelName(NOTE_NUM, "NOTE")


def get_logging_level(
    str_logging_level
):
    assert str_logging_level
    str_logging_level = str_logging_level.upper()

    return {
        'NOTSET': logging.NOTSET,
        'DEBUG': logging.DEBUG,
        'NOTE': logging.NOTE,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }.get(str_logging_level, logging.INFO)
