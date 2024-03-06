from scipy.io import loadmat
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import numpy as np
import os


if __name__ == '__main__':

    #frequency of telem. writing
    freq = 987

    filename = os.listdir('fourier/mat_files/')[0]
    name = 'fourier/mat_files/' + filename
    data = loadmat(name)
    name = name.split('/')[-1]
    data_items = np.concatenate([data['IMU_0'].T[1:2], data['IMU_0'].T[3:9]])
    data_labels = ['TimeUS', 'GyrX', 'GyrY', 'GyrZ', 'AccX', 'AccY', 'AccZ']

    df = pd.DataFrame({key : value for key, value in zip(data_labels, data_items)})


    T = 1 / freq
    N = len(df['TimeUS'].values)
    df_fourier = pd.DataFrame({key : (np.abs(fft(df[key].values))  if key != 'TimeUS' else fftfreq(N, T)) for key in df.keys()})

    for i, key in enumerate(df_fourier.keys()):
        if key !='TimeUS':
            plt.subplot(3, 2, i)
            plt.plot(df_fourier['TimeUS'].values[:N // 2], df_fourier[key].values[:N // 2], label=key)
            plt.xlabel('freq.')
            plt.ylabel(f'F[key]')
            plt.legend()
            plt.grid()
    plt.savefig(f'fourier/plots/spectrum_from({name})')
    df_fourier.to_csv(f'fourier/spectrum_data/spectrum_from({name}).csv')