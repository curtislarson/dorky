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
	dork = getDork(type)
	source = getSource(sourceType)

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

def getSource(type):
	source = 0
	if type == 'github':
		source = Github()
	elif type == 'pastebin':
		source = Pastebin()
	else:
		source = 0
	return source

def printUsage():
	print("dorky.py -t <type>")

if __name__ == '__main__':
	main(sys.argv[1:])