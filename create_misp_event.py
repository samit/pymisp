#!/usr/bin/python3
import misp_conn
from pymisp import PyMISP  
import configparser

_instance = None
__all__ = ['CreateMispEvent', 'create_mevent']

def _get_instance():
	global _instance
	if _instance is None:
		_instance = CreateMispEvent
	return _instance

def create_mevent():
	return _get_instance.create_misp_event()

class CreateMispEvent(object):
	def __init__(self, event_file='create_event.config'):
		self.event_file = event_file
	def create_misp_event(self):
		return self.create_event(self.make_conn(), self.read_event(self.event_file))

	__call__ = create_misp_event

	@staticmethod
	def make_conn():
		return misp_conn.MakeConn().get()

	@staticmethod
	def read_event(efile):
		config = configparser.ConfigParser()
		config.read(efile)
		return config


	@staticmethod
	def create_event(conn, efile):
		return conn.new_event(efile.get("event", "distrib"),efile.get("event", "info"), efile.get("event","analysis"), efile.get("event","threat"))
