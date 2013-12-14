from sources.source import Source
from dorks.searchterm import SearchTerm

class Pastebin(Source):
	def __init__(self):
		self.googleUrl = "https://www.google.com/search?q=site:pastebin.com";

	def executeDork(self, dork):
		for terms in dork.terms:
			

		
