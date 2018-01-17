#!/usr/bin/python3
from pymisp  import PyMISP 
import configparser
import json   
_instance = None
__all__ = ['MakeConn', 'create_conn']
def _get_instance():
	global _instance
	if _instance is None:
		_instance = MakeConn()
	return _instance

def create_conn():
	return _get_instance.get()

class MakeConn(object):
	def __init__(self, auth_file='auth.config', user_data='user.json'):
		self.auth_file = auth_file
		self.user_data = user_data
	def get(self):
		return self.mkconn(self.read(self.auth_file))
	__call__ = get

	@staticmethod
	def read(auth_f):
		config = configparser.ConfigParser()
		config.read(auth_f)
		return config

	@staticmethod
	def get_user(udata):
		with open(udata) as json_data:
			user_array = json.load(json_data)
		return user_array
	@staticmethod
	def mkconn(auth):
		misp = PyMISP(auth.get("cred", "misp_url"), auth.get("cred", "misp_key"), True, 'json', debug=True)
		return misp
