#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace logging_fortified

import io
import logging
from logging_fortified import (
    LoggingFormat,
    LoggingOutput,
    get_logger,
    __version__
)
from pprintpp import pprint

buffer = io.StringIO()
logger_handler = logging.StreamHandler(buffer)

log = get_logger(
    logger_name=__name__,
    logger_version=__version__,
    logger_level=logging.NOTE,
    logger_output=LoggingOutput.STDOUT,
    logger_format=LoggingFormat.STANDARD,
    logger_handler=logger_handler
)

log.info("logging: info", extra={'test': __name__})
log.note("logging: note", extra={'test': __name__})
log.debug("logging: debug", extra={'test': __name__})
log.warning("logging: warning", extra={'test': __name__})
log.error("logging: error", extra={'test': __name__})
log.critical("logging: critical", extra={'test': __name__})
log.exception("logging: exception", extra={'test': __name__})

buffer_str = buffer.getvalue()
buffer_lines = buffer_str.splitlines()
pprint(buffer_lines)

buffer.close()

pprint(log.getLevelName())
