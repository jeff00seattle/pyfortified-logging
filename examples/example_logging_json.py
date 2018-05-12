#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace logging_fortified

from pprintpp import pprint
import logging
from logging_fortified import (
    LoggingFormat,
    LoggingOutput,
    get_logger,
    __version__
)

log = get_logger(
    logger_name=__name__,
    logger_version=__version__,
    logger_level=logging.NOTE,
    logger_format=LoggingFormat.JSON,
    logger_output=LoggingOutput.STDOUT
)

log.info("logging: info", extra={'test': __name__})
log.debug("logging: debug", extra={'test': __name__})
log.note("logging: note", extra={'test': __name__})
log.warning("logging: warning", extra={'test': __name__})
log.error("logging: error", extra={'test': __name__})
log.critical("logging: critical", extra={'test': __name__})
log.exception("logging: exception", extra={'test': __name__})

pprint(log.getLevelName())
