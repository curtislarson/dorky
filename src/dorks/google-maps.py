class GoogleMaps(Dork):
	def __init__(self, type):
		dorks = ["https://maps.googleapis.com/maps/api/js?key="]
		super.__init__(type, dorks)