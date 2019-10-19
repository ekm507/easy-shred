
import os

def shred(filename):
    size = os.stat(filename).st_size

    for i in range(size):
        writeInFile(filename, 0)

    print(size)
    os.remove(filename)

