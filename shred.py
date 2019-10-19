

from os import stat, remove

# shred a file and delete it
def shred(filename):
    # get file size
    size = stat(filename).st_size

    #open the file as write+binary
    f = open(filename, 'w+b')

    # array to be written to the file.
    # a filesize length array of zeros.
    byte_arr = [0] * size

    # byte array, so it can be written to file
    binary_format = bytearray(byte_arr)

    # shred the file
    f.write(binary_format)

    # close the file so the os can remove it
    f.close()

    # remove the shredded file's name.
    remove(filename)

