from peakalgorithm import detect_peaks
from Datacollector import collector
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=RuntimeWarning)


#  This function peakfinder opens the csv file by user selection. Defaults to test data1
#  uses a peak detection algorithm
#  From MIT. The values returned in myindices are the indices of peaks in the time array.
#  Returns 1 array This function is tested by setting the show = True and visually inspecting
def peakfinder(vd):
    """This function calls the peak finder Algorithm used within rights from MIT.

    Args:
        vd: Numpy array of voltages.

    Returns:
        Array of indices that peaks occurred at within 'vd'.

    Raises:
        TypeError: If the array is empty or if 'vd' is an int or str or NaN another type is not possible.

    """
    if len(vd) == 0 or isinstance(vd, int) or isinstance(vd, str):
        raise TypeError("Error: Array Passed into peakfinder was Empty or not an Array")
    myindices = detect_peaks(vd, mph=0.19, mpd=260, show=False)

    return myindices


#  The timefinder function returns all the times that a peak occured by using the
#  arrray of peak indices. Returns an array. Only simple test is used because this is a straightforward function
def timefinder(mytime, myindex):
    """Finds the times that peaks occurred at by adding times to array

    Args:
        mytime: Numpy array of all of the time data.
        myindex: Array of indices where peaks occurred at.

    Returns:
        An array of times at which peaks occurred still in order of occurrence.

        Raises:
            TypeError: If the array is empty or if 'mytime' or 'myindex' is an int or str or NaN.
    """
    if len(mytime) == 0 or isinstance(mytime, int) or isinstance(mytime, str):
        raise TypeError("Error: Array Passed into timefinder was Empty or not an Array")
    if len(myindex) == 0 or isinstance(myindex, int) or isinstance(myindex, str):
        raise TypeError("Error: Array Passed into timefinder was Empty or not an Array")
    if len(myindex) > len(mytime):
        raise ValueError("Error: There are too many values within the array that contains indices of beats")
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
    """Returns average hr based on interval of user input.

    Args:
        dur: Total duration that time data encompasses.
        tarr: Array of times at which peaks occurred.

    Returns:
        Si

    Raises:
        TypeError: If the values passed in for 'dur' and 'tarr' were empty or not valid types.

    """
    if isinstance(dur, str) or np.isnan(dur):
        raise TypeError("Error: Value Passed into avghr was Empty or not the correct Type.")
    if len(tarr) == 0 or isinstance(tarr, int) or isinstance(tarr, str):
        raise TypeError("Error: Array Passed into avghr was Empty or not an array.")
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
    """Takes in unprocessed data array of time and outputs the duration.

    Args:
        tarr: Array of times for all data in the loaded csv file.

    Returns:
        dur as a numpy.float64.

    Raises:
        TypeError: When the array is empty or is not an array.
    """
    if len(tarr) == 0 or isinstance(tarr, int) or isinstance(tarr, str):
        raise TypeError("Error: Array Passed into durr was Empty or not an array.")
    f = len(tarr) - 1

    dur = tarr[f] - tarr[0]

    return dur


# findex finds the extreme voltages of the data. Takes in voltage array
#  Returns a min and a max as comma separated
def findex(volt):
    """Takes in array of voltages and outputs min and max.

    Args:
        volt: Array of voltages.

    Returns:
        Two numpy floats separated by a comma.

    Raises:
        TypeError: When the array is empty or is not an array.
    """
    if len(volt) == 0 or isinstance(volt, int) or isinstance(volt, str):
        raise TypeError("Error: Array Passed into findex was Empty or not an array.")
    mmax = np.max(volt)
    mmin = np.min(volt)

    return mmax, mmin


# numbeats takes in array of beat indices and find the length to get the total beats
# Returns a single value as a np.array. So simple doesn't really need significant testing.
def numbeats(beatindex):
    """Takes the length of array of beat indices to find total beats.

    Args:
        beatindex: Array of beat indices.

    Returns:
        An integer representing the number of beats that occurred.
    """
    if len(beatindex) == 0 or isinstance(beatindex, int) or isinstance(beatindex, str):
        raise TypeError("Error: Array Passed into beatindex was Empty or not an array.")
    mynum = len(beatindex)

    return mynum


if __name__ == '__main__':
    mytime = [1, 2, 3, 4]
    myd = 4
    print(avghr(myd, mytime))

