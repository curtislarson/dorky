from sources.source import Source
from dorks.searchterm import SearchTerm

class Pastebin(Source):
	def __init__(self):
		self.googleUrl = "https://www.google.com/search?q=site:pastebin.com";
		self.siteUrl = "http://www.pastebin.com/search.php?s=Search&q="
		super(Pastebin, self).__init__()

	def executeDork(self, dork):
		print(dork)
		for term in dork.terms:
			self.executeGoogleDork(term.dork, term.ignores)
			self.executePastebinDork(term.dork, term.ignores)

	def executePastebinDork(self, dork, ignores):
		# Looks like for pastebin you need a partner-pub query string
		# in order for the search to go through, for now we will hard code
		# it until I figure out how to get it programaticallt
		pastebinSearchUrl = self.siteUrl + dork + "&cx=partner-pub-7089230323117142%3A2864958357&cof=FORID%3A10&ie=UTF-8"
		source = self.getSource(pastebinSearchUrl)
		print(source)

	def executeGoogleDork(self, dork, ignores):
		googleSearchUrl = self.getGoogleSearchUrl(self.googleUrl, dork, ignores)
		source = self.getSource(googleSearchUrl)
		print(source)