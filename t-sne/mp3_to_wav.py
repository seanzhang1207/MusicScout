from os.path import split, splitext, join
import subprocess
from glob import glob
import numpy as np
import librosa
import cv2

data_path = '/Users/sean/Desktop Workspaces/MusicScout/dataset'

# Convert new MP3s if there is any
mp3_path = join(data_path, 'mp3')
wav_path = join(data_path, 'wav')
mp3_files = glob(join(mp3_path, '*.mp3'))
wav_files = glob(join(wav_path, '*.wav'))

for mp3_file in mp3_files:
    mp3_name = splitext(split(mp3_file)[1])[0]
    wav_name = mp3_name + '.wav'
    wav_file = join(wav_path, wav_name)

    if wav_file not in wav_files:
        command = ['ffmpeg', '-i', mp3_file, '-vn', '-acodec', 'pcm_s16le', '-ac', '1', '-ar', '44100', '-f', 'wav', wav_file]
        subprocess.run(command)
