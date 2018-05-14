.. -*- mode: rst -*-

pyfortified-logging
-------------------

This Python project is an extension of the native Python component `logging <https://docs.python.org/3/library/logging.html>`_
providing more robust message formatting for standard and JSON logging output, and in addtion allowing for extra
content populated as dictionaries.

Important Note
^^^^^^^^^^^^^^

This Python project is a refactoring of `logging-mv-integrations <https://pypi.org/project/logging-mv-integrations/>`_
for the purpose of general usage intent.

Work In Progress
^^^^^^^^^^^^^^^^

The following still needs to be performed for this Python project:

- Unit-testing: This project will be switching over to using Python native Unit testing framework `unittest <https://docs.python.org/3/library/unittest.html>`_.
- More concise documentation is required.
- Travis CI
- Badges


Badges
------

.. start-badges

.. list-table::
    :stub-columns: 1


.. |docs| image:: https://readthedocs.org/projects/pyfortified-logging/badge/?style=flat
    :alt: Documentation Status
    :target: http://pyfortified-logging.readthedocs.io

.. |hits| image:: http://hits.dwyl.io/jeff00seattle/pyfortified-logging.svg
    :alt: Hit Count
    :target: http://hits.dwyl.io/jeff00seattle/pyfortified-logging

.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: License Status
    :target: https://opensource.org/licenses/MIT

.. |travis| image:: https://travis-ci.org/jeff00seattle/pyfortified-logging.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/jeff00seattle/pyfortified-logging

.. |coveralls| image:: https://coveralls.io/repos/jeff00seattle/pyfortified-logging/badge.svg?branch=master&service=github
    :alt: Code Coverage Status
    :target: https://coveralls.io/r/jeff00seattle/pyfortified-logging

.. |requires| image:: https://requires.io/github/jeff00seattle/pyfortified-logging/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/jeff00seattle/pyfortified-logging/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/pyfortified_logging.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pyfortified_logging

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pyfortified-logging.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pyfortified-logging

.. end-badges


Install
-------

.. code-block:: bash

    pip install pyfortified_logging


Architecture
------------

``pyfortified-logging`` is an extension of the `logging facility for Python <https://docs.python.org/3/library/logging.html>`_
used for providing custom logger levels, format, and output.

.. image:: ./images/pyfortified_logging.png
   :scale: 50 %
   :alt: UML pyfortified-logging


Function: get_logger()
----------------------

.. code-block:: python

    def get_logger(
        logger_name,
        logger_version=None,
        logger_level=logging.INFO,
        logger_format=LoggingFormat.JSON,
        logger_output=LoggingOutput.STDOUT_COLOR,
        logger_handler=None
    ):


get_logger(): Parameters
^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------+-------------------------------------------------------------------------------------------------------------------------+
| Parameter       | Purpose                                                                                                                 |
+=================+=========================================================================================================================+
| logger_name     | Return a logger with the specified name or, if name is None, return a logger which is the root logger of the hierarchy. |
+-----------------+-------------------------------------------------------------------------------------------------------------------------+
| logger_version  |                                                                                                                         |
+-----------------+-------------------------------------------------------------------------------------------------------------------------+
| logger_format   | LoggingFormat                                                                                                           |
+-----------------+-------------------------------------------------------------------------------------------------------------------------+
| logger_output   | LoggingOutput                                                                                                           |
+-----------------+-------------------------------------------------------------------------------------------------------------------------+
| logger_handler  | logging.StreamHandler() or logging.FileHandler()                                                                        |
+-----------------+-------------------------------------------------------------------------------------------------------------------------+



Logging Levels
^^^^^^^^^^^^^^

Same Python logging levels, including one additional level NOTE.

+------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Level      | Purpose                                                                                                                                        |
+============+================================================================================================================================================+
| DEBUG      | Detailed information, typically of interest only when diagnosing problems.                                                                     |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| NOTE       | Detailed information, request processing, for example, request using cURL.                                                                     |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| INFO       | Confirmation that things are working as expected.  *[DEFAULT]*                                                                                 |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| WARNING    | An indication that something unexpected happened, or indicative of some problem in the near future. The software is still working as expected. |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| ERROR      | Due to a more serious problem, the software has not been able to perform some function.                                                        |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| CRITICAL   | A serious error, indicating that the program itself may be unable to continue running.                                                         |
+------------+------------------------------------------------------------------------------------------------------------------------------------------------+



Logging Format
^^^^^^^^^^^^^^

+------------+-------------------------------------------------------------------------------------------------------+
| Format     | Purpose                                                                                               |
+============+=======================================================================================================+
| STANDARD   | Standard logging format.                                                                              |
+------------+-------------------------------------------------------------------------------------------------------+
| JSON       | JSON logging format.  *[DEFAULT]*                                                                     |
+------------+-------------------------------------------------------------------------------------------------------+


.. code-block:: python

    class LoggingFormat(object):
        """TUNE Logging Format ENUM
        """
        STANDARD = "standard"
        JSON = "json"



Logging Output
^^^^^^^^^^^^^^

+--------------+----------------------------------------------------------------------------------------------+
| Output       | Purpose                                                                                      |
+==============+==============================================================================================+
| STDOUT       | Standard Output to terminal                                                                  |
+--------------+----------------------------------------------------------------------------------------------+
| STDOUT_COLOR | Standard Output using colored terminal                                                       |
+--------------+----------------------------------------------------------------------------------------------+
| FILE         | Standard Output to file created within *./tmp/log_<epoch time seconds>.json*.                |
+--------------+----------------------------------------------------------------------------------------------+


.. code-block:: python

    class LoggingOutput(object):
        """Logging Format ENUM
        """
        STDOUT = "stdout"
        STDOUT_COLOR = "color"
        FILE = "file"


Logging JSON Format
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import logging
    from pyfortified_logging import (LoggingFormat, get_logger, __version__)

    log = get_logger(
        logger_name=__name__,
        logger_version=__version__,
        logger_format=LoggingFormat.JSON,
        logger_level=logging.NOTE
    )

    log.info("logging: info", extra={'test': __name__})
    log.note("logging: note", extra={'test': __name__})
    log.debug("logging: debug", extra={'test': __name__})
    log.warning("logging: warning", extra={'test': __name__})
    log.error("logging: error", extra={'test': __name__})
    log.critical("logging: critical", extra={'test': __name__})
    log.exception("logging: exception", extra={'test': __name__})


Logging JSON Example Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ python3 examples/example_logging_json.py

    {"asctime": "2018-05-11 05:41:39 -0700", "levelname": "INFO", "name": "__main__",
    "version": "0.1.6", "message": "logging: info", "test": "__main__"}
    {"asctime": "2018-05-11 05:41:39 -0700", "levelname": "NOTE", "name": "__main__",
    "version": "0.1.6", "message": "logging: note", "test": "__main__"}
    {"asctime": "2018-05-11 05:41:39 -0700", "levelname": "WARNING", "name": "__main__",
    "version": "0.1.6", "message": "logging: warning", "test": "__main__"}
    {"asctime": "2018-05-11 05:41:39 -0700", "levelname": "ERROR", "name": "__main__",
    "version": "0.1.6", "message": "logging: error", "test": "__main__"}
    {"asctime": "2018-05-11 05:41:39 -0700", "levelname": "CRITICAL", "name": "__main__",
    "version": "0.1.6", "message": "logging: critical", "test": "__main__"}
    {"asctime": "2018-05-11 05:41:39 -0700", "levelname": "ERROR", "name": "__main__",
    "version": "0.1.6", "message": "logging: exception", "exc_info": "NoneType: None",
    "test": "__main__"}


Requirements
------------

``pyfortified-logging`` module is built upon Python 3 and has dependencies upon
several Python modules available within `Python Package Index PyPI <https://pypi.python.org/pypi>`_.

.. code-block:: bash

    make install-requirements

or


.. code-block:: bash

    python3 -m pip uninstall --yes --no-input -r requirements.txt
    python3 -m pip install --upgrade -r requirements.txt


Dependencies
^^^^^^^^^^^^

- coloredlogs: https://pypi.python.org/pypi/coloredlogs
- pprintpp: https://pypi.python.org/pypi/pprintpp
- python-json-logger: https://pypi.python.org/pypi/python-json-logger
- Pygments: https://pypi.python.org/pypi/Pygments
- safe-cast: https://pypi.python.org/pypi/safe-cast
- wheel: https://pypi.python.org/pypi/wheel
