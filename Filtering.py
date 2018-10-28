import numpy as np
from scipy import signal
from Datacollector import collector


def myfilter(df):
    """This function applies a low pass filter to a numpy array.

    Args:
        df: Array of 2 Numpy arrays that are time and voltage.

    Returns:
        Array of 2 Numpy arrays.

        Raises:
            TypeError: If the array is empty or if 'df' is an int or str or NaN another type is not possible.

    """
    if not df or isinstance(df, int) or isinstance(df, str):
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
    df = collector()
    myfilter(df)
