from dorks.dork import Dork
from dorks.searchterm import SearchTerm

class Rsa(Dork):

	ignores = []

	def __init__(self, type):
		dorks = ["-----BEGIN RSA PRIVATE KEY-----"
				 "-----END RSA PRIVATE KEY-----"]
		terms = []
		for dork in dorks:
			term = SearchTerm(dork, Rsa.ignores)
			terms.append(term)
		super(Rsa, self).__init__(type, terms)
