#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace pyfortified_logging

import logging
from pprintpp import pprint
from pyfortified_logging import (LoggingOutput, get_logger, __version__)

log = get_logger(
    logger_name=__name__,
    logger_version=__version__,
    logger_level=logging.NOTE,
    logger_output=LoggingOutput.STDOUT
)

log.info("logging: info", extra={'test': __name__})
log.note("logging: note", extra={'test': __name__})
log.debug("logging: debug", extra={'test': __name__})
log.warning("logging: warning", extra={'test': __name__})
log.error("logging: error", extra={'test': __name__})
log.critical("logging: critical", extra={'test': __name__})
log.exception("logging: exception", extra={'test': __name__})

pprint(log.getLevelName())
