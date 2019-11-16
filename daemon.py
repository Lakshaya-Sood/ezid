import threading
import logging

HIT_PERIOD = 1 #in seconds

def call_per_sec(func, sec):
    def wrapper():
        call_per_sec(func, sec)
        func()

    timer = threading.Timer(sec, wrapper)
    timer.start()

    return timer

def hel():
    print("hello")

call_per_sec(hel, HIT_PERIOD)