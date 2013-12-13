class Dork():

	def __init__(self, type, terms):
		self.type = type
		self.terms = terms


	class SearchTerm():
		def __init__(self, term, ignores):
			self.term = term
			self.ignores = ignores