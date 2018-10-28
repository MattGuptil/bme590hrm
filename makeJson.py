import json


#  Takes a dictionary in and a string that represents the file name where data was taken from
#  Creates a json file with the same name as the csv file that data was taken from
#  Returns nothing because it creates a file. Also fname will never be empty since our collector sets a default
def makej(mydir, fname):
    """Makes a JSON file and writes a dictionary to it.

    Args:
        mydir: Dictionary containing ecg data metrics.
        fname: String containing name of the csv file data was taken from.

    Returns:
        Nothing but it does create a file with the same name as the csv file data was collected from.

    Raises:
        TypeError: If 'mydir' is not a dict or if 'fname' is not a string.
    """
    if not isinstance(mydir, dict):
        raise TypeError("Input was not a dictionary")
    if not isinstance(fname, str):
        raise TypeError("File Name is not a string")

    fname = fname.strip('.csv').strip('\\')
    fname = fname + '.json'
    with open(fname, 'w') as fp:
        json.dump(mydir, fp)
    return


if __name__ == '__main__':
    fname = 'myTEST2.csv'
    mydir = {'a': 1, 'b': [1, 2, 2]}

    makej(mydir, fname)
