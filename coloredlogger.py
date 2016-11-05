#!/usr/bin/env python3
from __future__ import print_function
from colorama import Fore, Back, Style
from time import strftime
import copy

COLORS = Fore

def getLogger(cfg_name=None, config=None):
	logger = ColoredLogger()
	if cfg_name != None and config != None:
		logger.add_config(cfg_name, config)
	return logger


class ColoredLogger(object):
	_DEFAULT_CFG = {'level': 10, 'timestamp': '%Y-%m-%d %H:%M:%S', 'prefix': '[ ]', 'color': COLORS.WHITE, 'header-only': False}
	def __init__(self):
		self.configs = {
			'error':{'level': 1, 'prefix': '[-]', 'color': COLORS.RED},
			'info':{'level': 2, 'prefix': '[?]', 'color': COLORS.BLUE},
			'success':{'level': 3, 'prefix': '[+]', 'color': COLORS.GREEN},
			'verbose':{'level': 4, 'prefix': '[ ]', 'color': COLORS.WHITE},
		}
		for ck in self.configs:
			cfg = self.configs[ck]
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

		cfg = copy.deepcopy(self._DEFAULT_CFG)
		for k in cfg.keys():
			if k in config:
				cfg[k] = config[k]

		self.configs[config_name] = cfg

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

		sep = ' '
		if 'sep' in kwargs:
			sep = kwargs['sep']

		print(ts + cfg['color'] + cfg['prefix'] + header_suffix, sep.join(args), Style.RESET_ALL)

	def error(self, *args, **kwargs):
		self._color_print('error', *args, **kwargs)

	def success(self, *args, **kwargs):
		self._color_print('success', *args, **kwargs)

	def info(self, *args, **kwargs):
		self._color_print('info', *args, **kwargs)

	def log(self, *args, **kwargs):
		self._color_print('verbose', *args, **kwargs)

	def custom(self, *args, **kwargs):
		self._color_print(args[0], *args[1:], **kwargs)

if __name__ == '__main__':
	logger = ColoredLogger()
	logger.error('Omg red as rose error')
	logger.success('Such success much green wow')
	logger.info('just a blue info')
	logger.log('some log here')
	# make your own logger mode
	logger.add_config('my-log', {'prefix': "ROCK!",'color': COLORS.CYAN, 'header-only': True})
	logger.custom('my-log', 'YOU!')
	logger.custom('my-log', 'ALL!')
	logger.custom('my-log', 'test', 'with', 'at', 'symbols', sep='@')
	# AVAILABLE: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
