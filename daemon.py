import reader as r
import threading
from gpiozero import LED, Button
from readings_repo import input_scan_data
from subprocess import call
from time import sleep
from reader import ip

button = Button(4)
ledwifi = LED(16)
ledscanner = LED(20)
ledpower = LED(21)


def ping(host):
    return call(["ping", "-c", "4", "-w", "2", host]) == 0


def sensor_heartbeat():
    while True:
        sleep(15)
        if ping(ip):
            ledwifi.on()
        else:
            ledwifi.off()


def event_loop():
    # setup the LEDs to be active at start
    ledwifi.on()
    ledscanner.on()
    ledpower.on()

    # start the sensor_heartbeat
    t = threading.Thread(target=sensor_heartbeat)
    t.start()

    while True:
        button.wait_for_press()

        data = r.retrieve_serials(10, 1)
        if data is None:
            # indicate connection failure
            ledscanner.off()
        # if data is not empty, push it to the database
        elif data:
            input_scan_data(data)


event_loop()
