#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace pyfortified_logging

import io
import logging
import json
from pyfortified_logging import (
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
    logger_format=LoggingFormat.JSON,
    logger_output=LoggingOutput.STDOUT,
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
buffer_str = buffer_str.replace('\n',',')
buffer_str = buffer_str[:-1]
buffer_str = '[' + buffer_str + ']'

logJson = json.loads(buffer_str)
pprint(logJson)
buffer.close()

pprint(log.getLevelName())

