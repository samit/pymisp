#!/usr/bin/python3
from pymisp import PyMISP 
from misp_conn import MakeConn

_instance = None

__all__ = ['FileUploader', 'upload_file']

def _get_instance():
	global _instance
	if _instance is None:
		_instance = FileUploader()
	return _instance
def upload_file():
	return _get_instance.upload_fsample()

class FileUploader(object):
	def __init__(self, file_up='upload_sample.json'):
		self.file_up = file_up

	def upload_fsample(self):
		return self.upload(self.file_up)
	__call__ = upload_fsample

	@staticmethod
	def upload(ufile):
		misp = MakeConn().get()
		return misp.upload_samplelist(ufile["filepaths"]
			ufile["event_id"]
			ufile["distribution"]
			ufile["to_ids"]
			ufile["category"]
			ufile["comment"]
			ufile["info"]
			ufile["analysis"]
			ufile["threat_level_id"]
			)
	