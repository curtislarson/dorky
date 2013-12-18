from dorks.dork import Dork
from dorks.searchterm import SearchTerm

class Amazon(Dork):

	ignores = ["role/test"]

	def __init__(self, type):
		dorks = ["roleArn", "arn:aws:iam"]
		terms = []
		for dork in dorks:
			term = SearchTerm(dork, Amazon.ignores)
			terms.append(term)
		super(Amazon, self).__init__(type, terms)