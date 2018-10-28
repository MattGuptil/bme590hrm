import numpy as np
import pandas as pd


def collector():
    """Function Prompts User for File Name, Collects data from csv file.

        Args:

        Returns:
            Array of numpy arrays with missing values filled in as -999.

        Raises:
            FileNotFoundError: If 'df' is not findable.
            IOError: If error occurs when searching for file
            Type Error: If a string is not taken in

    """
    myfile = "data"

    fname = input("Enter File Name: ")
    if not isinstance(fname, str):
        raise TypeError("Error: Not a string")
    if fname == '':
        fname = '\\test_data1.csv'

    myfile = myfile + fname

    try:
        df = pd.read_csv(myfile)
    except FileNotFoundError:
        print('Error: File Not Found, or File Type not Recognizable')
    except IOError:
        print('Error: File Not Found, or File Type not Recognizable')

    my_csv = np.genfromtxt(myfile, delimiter=',', filling_values=-999)
    time, data = my_csv.transpose()
    ecgd = [time, data]

    return ecgd, fname
