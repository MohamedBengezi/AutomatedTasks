import zipfile
import os
import sys

if len(sys.argv) > 1:
    # Get address from command line.
    path = ''.join(sys.argv[1])
    name = ''.join(sys.argv[2])
else:
    path = 'D:\\benge\\Downloads\\ARCHIVES'
    name = 'original.zip'
os.chdir(path)    # move to the folder with example.zip

exampleZip = zipfile.ZipFile(name)
exampleZip.extractall()
exampleZip.close()
