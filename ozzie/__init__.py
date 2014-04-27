import logging
import ConfigParser
from ozzie import Ozzie
import os

# Setup Config Parser
config = ConfigParser.ConfigParser()
config.read("settings.cfg")

# Setup logging
logger = logging.getLogger('ozzie_app')
logLevel = config.getint("Logging", "Level")
logger.setLevel(logLevel)

logFile = config.get("Logging", "Filename")
fh = logging.FileHandler(logFile)
fh.setLevel(logLevel)

formatter = logging.Formatter(config.get("Logging", "Format", raw=True),
	config.get("Logging", "DateFormat"))
fh.setFormatter(formatter)
logger.addHandler(fh)

if config.has_option("Logging", "Welcome"):
	msg = config.get("Logging", "Welcome")
	logger.debug('*' * (len(msg)+8))
	logger.debug('*   ' + msg + '   *')
	logger.debug('*' * (len(msg)+8)+'\n')

from backend import OzzieFirebase
backend = OzzieFirebase(config)

ozzie = Ozzie(config, logger)




