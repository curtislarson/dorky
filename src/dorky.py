import getopt
import sys

from dorks.gmaps import GoogleMaps
from dorks.mysql import MySql

def main(argv):
	type = ''
	try:
		opts,args = getopt.getopt(argv, "t:h:", ["type=", "help"])
	except getopt.GetoptError:
		printUsage()
		sys.exit(2)
	for opt,arg in opts:
		if opt == "-h":
			printUsage()
			sys.exit()
		elif opt in ("-t","--type"):
			type = arg
	beginSearch(type)

def beginSearch(type):
	dork = 0
	if type == 'GoogleMaps':
		dork = GoogleMaps(type)
	elif type == 'Mysql':
		dork = MySql(type)
	else:
		dork = 0
	print(dork)

def printUsage():
	print("dorky.py -t <type>")

if __name__ == '__main__':
	main(sys.argv[1:])