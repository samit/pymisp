#!/usr/bin/python3
from pymisp import PyMISP 
from misp_conn import MakeConn

_instance = None

__all__ = ['DwSuricata', "dw_suricata_event", "dw_suricata_all"]

def _get_instance():
	global _instance
	if _instance is None:
		_instance = DwSuricata()
	return _instance

def dw_suricata_event():
	return _get_instance.download_event()

def dw_suricata_all():
	return _get_instance.dwonload_all()


class DwSuricata(object):
	def __init__(self, evt="suricata.json"):
		self.evt = evt

	def download_event(self):
		return self.dw_evt(self.get_evt(self.evt))
	__call__ download_event

	@staticmethod

	def get_evt(evts):
		return evts

	@staticmethod

	def dw_evts(event):
		misp = MakeConn().get()
		return misp.download_suricata_rule_event(event)

	def download_all(self):
		return self.dw_all_event(self.MakeConn().get())
	__call__ = download_all

	@staticmethod
	def dw_all_event(misp):
		return misp.download_all_suricata()
