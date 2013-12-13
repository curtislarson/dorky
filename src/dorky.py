import getopt
import sys

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

def printUsage():
	print("dorky.py -t <type>")

if __name__ == '__main__':
	main(sys.argv[1:])