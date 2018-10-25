from peakalgorithm import detect_peaks
from Datacollector import collector
import numpy as np

def peakfinder():
	

	ecgd = collector()
	time = ecgd[0]
	vd = ecgd[1]
	
	myindices = detect_peaks(vd,mph = 0, show =False)

	return(time,myindices)


def timefinder(mytime,myindex):
	newtime = mytime[myindex]
	return newtime


def avghr(dur,tarr):
	print("Max Input is", dur, "s")
	tint = input("Enter Avg HR Interval in secs:")
	tint = int(tint)

	if tint > dur or tint < 0:
		raise ValueError("You entered a value not in range. Try again.")

		i = 0
		j = 1
		k = 0
		mylen = len(tarr)

	while(True):
		if j >= mylen:
			break
		if tarr[j]-tarr[i] >= tint:
			beats[k] = 1+ j-i
			k = k+1
			i = j
			j = i +1
		else:
			j = j+1


	return beats

def durr(tarr):
	f = len(tarr) -1

	dur = tarr[f]-tarr[0]

	return dur


if __name__ == '__main__':
	a,b = peakfinder()

	c = timefinder(a,b)
	mydur = durr(a)
	avghr(mydur,c)