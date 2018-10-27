from Filtering import myfilter
import numpy as np


#  Takes in arrays and performs linear interpolation, checks range boundaries, and outputs filtered data
#  Can't test this as it is made up of tested functions so output will always be as expected when other functions pass
#  As long as functions check for exceptions
def dataCleaner(ecgd):

	time = sinterp(ecgd[0])
	volt = sinterp(ecgd[1])

	volt = ranger(volt)

	ecgd = [time, volt]

	time, fvolt = myfilter(ecgd)

	return time, fvolt


#  Goes through entire array to see if there is a boundary violation, fixes those issues
# . Inputs an array, Outputs fixed array
#  Checks to make sure that an iterable object was passed into it
def ranger(volt):

	if isinstance(volt, str) or isinstance(volt, int) or volt == '':
		raise TypeError("ERROR: Input was not a proper iterable, ")

	for j, each in enumerate(volt):
		if each >= 300:
			volt[j] = 299
		if each <= -300:
			volt[j] = -299
	return volt


# Performs my own custom linear interpolation on datasets when they are missing values
# Outputs fixed array/dataset
def sinterp1(time):
	
	i = 0
	j = 0
	k = 0
	t = len(time) - 1

	while(True):
		count = 3

		if time[t] == -999 or time[0] == -999:
			time[t] = 0

		if i >= t:
			break

		if time[i] == -999:

			j = i
			while(True):

				if time[j+1] == -999:

					j = j +1
					count = count + 1
				else:
					j = j+1
					break

			myint = float((time[j] -time[i-1])) / float(count)
			k = i-1

			while(True):
				
				if k >= j-1:
					break
				else:
					time[k+1] = float(time[k]) + float(myint)

					k = k + 1
		i = i + 1		
	return time


if __name__ == "__main__":
	myarr = np.array([-999, 1, -999, -999, 5, 7, -999, 15 , -999])
	t = sinterp1(myarr)
	print(t)
