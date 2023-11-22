import mne
import numpy as np
import pandas as pd

file_path = 'data/OpenBCI-RAW-2023-11-22_12-56-00_dani_pilot_1.txt'

df = pd.read_csv(file_path, comment='%')

df = df.iloc[:, 1:-3]

data = df.to_numpy().T

with open(file_path, 'r') as file:
    sample_rate_line = file.readlines()[2]
    sample_rate = int(sample_rate_line.split('=')[1].split('Hz')[0].strip())

ch_names = df.columns.tolist()
ch_types = ['eeg'] * len(ch_names)

info = mne.create_info(ch_names = ch_names, sfreq = sample_rate, ch_types = ch_types)

raw = mne.io.RawArray(data, info)

