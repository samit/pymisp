#!/usr/bin/python3
from pymisp import PyMISP
import misp_conn
import configparser
import json 
from six import string_types



_instance=None
__all__ = ['AddUser', 'create_user', 'list_user', 'delete_user', 'update_user']
def _get_instance():
	global _instance
	if _instance is None:
		_instance = AddUser
	return _instance

def create_user():
	return _get_instance.create_misp_user()

def list_user():
	return _get_instance.list_misp_user()

def delete_user():
	return _get_instance.del_misp_user()

def update_user():
	return _get_instance.update_misp_user()

class AddUser(object):
	def __init__(self, user_data='user.json'):
		"""Init method to get credentials """
		self.user_data = user_data

	def create_misp_user(self):
		""""Create user on your MISP Server  """
		return self.create_muser(self.connect_misp(), self.get_user(self.user_data))
	__call__ = create_misp_user

	@staticmethod
	def get_user(user_json):
		"""Reads the JSON data for user  """
		with open(user_json) as json_data:
			user_array = json.load(json_data)
		return user_array


	
	@staticmethod
	def connect_misp():

		return misp_conn.MakeConn().get()



	@staticmethod
	def create_muser(misp, user_data):
		"""Actual method that calls the MISP endpoint API  """

		for user in user_data:
			try:
				misp.add_user(user['email'], user['org_id'], user['role_id'])
			except Exception as e:
				print (e)

	def list_misp_user(self):
		return self.list_muser(self.connect_misp())
	__call__ = list_misp_user

	@staticmethod
	def list_muser(misp):
		return misp.get_users_list()

	def del_misp_user(self):
		return self.del_muser(self.connect_misp())

	__call__ = del_misp_user

	@staticmethod
	def del_muser(auth):
		return auth.delete_user('8')

	def update_misp_user(self):
		return self.update_muser(self.connect_misp())

	__call__ = update_misp_user

	@staticmethod
	def update_muser(auth):
		params = {"email":"abc@logpoint.com"}
		return auth.edit_user('2', email=params['email'])
		






			
