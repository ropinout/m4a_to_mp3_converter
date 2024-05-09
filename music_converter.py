import os
import soundfile as sf

main_folder = os.listdir()
for file_name in main_folder:
    if file_name.endswith('.mp3'):
        data, samplerate = sf.read(file_name)
        sf.write(file_name[:-4] + ".wav", data, samplerate, format='WAV')
    else:
        print(file_name, "is not mp3, so i cant convert")
