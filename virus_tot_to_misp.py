#!/usr/bin/python3
import pymisp
from pymisp.tools import VTReportObject 
import json
import logging
import datetime
from misp_conn import MakeConn
from urllib.parse import urlsplit

_instance = None

__all__ = ['VtrToMisp', 'vtr_msip_obj']

def _get_instance():
	global _instance
	if _instance is None:
		_instance = VtrToMisp()
	return _instance

def vte_misp_obj():
	return _get_instance.get_vtr_misp()

class VtrToMisp(object):
	def __init__(self, vtr_file='virus_total.json'):
		self.vtr_file = vtr_file

	def get_vtr_misp(self):
		return self.vtr_to_misp(self.virus_total_obj(self.read_vt(self.vtr_file), self.get_indicators()), self.get_misp_event(self.eventid=None, self.info=None))
	__call__ = vtr_to_misp

	@staticmethod
	def read_vt(vtjson):
		with open(vtjson) as vtotal:
			api_key = json.dump(vtotal)
		return api_key
	@staticmethod
	def get_indicators():
		pass

	@staticmethod
	def virus_total_obj(api_key, indicators):
		'''Build our VirusTotal report object, File object, and AV signature objects
		   and link them appropriately.
		   indicator: Indicator hash to search in VT for

		'''
		vtr_report = VTReportObject(api_key["virustotal"]["key"], indicators)
		report_objects = []
		report_objects.append(vtr_report)
		av_report = vtr_report._report
		if vtr_report._resource_type == 'file':
			file_object = pymisp.MISPObject(name="file")
			file_object.add_attribute("md5", value=raw_report["md5"])
			file_object.add_attribute("sha1", value=raw_report["sha1"])
			file_object.add_attribute("sha256", value=raw_report["sha256"])
			vtr_report.add_reference(referenced_uuid=file_object.uuid, relationship_type="report of")
			report_objects.append(file_object)
		elif vtr_report._resource_type == "url":
			parsed = urlsplit(indicator)
			url_object = pymisp.MISPObject(name="url")
			url_object.add_attribute("url", value=parsed.geturl())
			url_object.add_attribute("host", value=parsed.hostname)
			url_object.add_attribute("scheme", value=parsed.scheme)
			url_object.add_attribute("port", value=parsed.port)
			vtr_report.add_reference(referenced_uuid=url_object.uuid, relationship_type="report of")
			report_objects.append(url_object)
		for antivirus in av_report["scans"]:
			if av_report["scans"][antivirus]["detected"]:
				av_object = pymisp.MISPObject(name="av-signature")
				av_object.add_attribute("software", value=antivirus)
				signature_name = raw_report["scans"][antivirus]["result"]
				av_object.add_attribute("signature", value=signature_name, disable_correlation=True)
				vtr_report.add_reference(referenced_uuid=av_object.uuid, relationship_type="included-in")
				report_objects.append(av_object)
	    return report_objects
	@staticmethod
	def get_misp_event(eventid, info):
		eventid=1#The event id of the MISP event to upload objects to
		#info="The event's title"
		misp = MakeConn().get()
		if eventid:
			event = misp.get_event(eventid)
		elif info:
			event = misp.new_event(info=info)
		else:
			event = misp.new_event(info="VirusTotal Report")
		misp_event = pymisp.MISPEvent()
		misp_event.load(event)
		return misp_event


	@staticmethod
	def vtr_to_misp(misp_obj, misp_event):
		misp = MakeConn().get()
		for obj in misp_obj:
			template_id = misp.get_object_template_id(obj.template_uuid)
			misp.add_object(misp_event.id, template_id, obj)
		for mobject in misp_obj:
			for reference in mobject.ObjectReference:
				misp.add_object_reference(reference)
	
		








