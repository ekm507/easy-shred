def shred(filename):
    size = getFileSize(filename)

    for i in range(size):
        writeInFile(filename, 0)

    deleteFile(filename)