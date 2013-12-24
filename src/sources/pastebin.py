from sources.source import Source
from dorks.searchterm import SearchTerm

class Pastebin(Source):
	def __init__(self):
		self.googleUrl = "https://www.google.com/search?q=site:pastebin.com";
		self.siteUrl = "http://www.pastebin.ca/search.php?s=Search&q="
		super(Pastebin, self).__init__()

	def executeDork(self, dork):
		print(dork)
		for term in dork.terms:
			self.executeGoogleDork(term.dork, term.ignores)

	def executeGoogleDork(self, dork, ignores):
		googleSearchUrl = self.getGoogleSearchUrl(self.googleUrl, dork, ignores)
		source = self.getSource(googleSearchUrl)
		print(source)