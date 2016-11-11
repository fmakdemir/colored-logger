.. role:: cmd(code)
   :language: python

.. role:: red

.. role:: green

.. role:: blue

.. role:: teal

************************
ColoredLogger for Python
************************

.. image:: https://img.shields.io/pypi/v/coloredlogger.svg
    :target: https://pypi.python.org/pypi/coloredlogger/
.. image:: https://img.shields.io/badge/wheel-yes-brightgreen.svg
    :target: https://pypi.python.org/pypi/coloredlogger/
.. image:: https://travis-ci.org/Fmakdemir/colored-logger.svg?branch=master
    :target: https://travis-ci.org/Fmakdemir/colored-logger


Colored Logger for Python that uses clorama for colorful output with timestamp
and customizable format. Colored Logger has timestamp, colored header or full line,
and custom time format

Colored Logger for Python that uses clorama for colorful output with timestamp and customizable format

Setup
#####

Use :cmd:`pip install coloredlogger` to install using pip or
use source code and install requirements with :cmd:`pip install -r requirements.txt`

get a logger with:

.. code-block:: python

    from coloredlogger import ColoredLogger
    logger = ColoredLogger()

or get logger with optional config name and config

.. code-block:: python

    import coloredlogger
    logger = coloredlogger.get_logger(cfg_name=OPTIONAL_CONFIG_NAME, OPTIONAL_CONFIG)

log using pre-setup methods:

.. code-block:: python

    logger.error('A red error')
    logger.success('A green success message')
    logger.info('A blue info message')
    logger.verbose('Or just some verbose log')

And you should see:

.. image:: https://github.com/Fmakdemir/colored-logger/blob/master/assets/coloredlog-1.png?raw=true

..
    | 2016-11-05 21:35:55 :red:`[-] Omg red as rose error`
    | 2016-11-05 21:35:55 :green:`[+] Such success much green wow`
    | 2016-11-05 21:35:55 :blue:`[?] just a blue info`
    | 2016-11-05 21:35:55 [ ] some log here

or make your own log method using a name prefix color level and whether only
header will be colored or the whole line:

.. code-block:: python

    logger.add_config('my-log', {'prefix': "ROCK!",'color': ColoredLogger.COLORS.CYAN, 'header-only': True})
    logger.log('my-log', 'YOU!')
    logger.log('my-log', 'ALL!')

..
    | 2016-11-05 21:35:55 :teal:`ROCK!` YOU!
    | 2016-11-05 21:35:55 :teal:`ROCK!` ALL!
    | 2016-11-05 21:35:55 :teal:`ROCK!` test@with@at@symbols

And you should see:

.. image:: https://github.com/Fmakdemir/colored-logger/blob/master/assets/coloredlog-2.png?raw=true

You can also overwrite previous configs by:

.. code-block:: python

    logger.add_config('error', {'prefix': 'Custom error with {{TIME}}: ', 'header-only': True})

This will overwrite :code:`error` config's properties with given ones which
are :code:`prefix` and :code:`header-only`

Config object
#############
All keys are optional and if not given will be overridden by defaults

.. code-block:: python

    {
        'level': 10, # integer
        'timestamp': '%Y-%m-%d %H:%M:%S', # timestamp format used with strftime
        'prefix': '[ ]', # prefix which can include {{TIME}} to put timestamp with
        'color': coloredlogger.COLORS.WHITE, # one of coloredlogger.COLORS
        'header-only': False # whether or not color whole line or just header
    }

COLORS Object
*************
Fore colors from clorama library

