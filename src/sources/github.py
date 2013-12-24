from sources.source import Source
from dorks.searchterm import SearchTerm

class GitHub(Source):
	def __init__(self):
		self.googleUrl = "https://www.google.com/search?q=site%3Agithub.com"
		self.siteUrl = "https://github.com/search?type=Code&q="
		super(GitHub, self).__init__()

	def executeDork(self, dork):
		print(dork)
		for term in dork.terms:
			self.executeGoogleDork(term.dork, term.ignores)

	def executeGoogleDork(self, dork, ignores):
		googleSearchUrl = self.getGoogleSearchUrl(self.googleUrl, dork, ignores)
		source = self.getSource(googleSearchUrl)
		print(source)