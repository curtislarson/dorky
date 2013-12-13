class MySql(Dork):

	ignores = ["localhost"]

	def __init__(self, type):
		dorks = ["mysql_connect",
				 "mysqli_connect",
				 "mysql_select_db",
				 "mysqli_select_db"]
		terms = []
		for dork in dorks:
			term = SearchTerm(dork, ignores)
			terms.append(term)
		super.__init__(type, terms)
