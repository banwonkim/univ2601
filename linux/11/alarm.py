import signal
import time
import sys
def alarm_hand(signo, frame):
    print('shut up')
    sys.exit(0)
    
