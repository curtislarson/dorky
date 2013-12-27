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
			self.executeGithubDork(term.dork, term.ignores)

	def executeGithubDork(self, dork, ignores):
		githubSearchUrl = self.siteUrl + dork
		source = self.getSource(githubSearchUrl)
		print(source)

	def executeGoogleDork(self, dork, ignores):
		googleSearchUrl = self.getGoogleSearchUrl(self.googleUrl, dork, ignores)
		source = self.getSource(googleSearchUrl)
		# String we are looking for
		# <h3 class="r"><a href="
		# end with double quotes