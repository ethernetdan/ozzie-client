#import RPi.GPIO as GPIO
import time
import urllib2
import datetime
import socket
import logging
import os
import backend

# Setup Logging



class Ozzie:

	def __init__(self, config, logger):

		logger.debug('setup started...')
		logger.debug('running from: ' + os.getcwd())

		self.ip = getLocalIP()
		logger.info("Current LAN IP is " + self.ip)

		self.data = backend.OzzieFirebase(config)
		self.data.pollServer("thisisatest")



def getLocalIP():
	# create dummy socket to get local IP
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('google.com',0))
	return s.getsockname()[0]
		



	
 
# def restart():
#     logger.error("Restarting called!")
#     command = "/usr/bin/sudo /sbin/shutdown -r now"
#     import subprocess
#     process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
#     output = process.communicate()[0]
#     print output


# # setup GPIO
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(18, GPIO.OUT)

# GPIO.setup(16,GPIO.IN)
# input = GPIO.input(18)


# baseurl = "URL"
# status = 'n'
# delta = datetime.timedelta(minutes=20)
# last = datetime.datetime.now() + delta

# logger.debug('setup complete, starting session:\n')

# while True:
# 	try:
# 		if (GPIO.input(16)):
# 			GPIO.output(18, True)
# 			if (status != 'o' or last <= datetime.datetime.now()):
# 				urllib2.urlopen(baseurl + "1").read()
# 				status = 'o'
# 				last = datetime.datetime.now() + delta
# 				logger.info('collider is open!')	
	
# 		else:
# 			GPIO.output(18, False)
# 	    		if (status != 'c' or last <= datetime.datetime.now()):
# 				urllib2.urlopen(baseurl + "0").read()
# 				status = 'c'
# 				last = datetime.datetime.now() + delta
# 				logger.info('collider is closed :(')
				
# 	except Exception as e:
# 		logger.exception(e)
# 		restart()
# 	finally:
# 		time.sleep(15);

# logger.warning('the script stopped runnning')
# GPIO.cleanup()
# restart()
