import time
from multiprocessing import Process

from bapcs import cool as bapcs
from hws import cool as hws

if __name__ == "__main__":
    process1 = Process(target=bapcs)
    process2 = Process(target=hws)
    process1.start()
    time.sleep(5)
    process2.start()