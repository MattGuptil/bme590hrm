import numpy as np


def findqrs(data):

    dsq = doubdiff(data)
    mysorted = mysort(dsq)  # Sorts in reverse order and gives indices of QRS segments
    diffarray = diffselect(mysorted)  # Trims based on QRS segments
    f = diffarray[0]
    f = np.sort(f)
    f = np.flip(f)  # Gives Indices of detected QRS segments

def doubdiff(data):

    volt = data[1]
    time = data[0]
    m = len(volt)
    d1 = []
    d2 = []
    for i in range(0, m-2):
        d1[i] = volt[i+1] - volt[i]

    for j in range(0, m-3):
        d2[j] = d1[j+1] - d1[j]

    dsq = np.square(d2)

    return dsq


def mysort(v):

    f = np.argsort(-v)

    s = np.sort(v)

    s = np.flip(s)

    return [f, s]


def diffselect(myarray):
    time = myarray[0]
    volts = myarray[1]
    mymax = volts[0]

    mythresh = mymax - .03*mymax

    for j, i in volts:
        if i < mythresh:
            j = j - 1  # used to trim voltage array
            break

    time = time[:j]
    volts = volts[:j]
    return [time, volts]
