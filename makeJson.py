import json


#  Takes a dictionary in and a string that represents the file name where data was taken from
#  Creates a json file with the same name as the csv file that data was taken from
#  Returns nothing because it creates a file
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
