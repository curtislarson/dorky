import getopt
import sys

from dorks.gmaps import GoogleMaps
from dorks.mysql import MySql
from dorks.amazon import Amazon

def main(argv):
	type = ''
	sourceType = ''
	try:
		opts,args = getopt.getopt(argv, "t:s:h:", ["type=","source=", "help"])
	except getopt.GetoptError:
		printUsage()
		sys.exit(2)
	for opt,arg in opts:
		if opt == "-h":
			printUsage()
			sys.exit()
		elif opt in ("-t","--type"):
			type = arg
		elif opt in ("-s", "--source"):
			source = arg
	beginSearch(type.lower(), sourceType.lower())

def beginSearch(type, sourceType):
	dorks = []
	if type == 'all':
		dorks = getDorks()
	else:
		dorks.insert(0, getDork(type))
	sources = []
	if sourceType == 'all':
		sources = getSources()
	else:
		sources.insert(0, getSource(sourceType))

def getDork(type):
	dork = 0
	if type == 'googlemaps':
		dork = GoogleMaps(type)
	elif type == 'mysql':
		dork = MySql(type)
	elif type == 'amazon':
		dork = Amazon(type)
	else:
		dork = 0
	return dork

def getDorks():
	dorks = []
	dorks.insert(0, getDork('googlemaps'))
	dorks.insert(0, getDork('mysql'))
	dorks.insert(0, getDork('amazon'))
	return dorks

def getSource(type):
	source = 0
	if type == 'github':
		source = Github()
	elif type == 'pastebin':
		source = Pastebin()
	else:
		source = 0
	return source

def getSources():
	sources = []
	sources.insert(0, getSource('github'))
	sources.insert(0, getSource('pastebin'))
	return sources

def printUsage():
	print("dorky.py -t <type>")

if __name__ == '__main__':
	main(sys.argv[1:])