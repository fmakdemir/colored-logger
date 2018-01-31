#!/usr/bin/env python3
from __future__ import print_function
from colorama import Fore, Back, Style
from time import strftime
import copy
import sys

COLORS = Fore

def get_logger(name=None, configs=None):
	logger = ColoredLogger(name=name)
	logger.add_configs(configs)
	return logger

_DEFAULT_CFG = {'level': 10, 'timestamp': '%Y-%m-%d %H:%M:%S', 'prefix': '[ ]', 'color': COLORS.WHITE, 'header-only': False}

class ColoredLogger(object):
	def __init__(self, name=None):
		self._DEFAULT_CFG = copy.deepcopy(_DEFAULT_CFG)
		self.configs = {
			'wtf':{'level': 0, 'prefix': '[X]', 'color': COLORS.MAGENTA},
			'error':{'level': 1, 'prefix': '[-]', 'color': COLORS.RED},
			'info':{'level': 2, 'prefix': '[?]', 'color': COLORS.BLUE},
			'success':{'level': 3, 'prefix': '[+]', 'color': COLORS.GREEN},
			'verbose':{'level': 4, 'prefix': '[ ]', 'color': COLORS.WHITE},
		}
		if name:
			prefix = self._DEFAULT_CFG['prefix']
			self._DEFAULT_CFG['prefix'] = '[%s] %s' % (name, prefix)
		for ck in self.configs:
			cfg = self.configs[ck]
			if name:
				cfg['prefix'] = '[%s] %s' % (name, cfg['prefix'])
			for k in self._DEFAULT_CFG:
				if k not in cfg:
					cfg[k] = self._DEFAULT_CFG[k]
			if cfg['timestamp'] == True:
				cfg['timestamp'] = self._DEFAULT_CFG['timestamp']
			elif cfg['timestamp'] == '' or type(cfg['timestamp']) != str:
				cfg['timestamp'] = False

	def add_config(self, config_name, config):
		if type(config_name) != str or type(config) != dict:
			raise TypeError('config_name is not str or config is not dict')
		# if we have a copy with same name just update it or copy from default
		if config_name in self.configs:
			cfg = self.configs[config_name]
		else:
			cfg = copy.deepcopy(self._DEFAULT_CFG)
		for k in cfg.keys():
			if k in config:
				cfg[k] = config[k]

		self.configs[config_name] = cfg

	def add_configs(self, configs=None):
		if not configs:
			return
		if type(configs) != list:
			raise TypeError('Invalid config list received: %s' % repr(configs))
		for cfg in configs:
			if type(cfg) == dict and 'config_name' in cfg and 'config' in cfg:
				self.add_config(**cfg)
			else:
				raise TypeError('Invalid config received: %s' % repr(cfg))

	def _color_print(self, cfg_name, *args, **kwargs):
		try:
			cfg = self.configs[cfg_name]
		except KeyError:
			raise(KeyError('Config "%s" not found' % cfg_name))

		header_suffix = ''
		if cfg['header-only']:
			header_suffix = COLORS.WHITE

		ts = ''
		if cfg['timestamp'] != False:
			ts = strftime(cfg['timestamp']) + ' '
		prefix = cfg['prefix'][:] # copy to not mess prefix
		if '{{TIME}}' in prefix:
			prefix = prefix.replace('{{TIME}}', ts)
			ts = ''

		sep = ' '
		if 'sep' in kwargs:
			sep = kwargs['sep']
		header = ts + cfg['color'] + prefix + header_suffix
		args = list(args)
		args.append(Style.RESET_ALL)
		# TODO: change to python logger
		print(header, *args, **kwargs)
		# flush to show changes
		sys.stdout.flush()

	def error(self, *args, **kwargs):
		self._color_print('error', *args, **kwargs)

	def success(self, *args, **kwargs):
		self._color_print('success', *args, **kwargs)

	def info(self, *args, **kwargs):
		self._color_print('info', *args, **kwargs)

	def verbose(self, *args, **kwargs):
		self._color_print('verbose', *args, **kwargs)

	def wtf(self, *args, **kwargs):
		self._color_print('wtf', *args, **kwargs)

	def log(self, *args, **kwargs):
		self._color_print(args[0], *args[1:], **kwargs)

if __name__ == '__main__':
	logger = ColoredLogger()
	logger.wtf('WTF??')
	logger.error('Omg red as rose error')
	logger.success('Such success much green wow')
	logger.info('just a blue info')
	logger.verbose('some log here')
	# make your own logger mode
	logger.add_config('my-log', {'prefix': "ROCK!",'color': COLORS.CYAN, 'header-only': True})
	logger.log('my-log', 'YOU!')
	logger.log('my-log', 'ALL!')
	logger.log('my-log', 'test', 'with', 'at', 'symbols', sep='@')
	# AVAILABLE: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
	logger.add_config('error', {'prefix': 'Custom error with {{TIME}}: ', 'timestamp': '[%Hh:%Mm:%Ss]', 'header-only': True})
	logger.error('Overwritten error log! Red header with time')
	for i in range(100000000):
		pass
	logger.error('test showing time is working')
	# named logger with custom log
	logger = get_logger('MY LOG', [{'config_name': 'custom-log', 'config': {'timestamp': '%Y/%m/%d %H:%M:%S'}}])
	logger.info('This should have MY LOG [?] as prefix')
	logger.success('This should have MY LOG [+] as prefix')
	logger.verbose('Yeey')
	logger.log('custom-log', 'This custom log should have overwritten timestamp')
