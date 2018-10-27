import json


def makej(mydir, fname):

    if not isinstance(mydir, dict):
        raise TypeError("Input was not a dictionary")
    if not isinstance(fname, str):
        raise TypeError("File Name is not a string")

    fname = fname.strip('.csv')
    fname = fname + '.json'
    with open(fname, 'w') as fp:
        json.dump(mydir, fp)

    return


if __name__ == '__main__':
    fname = 'myTEST.csv'
    mydir = 1

    makej(mydir, fname)
