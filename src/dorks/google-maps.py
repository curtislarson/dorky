class GoogleMaps(Dork):

	ignores = ["API_KEY"]

	def __init__(self, type):
		dorks = ["https://maps.googleapis.com/maps/api/js?key="]
		terms = []
		for dork in dorks:
			term = SearchTerm(dork, ignores)
			terms.append(term)
		super.__init__(type, terms)