#!/usr/bin/python3
from pymisp import  PyMISP 
from misp_conn import MakeConn
_instance = None
__all__ = ['GetMispAttr', 'get_attr_stat', 'get_attr_stat_with_context']

def _get_instance():
	global _instance
	if _instance is None:
		_instance = GetMispAttr()
	return _instance

def get_attr_stat():
	return _get_instance.get()
def get_attr_stat_with_context():
	return _get_instance.get_context()

class GetMispAttr(object):
	"""Get attributes statistics from the MISP instance """
	def __init__(Self):
		self.__init__

	def get(self):
		return self.get_misp_instance_attr()
	__call__ = get_misp_instance_attr

	@staticmethod
	def get_misp_instance_attr():
		misp = MakeConn().get()
		return misp.get_attributes_statistics(misp, percentage=True)
		
	def get_context(self):
		return self.self.get_attr_stat_with_ctxt()
	__call__ = get_attr_stat_with_ctxt
    
    @staticmethod
	def get_attr_stat_with_ctxt():
		misp = MakeConn().get()
		return misp.get_attributes_statistics(context='category', percentage=True)
