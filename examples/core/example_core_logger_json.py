#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace logging_fortified

import logging
from logging.config import dictConfig

log_config = {
    "version": 1,
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "fmt": "[%(asctime)s] %(levelname)s::[%(process)d %(thread)d]::%(module)s - %(message)s",
        },
    },
    "handlers": {
        "stream": {
            "level": "DEBUG",
            "formatter": "json",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "example_logger": {
            "handlers": ["stream"],
            "level": "DEBUG",
            "propagate": True,
        },
    }
}

# Configure logging
dictConfig(log_config)
log = logging.getLogger("example_logger")

log.debug("Don't step on the %s", "broken glass")

log.info("Hello World")

logging.debug("This message should go to the log file")
logging.info("So should this")
logging.warning("And this, too")

log.info("Hello World")