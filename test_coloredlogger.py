import pytest
import coloredlogger

def test_preconfigs():
	print()
	logger = coloredlogger.get_logger()
	logger.verbose("verbose")
	logger.info("info")
	logger.success("success")
	logger.error("error")

def test_custom_cfg():
	print()
	logger = coloredlogger.get_logger()
	logger.add_config('test', {
		'timestamp': '%d_%m_%Y',
		'header-only': True,
		'color': coloredlogger.COLORS.MAGENTA,
		'prefix': '|Test| Timestamp: {{TIME}}|'
	})
	logger.log('test', 'testing')

def test_cfg_overwrite():
	print()
	logger = coloredlogger.get_logger()
	logger.add_config('test', {'header-only': True})
	logger.log('test', 'testing 2')

def test_init_with_logger_name():
	print()
	logger = coloredlogger.get_logger('MY LOGGER', [{
		'config_name':'hi',
		'config':{
			'prefix': 'hi',
			'timestamp': False,
			'header-only':True,
			'color': coloredlogger.COLORS.LIGHTYELLOW_EX
	}}])
	logger.wtf('WHAAAT')
	logger.log('hi', 'there')
