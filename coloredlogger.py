#!/usr/bin/env python3
from colorama import Fore, Back, Style

class ColoredLogger(object):
	COLORS = Fore
	def __init__(self):
		self.configs = {
			'error':{'level': 1, 'prefix': '[-]', 'color': self.COLORS.RED},
			'info':{'level': 2, 'prefix': '[?]', 'color': self.COLORS.BLUE},
			'success':{'level': 3, 'prefix': '[+]', 'color': self.COLORS.GREEN},
			'verbose':{'level': 4, 'prefix': '[ ]', 'color': self.COLORS.WHITE},
		}

	def _color_print(self, cfg_name, *args, **kwargs):
		cfg = self.configs[cfg_name]
		print(cfg['color'] + cfg['prefix'], ' '.join(args), Style.RESET_ALL)

	def error(self, *args, **kwargs):
		self._color_print('error', *args, **kwargs)

	def success(self, *args, **kwargs):
		self._color_print('success', *args, **kwargs)

	def info(self, *args, **kwargs):
		self._color_print('info', *args, **kwargs)

	def log(self, *args, **kwargs):
		self._color_print('verbose', *args, **kwargs)


if __name__ == '__main__':
	logger = ColoredLogger()
	logger.error('Omg red as rose error')
	logger.success('Such success much green wow')
	logger.info('just a blue info')
	logger.log('some log here')
