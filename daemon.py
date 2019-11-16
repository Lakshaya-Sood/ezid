import logging
import reader as r
from gpiozero import LED, Button
from readings_repo import input_scan_data


def event_loop():
    button = Button(4)
    while True:
        button.wait_for_press()
        input_scan_data(r.retrieve_serials(10))


event_loop()
