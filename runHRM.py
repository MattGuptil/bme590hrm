from newindice import *
from makeJson import makej

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
