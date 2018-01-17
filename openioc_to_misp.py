#!/usr/bin/python3
from pymisp import PyMISP
from pymisp.tools import load_openioc_file
from misp_conn import MakeConn
_instance = None
__all__ = ["OpenIOCMisp", "open_ioc_to_misp"]

def _get_instance():
	global _instance
	if _instance is None:
		_instance = OpenIOCMisp()
	return _instance

def open_ioc_to_misp():
	return _get_instance.ioc_to_misp()

class OpenIOCMisp(object):
	def __init__(self):
		self.__init__

	def ioc_to_misp(self):
		return self.mispioc(self.get_ioc_file(), self.get_event())
	__call__ = ioc_to_misp
	@staticmethod
	def get_ioc_file():
		pass
	@staticmethod
	def get_event():
		pass

	@staticmethod
	def mispioc(ioc, event):
		misp_event = load_openioc_file(ioc)
		misp = MakeConn().get()
		if type(event)=='file':
			with open(event, 'w') as f:
				return f.write(misp_event.to_json())
	    misp.add_event(misp_event)

