import pandas as pd
import os

def collector():
    myfile = "data"

    fname = input("Enter File Name: ")

    if fname == '':
        fname = '\\test_data1.csv'

    myfile = myfile + fname

    df = pd.read_csv(myfile)
    return df


if __name__ == "__main__":
    print(collector())
