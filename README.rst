ColoredLogger for Python
########################

Colored Logger for Python that uses clorama for colorful output with timestamp and customizable format

Setup
-----

First install requirements with `pip install -r requirements.txt` or use pip install coloredlogger

get a logger with:

.. code-block:: python
	from coloredlogger import ColoredLogger
	logger = ColoredLogger()

or get logger with optional config name and config

.. code-block:: python
	import coloredlogger
	logger = coloredlogger.getLogger(cfg_name=OPTIONAL_CONFIG_NAME, OPTIONAL_CONFIG)

log using pre-setup methods:

.. code-block:: python
	logger.error('A red error')
	logger.success('A green success message')
	logger.info('A blue info message')
	logger.log('Or just some verbose log')


or make your own log method using a name prefix color level and whether only
header will be colored or the whole line:

.. code-block:: python
	logger.add_config('my-log', {'prefix': "ROCK!",'color': ColoredLogger.COLORS.CYAN, 'header-only': True})
	logger.custom('my-log', 'YOU!')
	logger.custom('my-log', 'ALL!')

Config object
-------------
All keys are optional and if not given will be overridden by defaults
.. code-block:: python
	{
		'level': 10, # integer
		'timestamp': '%Y-%m-%d %H:%M:%S', # timestamp format used with strftime
		'prefix': '[ ]', # prefix which can include {{TIME}} to put timestamp with
		'color': coloredlogger.COLORS.WHITE, # one of coloredlogger.COLORS
		'header-only': False # whether or not color whole line or just header
	}

colors
??????
colors from clorama library

