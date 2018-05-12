#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace logging_fortified

import logging

log = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)
log.setLevel(logging.DEBUG)

log.debug("Don't step on the %s", "broken glass")

log.info("Hello World")

logging.debug("This message should go to the log file")
logging.info("So should this")
logging.warning("And this, too")