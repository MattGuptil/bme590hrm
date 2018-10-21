import numpy as np
import pands as pd
import sys


def collector():
    myfile = "data"

    fname = input("Enter File Name: ")

    if fname == '':
        fname = '\\test_data1.csv'

    myfile = myfile + fname

    try:
        df = pd.read_csv(myfile)
    except FileNotFoundError:
        print('File Not Found, or File Type not Recognizable')
        sys.exit()

    my_csv = np.genfromtxt(myfile, delimiter=',')
    time, data = my_csv.transpose()
    ecgd = [time, data]

    return ecgd

