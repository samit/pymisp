#!/usr/bin/python3
from pymisp import PyMISP  
import misp_conn
import configparser

_instance = None
__all__ = ["AddEventAttr", "add_event_attr"]
def _get_instance():
	global _instance
	if _instance is None:
		_instance = AddEventAttr()
	return _instance

def add_event_attr():
	return _get_instance.add()

class AddEventAttr(object):
	def __init__(self, attrs='event_attr.config'):
		self.attrs = attrs

	def add(self):
		return self.add_attr(self.read_attr(self.attrs))
	__call__ = add

	@staticmethod

	def read_attr(attrdata):
		config = configparser.ConfigParser()
		config.read(attrdata)
		return config
		
	@staticmethod
	def add_attr(evattr):
		misp = misp_conn.MakeConn().get()
		past_event = misp.get_event(evattr.get("attr","event"))
		new_event = misp.add_named_attribute(past_event,evattr.get("attr","type"),evattr.get("attr","value") )

