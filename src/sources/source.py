import abc
import urllib2
import urllib

class Source(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def executeDork(self, dork):
		""" Execute the provided dork based on the current source"""
		return

	def getSource(self, url):
		user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
		headers = {'User-Agent' : user_agent}
		request = urllib2.Request(url, None, headers)
		response = urllib2.urlopen(request)
		return response.read()

	def getGoogleSearchUrl(self, googleUrl, dork, ignores):
		googleSearchUrl = googleUrl + urllib.quote(" intext:\"" + dork + "\"")
		for ignore in ignores:				
			googleSearchUrl += urllib.quote(" -\"" + ignore + "\"")
		return googleSearchUrl