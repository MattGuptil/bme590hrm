import numpy as np
import pandas as pd
import sys


def collector():
    """Function Prompts User for File Name, Collects data from csv file.

        Args:

        Returns:
            Array of numpy arrays with missing values filled in as -999.

        Raises:
            FileNotFoundError: If 'df' is not findable.

    """
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

    my_csv = np.genfromtxt(myfile, delimiter=',', filling_values=-999)
    time, data = my_csv.transpose()
    ecgd = [time, data]

    return ecgd, fname

