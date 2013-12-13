from dorks.dork import Dork
from dorks.searchterm import SearchTerm

class GoogleMaps(Dork):

	ignores = ["API_KEY"]

	def __init__(self, type):
		dorks = ["https://maps.googleapis.com/maps/api/js?key="]
		terms = []
		for dork in dorks:
			term = SearchTerm(dork, GoogleMaps.ignores)
			terms.append(term)
		super(GoogleMaps, self).__init__(type, terms)