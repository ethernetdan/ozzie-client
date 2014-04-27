import RPi.GPIO as GPIO
import time
import urllib2
import datetime
import socket
import logging
import os

# Setup Logging

logger = logging.getLogger('ozzie_app')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('app.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s",
                              "%Y-%m-%d %H:%M:%S")
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.debug("***********************")
logger.debug("*   OZ HAS STARTED!   *")
logger.debug("***********************\n")

logger.debug('setup started...')
logger.debug('running from: ' + os.getcwd())
 
def restart():
    logger.error("Restarting called!")
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output


# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

GPIO.setup(16,GPIO.IN)
input = GPIO.input(18)
# create dummy socket to get local IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com',0))
ip = s.getsockname()[0]
logger.info("Current IP is " + ip)

baseurl = "URL"
status = 'n'
delta = datetime.timedelta(minutes=20)
last = datetime.datetime.now() + delta

logger.debug('setup complete, starting session:\n')

while True:
	try:
		if (GPIO.input(16)):
			GPIO.output(18, True)
			if (status != 'o' or last <= datetime.datetime.now()):
				urllib2.urlopen(baseurl + "1").read()
				status = 'o'
				last = datetime.datetime.now() + delta
				logger.info('collider is open!')	
	
		else:
			GPIO.output(18, False)
	    		if (status != 'c' or last <= datetime.datetime.now()):
				urllib2.urlopen(baseurl + "0").read()
				status = 'c'
				last = datetime.datetime.now() + delta
				logger.info('collider is closed :(')
				
	except Exception as e:
		logger.exception(e)
		restart()
	finally:
		time.sleep(15);

logger.warning('the script stopped runnning')
GPIO.cleanup()
restart()
