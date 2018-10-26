import json

def makeJ(mydir, fname):

	fname = fname.strip('.csv')
	fname = fname + '.json'
	with open(fname, 'w') as fp:
		json.dump(mydir,fp)

	return

if __name__ == '__main__':

	fname = 'myTEST.csv'
	mydir = {"key1": 'WOW',
				"key2": 'GEEZE'}

	makeJ(mydir, fname)