import sys
from datetime import datetime
import time
import os

n = int(raw_input("HAck COunt: "))
filename = "abc"

# yy = "2018"
# mm = "05"
# commits_in_a_day = n/30

# for dd in range(0,30):

for i in range(0,n):
    with open(filename, 'a+') as f:
        # for count in range(0,commits_in_a_day)
        # os.system('date +%Y%m%d -s "' + yymmdd + "'")
        f.write(str(datetime.now()))
        os.rename(filename,filename)
        os.system('git add .')
        os.system('git commit -m "Nonsense commit by Hack bot"')
        time.sleep(1)
