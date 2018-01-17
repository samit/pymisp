#!/usr/bin/python3
from pymisp import PyMISP 
import misp_conn
import configparser

_instance = None
__all__ = ['FetchEventFeed', 'fetch_event_feed']

def _get_instance():
	global _instance
	if _instance is None:
		_instance = FetchEventFeed()
	return _instance

def fetch_event_feed():
	return _get_instance.fetch_event()

class FetchEventFeed(object):
	def __init__(self, feed_id='feed.config'):
		self.feed_id = feed_id
	def fetch_event(self):
		return self.feed_event(self.read_feed(self.feed_id))
	__call__ = fetch_event

	@staticmethod

	def read_feed(feeds):
		config = configparser.ConfigParser()
		config.read(feeds)
		return config

	@staticmethod
	def feed_event(events):
		misp = misp_conn.MakeConn().get()
		feed_id = events.get("fetch", "feedid")
		return misp.fetch_feed(feed_id)
