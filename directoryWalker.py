import os, sys

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = 'D:\\CODE'
    
print(path)

for folderName, subfolders, filenames in os.walk(path):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
