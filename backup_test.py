import zipfile as zip
import os
from time import time, ctime, sleep
import zlib
from alive_progress import alive_bar

print(r"""/
▪       ▄▄ •       ▄▄▄▄▄     ▄· ▄▌      ▄• ▄▌    ▄▄▄▄· ▄▄▄        
██     ▐█ ▀ ▪▪     •██      ▐█▪██▌▪     █▪██▌    ▐█ ▀█▪▀▄ █·▪     
▐█·    ▄█ ▀█▄ ▄█▀▄  ▐█.▪    ▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ▐█▀▀█▄▐▀▀▄  ▄█▀▄ 
▐█▌    ▐█▄▪▐█▐█▌.▐▌ ▐█▌·     ▐█▀·.▐█▌.▐▌▐█▄█▌    ██▄▪▐█▐█•█▌▐█▌.▐▌
▀▀▀    ·▀▀▀▀  ▀█▄▀▪ ▀▀▀       ▀ •  ▀█▄▀▪ ▀▀▀     ·▀▀▀▀ .▀  ▀ ▀█▄▀▪
""")

backup_dst = '/Users/uwe/opt/Backup'
t = time()
Stamp = ctime(t)
path_input = input('Enter the path to backup: ')
Stamp_time=Stamp.replace(':', '_')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def backup(data):
    with zip.ZipFile(Stamp_time+' backup.zip', 'w', zip.ZIP_DEFLATED, compresslevel=9) as myzip:
        for root, dirs, files in os.walk(data):
                with alive_bar(len(files)) as bar:
                    for file in files:
                        myzip.write(os.path.join(root, file)) 
                        bar()
                        sleep(0.1)
                        print('File: ', file, ' added to backup')
                        sleep(0.1)  #feels more natural
    print(bcolors.OKGREEN + 'Backup finished')

backup(path_input)