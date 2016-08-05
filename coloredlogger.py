#!/usr/bin/env python3
from colorama import Fore, Back, Style
import copy

class ColoredLogger(object):
	COLORS = Fore
	_DEFAULT_CFG = {'level': 10, 'prefix': '[ ]', 'color': COLORS.WHITE, 'header-only': False}
	def __init__(self):
		self.configs = {
			'error':{'level': 1, 'prefix': '[-]', 'color': self.COLORS.RED, 'header-only': False},
			'info':{'level': 2, 'prefix': '[?]', 'color': self.COLORS.BLUE, 'header-only': False},
			'success':{'level': 3, 'prefix': '[+]', 'color': self.COLORS.GREEN, 'header-only': False},
			'verbose':{'level': 4, 'prefix': '[ ]', 'color': self.COLORS.WHITE, 'header-only': False},
		}

	def add_config(self, config_name, config):
		if type(config_name) != str or type(config) != dict:
			raise TypeError('config_name is not str or config is not dict')

		cfg = copy.deepcopy(self._DEFAULT_CFG)
		for k in cfg.keys():
			if k in config:
				cfg[k] = config[k]

		self.configs[config_name] = config

	def _color_print(self, cfg_name, *args, **kwargs):
		cfg = self.configs[cfg_name]
		header_suffix = ''
		if cfg['header-only']:
			header_suffix = self.COLORS.WHITE
		print(cfg['color'] + cfg['prefix'] + header_suffix, ' '.join(args), Style.RESET_ALL)

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
	logger.add_config('my-log', {'prefix': "ROCK!",'color': ColoredLogger.COLORS.CYAN, 'header-only': True})
	logger.custom('my-log', 'YOU!')
	logger.custom('my-log', 'ALL!')
	# AVAILABLE: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
