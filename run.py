import sys
from datetime import datetime
import time
import os

n = int(raw_input("HAck COunt: "))
filename = "abc"
for i in range(0,n):
    with open(filename, 'a+') as f:
        f.write(str(datetime.now()))
        os.rename(filename,filename)
        os.system('git add .')
        os.system('git commit -m "added nonsense file"')
        time.sleep(1)
