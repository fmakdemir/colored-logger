import pytest
import coloredlogger

def test_preconfigs():
	print()
	logger = coloredlogger.get_logger()
	logger.verbose("verbose")
	logger.info("info")
	logger.success("success")
	logger.error("error")

def test_custom_cfg_and_cfg_overwrite():
	print()
	logger = coloredlogger.get_logger()
	logger.add_config('test', {'timestamp': '%d_%m_%Y', 'headermonly': True, 'color': coloredlogger.COLORS.MAGENTA, 'prefix': '|Test| Timestamp: {{TIME}}|'})
	logger.log('test', 'testing')
	logger.add_config('test', {'header-only': False})
	logger.log('test', 'testing 2')

