#!/usr/bin/python3
from pymisp import PyMISP 
from misp_conn import MakeConn
_instance = None
__all__ = ["GetAllTags", "get_tag_instance"]

def _get_instance():
	global _instance
	if _instance is None:
		_instance = GetAllTags()
	return _instance

def get_tag_instance():
	return _get_instance().get_tag()


class GetAllTags(object):
	"""Get all the tags used on the instance """
	def __init__(self):
		self.__init__

	def get_tag(Self):
		return self.get_all_tag_used(self.MakeConn().get())
	__call__ = get_tag

	@staticmethod
	def get_all_tag_used(misp):
		return misp.get_all_tags(True)
	

