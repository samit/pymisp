#!/usr/bin/python
from pymisp import PyMISP 
import misp_conn
import os 
_instance = None

__all__ = ['MispSearch', 'search_one', 'search_all']

def _get_instance():
	global _instance
	if _instance is None:
		_instance = MispSearch()
	return _instance

def search_one():
	return _get_instance.search_for_one()

def search_all():
	return _get_instance.search_for_all()

class MispSearch(object):
	def __init__(self, search_param='search.json'):
		self.search_param = search_param

	def search_for_one(self):
		return self.search_params(self.get_search_item(self.search_param))
	__call__ = search_for_one

	@staticmethod 
	def get_search_item(s_param):
		if s_param['output'] is not None and os.path.exists(s_param['output']):
			print ("Output file already exists aborting ......!")
			exit(0)
		return s_param

	@staticmethod
	def search_params(json_data):
		if json_data['attributes']:
			controller = 'attributes'
		else:
			controller = 'events'
		misp = misp_conn.MakeConn().get()
		kwargs = {json_data['param']:json_data['search']}
		result = misp.search(controller, **kwargs)
		if json_data['quiet']:
			for e in result['response']:
				return '{}{}{}\n'.format(url, '/events/view/', e['Event']['id'])
		elif out is None:
			return json.dumps(result['response'])
		else:
			with open(json_data['output'],'w') as search_res:
				search_res.write(json.dumps(result['response']))

	def search_for_all(self):
		return self.search_all(self.get_search_item(self.search_param))
	__call__ = search_for_all

	@staticmethod
	def search_all(s_item):
		misp = misp_conn.MakeConn().get()
		result = misp.search_all(s_item['search'])
		if json_data['quiet']:
			for e in result['response']:
				return '{}{}{}\n'.format(url, '/events/view/', e['Event']['id'])
		elif out is None:
			return json.dumps(result['response'])
		else:
			with open(s_item['output'],'w') as search_res:
				search_res.write(json.dumps(result['response']))













