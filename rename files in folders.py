import os

lijstmetfiles = os.listdir(os.getcwd())
    for i in range(len(lijstmetfiles)):
        os.rename(str(lijstmetfiles[i]), str(lijstmetfiles[i])