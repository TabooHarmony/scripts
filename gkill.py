import math
import os
import time
import psutil as psutil
while True:
    try:
        os.system("cls")
        print("_____________________________________________________")
        for pid in psutil.process_iter():
           if(pid.name() == "RobloxPlayerBeta.exe"):
               print(str(pid.pid)+" mem:"+str(math.trunc(psutil.Process(pid.pid).memory_info().rss / 1024 / 1024))+"M Status:"+psutil.Process(pid.pid).status())
        for pid in psutil.process_iter():
           if(pid.name() == "RobloxPlayerBeta.exe"):
               if (psutil.Process(pid.pid).memory_info().rss / 1024 / 1024)<50 and psutil.Process(pid.pid).status()== "running":
                   psutil.Process(pid.pid).suspend()
                   print(str(pid.pid)+" suspended")
        time.sleep(5)
    except:
        pass
