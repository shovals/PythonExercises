from multiprocessing import Pool
from multiprocessing import cpu_count
import os
from time import sleep
from shutil import copyfile


def f(x):
    counter = 0
    while True and counter < 100000000:  # Counter is used as a time limit for loading the CPU
        x*x
        counter += 1


if __name__ == '__main__':

    print ""
    print ""
    print "     O~~~~          O~            O~~                               O~~"
    print "  O~~    O~~      O~ ~~          O~~                               O~~"
    print "O~~       O~~    O~  O~~         O~~         O~~       O~~         O~~"
    print "O~~       O~~   O~~   O~~        O~~       O~~  O~~  O~~  O~~  O~~ O~~"
    print "O~~       O~~  O~~~~~~ O~~       O~~      O~~    O~~O~~   O~~ O~   O~~"
    print "  O~~ O~ O~~  O~~       O~~      O~~       O~~  O~~ O~~   O~~ O~   O~~"
    print "    O~~ ~~   O~~         O~~     O~~~~~~~~   O~~      O~~ O~~~ O~~ O~~"
    print "         O~                                                           "
    print ""
    print ""

    print "--- QA Load Generator App Ver 1.0 ---\n"
    print "1 - CPU load\n" \
          "2 - Memory load\n" \
          "3 - Disk load\n" \
          "4 - Exit\n"

    LoadSelection = input("Enter the load to generate >>> ")

    os.startfile('C:\\Windows\\System32\\Taskmgr.exe')  # opening the task manager to view load

    if LoadSelection == 1:  # Loads all processors of the CPU
        print "CPU load generating..."
        processes = cpu_count()
        print "Utilizing %d cores" % processes
        pool = Pool(processes)
        pool.map(f, range(processes))

    elif LoadSelection == 2:
        print "Memory load generating...\n"
        n = 1600000000  # allocating a bunch of memory to run
        b = [0] * n

    elif LoadSelection == 3:  # Copy several big files to the disk
        print "Disk load generating..."
        dir_name = os.getcwd()   # Get current working directory
        f = open('bigfile.big', "wb")  # Create a 1G file size to copy
        f.seek(1073741824 - 1)
        f.write("\0")
        f.close()
        for filecopy in range(1, 11):  # Create copies of the 1G file
            copyfile("bigfile.big", "bigfile {}.big".format(filecopy))
        test = os.listdir(dir_name)  # Get directory file list including *.big files to remove
        for item in test:  # Remove copied files from disk
            if item.endswith(".big"):
                os.remove(os.path.join(dir_name, item))

    elif LoadSelection == 4:
        print "How about NOOOOOOOOOO..."
        quit()
