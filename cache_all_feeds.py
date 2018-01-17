from pymisp import PyMISP  
import misp_conn
_instance = None
__all__ = ['CacheAllFeeds','cache_all_feed']

def _get_instance():
	global _instance
	if _instance is None:
		_instance = CacheAllFeeds()
	return _instance

def cache_all_feed():
	return _get_instance.get()

class CacheAllFeeds(object):
	def __init__(self):
		self.__init__

	def get(self):
		return self.get_all_feeds()
	__call__ = get

	@staticmethod
	def get_all_feeds():
		misp = misp_conn.MakeConn().get()
		return misp.cache_all_feeds()
	