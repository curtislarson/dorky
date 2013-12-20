from sources.source import Source
from dorks.searchterm import SearchTerm

class Pastebin(Source):
	def __init__(self):
		self.googleUrl = "https://www.google.com/search?q=site:pastebin.com";
		self.siteUrl = "http://www.pastebin.ca/search.php?s=Search&q="

	def executeDork(self, dork):
		print(dork)
		for term in dork.terms:
			print(term)