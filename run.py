import sys
from datetime import datetime

with open(str(datetime.now()) + '.non_sense', 'a+') as f:
    f.write(str(datetime.now()))
    f.write('\n')