#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace pyfortified_logging

import os
import logging
import logging.config
import time
import math

from .logging_json_formatter import LoggingJsonFormatter
from .logger_adapter_custom import LoggerAdapterCustom

from .logging_format import LoggingFormat
from .logging_output import LoggingOutput


def get_logger(
    logger_name,
    logger_version=None,
    logger_level=logging.INFO,
    logger_format=LoggingFormat.JSON,
    logger_output=LoggingOutput.STDOUT_COLOR,
    logger_handler=None,
    logger_filename=None
):
    """
        logger_name      Return a logger with the specified logger_name, creating it if necessary.
        logger_level     Set the root logger level to the specified level.
        logger_format    LoggerFormat.
        logger_output    LoggerOutput.
        logger_handler   Provide custom logging handler.
    """
    if logger_format == LoggingFormat.STANDARD:
        formatter = logging.Formatter(
            '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        )
    else:
        formatter = LoggingJsonFormatter(
            logger_name,
            logger_version,
            logger_output=logger_output,
            fmt='%(asctime)s %(levelname)s %(name)s %(version)s %(message)s'
        )

    logger_path = None
    if logger_handler is None:
        if logger_output == LoggingOutput.FILE:
            logging_dir = "./tmp"
            if not os.path.isdir(logging_dir):
                os.makedirs(logging_dir)

            if logger_filename is None:
                # logger_name_tag = logger_name.replace('.', '_')

                # Log name combines logger_format and epoch time in seconds
                # rounded-up to the nearest 10 seconds
                epoch_time_sec = int(time.time())
                epoch_time_sec_ceil = int(math.ceil((epoch_time_sec + 10) / 10.0)) * 10

                logger_filename = "log_{0}".format(epoch_time_sec_ceil)

            logger_path = "{0}/{1}.json".format(logging_dir, logger_filename)
            if not os.path.isfile(logger_path):
                open(logger_path, "w+")

            logger_handler = logging.FileHandler(logger_path, encoding='utf-8')
        else:
            logger_handler = logging.StreamHandler()

    logger_handler.setFormatter(formatter)

    log = logging.getLogger(logger_name)
    log.setLevel(logger_level)

    if not len(log.handlers):
        log.addHandler(logger_handler)

    return LoggerAdapterCustom(logger_output, logger_path, log, {'version': logger_version})
