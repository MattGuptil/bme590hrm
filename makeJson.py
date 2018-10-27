import json


def makej(mydir, fname):

    if not isinstance(mydir, dict):
        raise TypeError("Input was not a dictionary")
    if not isinstance(fname, str):
        raise TypeError("File Name is not a string")

    fname = fname.strip('.csv').strip('\\')
    fname = fname + '.json'
    with open(fname, 'w') as fp:
        print(fname)
        json.dump(mydir, fp)
    print(json.dumps(mydir))
    return


if __name__ == '__main__':
    fname = 'myTEST2.csv'
    mydir = {'a': 1, 'b': [1, 2, 2]}

    makej(mydir, fname)
