from sources.source import Source
from dorks.searchterm import SearchTerm

class GitHub(Source):
	def __init__(self):
		self.googleUrl = "https://www.google.com/search?q=site%3Agithub.com"
		self.siteUrl = "https://github.com/search?type=Code&q="

	def executeDork(self, dork):
		print(dork)
		for term in dork.terms:
			print(term)