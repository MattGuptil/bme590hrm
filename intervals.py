import numpy as np
def intervs(qrstime,qrsindex):
	i = 0
	n = 0
	while(True):
		if(i+1 >= len(qrsindex)):
			break

		myst = qrsindex[i]
		myne = qrsindex[i+1]
		#print(qrstime[myne] - qrstime[myst])
		if(qrstime[myne] - qrstime[myst] <= .075):
			
			qrsindex = np.delete(qrsindex, i+1, 0)
			
		else:
			i = i + 1
		n = n+1
	return qrsindex


if __name__ == '__main__':
	re = intervs(np.array([0,1,1.01,2,3,3.01]),np.array([0,1,2,3,4,5]))
	myy = np.array([0,1,3,4])
	np.testing.assert_array_equal(re,myy, 'SIKE')






