from Filtering import myfilter
import numpy as np
def dataCleaner(ecgd):

	time = sinterp(ecgd[0])
	volt = sinterp(ecgd[1])

	volt = ranger(volt)

	ecgd = [time, volt]

	time, fvolt = myfilter(ecgd)

def typeCorrection(arry):

	for j,each in arry:
		


def ranger(volt):

	for j,each in volt:
		if each >= 300:
			volt[j] = 299
	return volt

def sinterp(time):
	
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
			#print(myint)
			print('k=',k , '  j=',j)
			while(True):
				
				if k >= j-1:
					break
				else:
					time[k+1] = float(time[k]) + float(myint)
					print(time[k+1])
					k = k + 1
		i = i + 1		
	return time


if __name__ == "__main__":
    myarr = np.array([-999, 1, -999, -999, 5, 7, -999, 15 , -999])

    t = sinterp(myarr)
    print(t)