#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace pyfortified_logging

import logging
from pyfortified_logging import (
    LoggingFormat,
    LoggingOutput,
    get_logger,
    __version__
)
from pprintpp import pprint

log = get_logger(
    logger_name=__name__,
    logger_version=__version__,
    logger_level=logging.NOTE,
    logger_format=LoggingFormat.JSON,
    logger_output=LoggingOutput.FILE
)

log.info("logging: info", extra={'test': __name__})
log.note("logging: note", extra={'test': __name__})
log.debug("logging: debug", extra={'test': __name__})
log.warning("logging: warning", extra={'test': __name__})
log.error("logging: error", extra={'test': __name__})
log.critical("logging: critical", extra={'test': __name__})
log.exception("logging: exception", extra={'test': __name__})

pprint("Logger file path: {0}".format(log.logger_path))

logger_fp = open(log.logger_path, 'r')
pprint(logger_fp.readlines())

pprint(log.getLevelName())
