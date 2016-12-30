import argparse

def get_args():
	parse=argparse.ArgumentParser(
		description="simple arguments parser",
		epilog="This is where you might put example usage")

	parse.add_argument('-x', action="store", require=True, help='Help text for option X')
	parse.add_argument('-y', help='Help text for option Y', default= False)
	parse.add_argument('-z', help='Help text for option Z', type=int)

	print (parse.parse_args())

if __name__=='__main__':
	get_args()