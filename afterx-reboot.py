import psutil
import os
import time

#check uptime
def minutes_elapsed():
    return (time.time() - psutil.boot_time())/60


#if greater then 3 days reboot
while True:
    time.sleep(60)
    if minutes_elapsed() >= 4320:
        os.system('/bin/systemctl reboot -i')
