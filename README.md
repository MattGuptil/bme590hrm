# bme590hrm
Heart Rate Monitor for BME590

Start:
    To run this program properly, open runHRM.py. This script 
    does not take anything in as an input.
    
   To Use:
        Run the script. The app will prompt you for an input csv file
        this csv file must be stored in a directory called data that is in the same directory as all the python files, or root.
        If no file is selected, the script defaults to test_data1.csv.
        If an incorrect file type or file is not found an exception is raised.
        Then each function is run to generate the required metrics.
        The collector function outputs the ecg data in an array and the file name as a string.
        Peakfinder takes in the ecg voltage data and finds the peaks. This function outputs the indices where the peaks have been
        found. The Durr function takes in the overall time data and finds the total duration of the data.
        Findex finds the extremes of the voltage by looking through the voltage data.
        Numbeats takes in the indices where peaks are and outputs the total number of beats.
        Timefinder takes in the total time and indices of the peaks and outputs the
        times where peaks are in an array.
        Avghr takes in the duration and times of peaks, asks user for interval, makes sure
        that the interval is within bounds and the find avg hr.
        It outputs this as a single value.
        The metrics are then stored in a dictionary. 
        Makej takes in the metrics dictionary and original file name. It
        creates a json file with the same name as the csv file that was used.
        
    Note: Code will not detect peaks that are negative.
    Note2: A graph can be displayed showing where the code found peaks if desired.
    Simply change to show =True within the newindice.py script inside the peakfinder
    function.
    Note3: To use make sure to type a backslash before inputing file name, such as '\test_data21.csv'
    Note4: Several Functions were not tested because they were 1. Used within copyright from and
    outside source (MIT). 2. Were only holder functions to execute functions 
    that already had unit tests associated with them.
    
Further:
    There are several python files that are not used and those do not have docstrings or significant unit tests.
    These were written when I was trying to build my own algorithm that would also detect the QRS intervals. I spent way
    to much time on it and I don't want to delete it so it is still in the project. These have been put into the 
    directory titled 'NotUsed'
 
        