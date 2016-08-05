# pyColoredLogger
Colored Logger library for python

get a logger with:

```
from coloredlogger import ColoredLogger
logger = ColoredLogger()
```

log using pre-setup methods:

```
logger.error('A red error')
logger.success('A green success message')
logger.info('A blue info message')
logger.log('Or just some verbose log')
```

or make your own log method using a name prefix color level and whether only
header will be colored or the whole line:

```
logger.add_config('my-log', {'prefix': "ROCK!",'color': ColoredLogger.COLORS.CYAN, 'header-only': True})
logger.custom('my-log', 'YOU!')
logger.custom('my-log', 'ALL!')
```

