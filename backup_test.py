import zipfile as zip
import os
from time import time, ctime

backup_dst = '/Users/uwe/opt/Backup'
t = time()
Stamp = ctime(t)
data = input('Enter the path to backup: ')


with zip.ZipFile('backup.zip', 'w') as myzip:
    for root, dirs, files in os.walk(data):
        for file in files:
            myzip.write(os.path.join(root, file))
            print('File: ', file, ' added to archive')
    print('Backup finished')

