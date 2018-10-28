from Filtering import myfilter
import numpy as np
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=RuntimeWarning)


#  Takes in arrays and performs linear interpolation, checks range boundaries, and outputs filtered data
#  Can't test this as it is made up of tested functions so output will always be as expected when other functions pass
#  As long as functions check for exceptions
def datacleaner(ecgd):
    """This function gives us filtered and interpolated data.

    Args:
        ecgd: Array of ecgd data array contains two numpy arrays of time and voltage.

    Returns:
        Two numpy array separated by commas of the cleaned data.

    Raises:
        TypeError: If 'ecgd' is empty or isn't the correct type.
    """
    if len(ecgd) == 0 or isinstance(ecgd, str) or isinstance(ecgd, int):
        raise TypeError("ERROR: Input was not a proper iterable, ")
    time = sinterp1(ecgd[0])
    volt = sinterp1(ecgd[1])

    ecgd = [time, volt]

    time, volt = myfilter(ecgd)

    volt = ranger(volt)

    return time, volt


#  Goes through entire array to see if there is a boundary violation, fixes those issues
# . Inputs an array, Outputs fixed array
#  Checks to make sure that an iterable object was passed into it
def ranger(volt):
    """Finds value out of range and changes them to be within range.

    Args:
        volt: Numpy array of voltages.

    Returns:
        Numpy array of fixed voltages.

    Raises:
        TypeError: If 'volt' empty or not the correct data type.
    """
    if len(volt) == 0 or isinstance(volt, str) or isinstance(volt, int):
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
    """Takes in a array or numpy array and fills in missing data through interpolation.

    Args:
        time: Numpy array or simple array of values taken from csv file possible missing data.

    Returns:
        Interpolated numpy array that doesn't have any missing data points.

    Raises:
        TypeError: If 'time' is empty or is not the correct type
    """
    if len(time) == 0 or isinstance(time, str) or isinstance(time, int):
        raise TypeError("ERROR: Input was not a proper iterable, ")
    i = 0
    j = 0
    k = 0
    t = len(time) - 1

    while (True):
        count = 3

        if time[t] == -999 or time[0] == -999:
            time[t] = 0

        if i >= t:
            break

        if time[i] == -999 or np.isnan(time[i]):

            j = i
            while (True):

                if time[j + 1] == -999:

                    j = j + 1
                    count = count + 1
                else:
                    j = j + 1
                    break

            myint = float((time[j] - time[i - 1])) / float(count)
            k = i - 1

            while (True):

                if k >= j - 1:
                    break
                else:
                    time[k + 1] = float(time[k]) + float(myint)

                    k = k + 1
        i = i + 1
    return time


if __name__ == "__main__":
    myarr = np.array([-999, 1, -999, -999, 5, 7, -999, 15, -999])
    t = sinterp1(myarr)
    print(t)
