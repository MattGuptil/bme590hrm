from peakalgorithm import detect_peaks
from Datacollector import collector
import numpy as np


#  This function peakfinder opens the csv file by user selection. Defaults to test data1
#  uses a peak detection algorithm
#  From MIT. The values returned in myindices are the indices of peaks in the time array.
#  Returns 1 array This function is tested by setting the show = True and visually inspecting
def peakfinder(vd):
    myindices = detect_peaks(vd, mph=0, show=False)

    return myindices


#  The timefinder function returns all the times that a peak occured by using the
#  arrray of peak indices. Returns an array. Only simple test is used because this is a straightforward function
def timefinder(mytime, myindex):
    newtime = []
    for each in myindex:
        newtime.append(mytime[each])

    return newtime


#  avghr Allows the user to select and Avg HR interval based in seconds and requires
#  it to be in the range of the data. If not in range it throws a value error
#  To calculate intervals it looks at the distance between elements and waits until
#  the interval is matched or exceeded. It then takes the number of beats found in the
#  interval and outputs all the beats found in that interval into an array
#  resulting in array of beats per interval. This is then converted to beats/sec ->
#  beats/min and then the array is averaged to find the overall average.
#  This returns one value of Avg BPM, technically it is still a np.array
#  It takes in an array of times that beats occurred at
def avghr(dur, tarr):
    print("Max Input is", dur, "s")
    tint = input("Enter Avg HR Interval in secs:")
    tint = int(tint)

    if tint > dur or tint < 0:
        raise ValueError("You entered a value not in range. Try again.")

    i = 0
    j = 1

    mylen = len(tarr)
    beats = []

    while True:
        if j >= mylen:

            break

        if tarr[j] - tarr[i] >= tint or j == mylen - 1:

            beats = np.append(beats, j - i)

            i = j
            j = i + 1
        else:
            j = j + 1

    bps = np.true_divide(beats, tint)  # might need to add beats to input here

    bpm = bps * 60
    avgbpm = np.mean(bpm)

    return avgbpm


#  durr find the total duration of the data. It must take in the full array of times
#  Not the array with the times of peaks! Return a single value
def durr(tarr):
    f = len(tarr) - 1

    dur = tarr[f] - tarr[0]

    return dur


# findex finds the extreme voltages of the data. Takes in voltage array
#  Returns a min and a max as comma separated
def findex(volt):
    mmax = np.max(volt)
    mmin = np.min(volt)

    return mmax, mmin


# numbeats takes in array of beat indices and find the length to get the total beats
# Returns a single value as a np.array. So simple doesn't really need significant testing.
def numbeats(beatindex):
    mynum = len(beatindex)

    return mynum


if __name__ == '__main__':
    mytime = [1, 2, 3, 4]
    myd = 4
    print(avghr(myd, mytime))

