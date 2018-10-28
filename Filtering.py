import numpy as np
from scipy import signal


def myfilter(df):
    """This function applies a low pass filter to a numpy array.

    Args:
        df: Array of 2 Numpy arrays that are time and voltage.

    Returns:
        Array of 2 Numpy arrays.

        Raises:
            TypeError: If the array is empty or if 'df' is an int or str or NaN another type is not possible.

    """
    if len(df) == 0 or isinstance(df, int) or isinstance(df, str) or not len(df) == 2:
        raise TypeError("Error: Array Passed into Filter was Empty or not an Array")
    mytime = df[0]
    myvolt = df[1]
    b, a = signal.butter(4, .1, 'low')

    output = signal.filtfilt(b, a, myvolt)

    # plt.plot(mytime, myvolt, label='Original')
    # plt.plot(mytime, output, label='filtered')
    # plt.show()

    filtdata = (mytime, output)
    return filtdata


if __name__ == "__main__":
    d = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
    print(myfilter(d))
