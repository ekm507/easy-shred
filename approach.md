# easy file shredder

this is probably not the best code possible,  
but it's friendly :)

## how it works

getting a filename and address, it openes file as write and gets  
the filesize.

then it simply fills file with zeros so file gets shredded.

finally using shell commands it deletes the file.

## TODO

* force shred a file: do it even if a process it using the file.

* write a `main.py` file, so it can be used from shell.
