from dorks.dork import Dork
from dorks.searchterm import SearchTerm

class MySql(Dork):

	ignores = ["localhost"]

	def __init__(self, type):
		dorks = ["mysql_connect",
				 "mysqli_connect",
				 "mysql_select_db",
				 "mysqli_select_db"]
		terms = []
		for dork in dorks:
			term = SearchTerm(dork, MySql.ignores)
			terms.append(term)
		super(MySql, self).__init__(type, terms)
