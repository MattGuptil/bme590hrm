from newindice import *
from sinterp import datacleaner
from makeJson import makej
from Datacollector import collector

#  This function runs all of my functions and outputs to a JSON file
#  This script allows the user to select the file to examine and
#  the interval for average heart rate.
if __name__ == '__main__':
    """This is main running function that combines all the functions and utilizes them for their potential."""
    ecgd, fname = collector()
    ttime, vd = datacleaner(ecgd)

    myindices = peakfinder(vd)
    mydur = durr(ttime)
    myextr = findex(vd)
    mynumbeats = numbeats(myindices)
    timeindex = timefinder(ttime, myindices)
    myavghr = avghr(mydur, timeindex)

    metrics = {"mean_hr_bpm": myavghr,
               "voltage_extremes": myextr,
               "duration": mydur,
               "num_beats": mynumbeats,
               "beats": timeindex
               }
    makej(metrics, fname)

    print("Your Output Data File Has Been Created. Please Come Again")
