'''
Author: Michael Shieh
Date: 3/12/2021

This file contains the configuration for the web service.
'''
class Config(object):
	pass

class ProdConfig(Config):
	pass

class DevConfig(Config):
	DEBUG = True
