#!/usr/bin/python3
from pymisp import PyMISP 
import misp_conn
import os 
_instance = None
__all__ = ['NetFlowNetAct','net_flow_filevent', 'net_flow_filevntFile','net_oput_comm']
def _get_instance():
	global _instance
	if _instance is None:
		_instance = NetFlowNetAct()
	return _instance

def net_flow_filevent():
	return _get_instance.filter_eventid()

def net_flow_filevntFile():
	return _get_instance.filter_eventfile()

def net_oput_comm():
	return _get_instance.output_with_comments()

class NetFlowNetAct(object):
	def __init__(self, net_json='network.json'):
		self.net_json = net_json
	
	def filter_eventid(self):
		return self.filter_event_id(self.get_event(self.get_event_id()))
	__call__ = filter_eventid


	@staticmethod
	def get_event_id():
		event_id = 1234
		return event_id

	@staticmethod
	def read(net_file):
		with open(net_file) as netfile:
			array = json.dump(netfile)
		return array

	@staticmethod
	def get_event(eids):
		if eids >0:
			misp = misp_conn.MakeConn().get()
			json_event = misp.get_event(eids)
			return json_event
			

    @staticmethod
    def filter_event_id(json_event):
    	pass

    def filter_eventfile(self):
    	return self.filter_evt_file(self.get_event_fid())
    __call__ = filter_eventfile

    @staticmethod
    def get_event_fid():
    	pass
    @staticmethod
    def filter_evt_file(elist):
    	pass
    def output_with_comments():
    	return self.commented_output()
    __call__ = output_with_comments

    @staticmethod
    def commented_output():
    	pass




    



