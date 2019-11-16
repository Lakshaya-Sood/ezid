import threading
import logging
import reader as r
from time import sleep

HIT_PERIOD = 1  # in seconds


def call_per_sec(func, sec):
    def wrapper():
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            func()
            sleep(HIT_PERIOD)

    t = threading.Thread(target=wrapper)
    t.start()
    return t


# testing the reading functionality
# r.start_scan()

# t = call_per_sec(lambda: print(list(r.retrieve_serials())), HIT_PERIOD)
# sleep(3) # simulate the wait for the button press
# t.do_run = False
# t.join()  # wait for the thread to actually finish

# r.stop_scan()

def event_loop():
    while True:
        pass
