class MySql(Dork):
	def __init__(self, type):
		dorks = ["mysql_connect",
				 "mysqli_connect",
				 "mysql_select_db",
				 "mysqli_select_db"]
		super.__init__(type, dorks)
