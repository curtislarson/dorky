from sources.source import Source
from dorks.searchterm import SearchTerm

class GitHub(Source):
	def __init__(self):


	def executeDork(self, dork):
		for terms in dork.terms:
