from playsound import playsound
import os
import time


# Open audio files folder
path = "C:\\Users\\shoval\\Music\\Ron audio files\\"
a = os.listdir(path)  # Directory where the wav files are at

# Playback each file on the list
for file in a:
    print "Start playback file {} at {}".format(file, time.strftime("%H:%M:%S"))
    for number in range(1, 3):  # Number of time to playback each file
        playsound(path + file)


