import abc
import urllib2

class Source(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def executeDork(self, dork):
		""" Execute the provided dork based on the current source"""
		return

	def getSource(self, url):
		page = urllib2.urlopen(url)
		return page.read()

	def getGoogleSearchUrl(self, googleUrl, dork, ignores):
		googleSearchUrl = googleUrl + " intext:\"" + dork + "\""
		for ignore in ignores:				
			googleSearchUrl += " -\"" + ignore + "\""
		return googleSearchUrl