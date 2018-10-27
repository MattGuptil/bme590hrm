from newindice import *
from makeJson import makej


#  This function runs all of my functions and outputs to a JSON file
#  This script allows the user to select the file to examine and
#  the interval for average heart rate.
if __name__ == '__main__':
    #  Add filtering to peakfinder function or incorporate new one
    ecgd, fname = collector()
    ttime = ecgd[0]
    vd = ecgd[1]

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
