import abc
import urllib2

class Source():
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def executeDork(self, dork):
		""" Execute the provided dork based on the current source"""
		return

	def getSource(url):
		page = urllib2.urlopen(url)
		return page.read()