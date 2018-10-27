import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from Datacollector import collector


def myfilter(df):
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
