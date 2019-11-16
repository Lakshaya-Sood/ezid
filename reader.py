import requests as r
import socket
from time import time, sleep
import threading

base_url = "http://169.254.57.201/api/"
ip = "169.254.57.201"
uuid = open("./uuid.txt").readlines()[0].strip()


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def flatten(l):
    return [item for sublist in l for item in sublist]


def start_scan():
    r.post(base_url + "MIStartInventory")


def stop_scan():
    r.post(base_url + "MIStopInventory")


def parse_chunk(chunk):
    return {"uii": chunk[1],
            "antenna_id": chunk[2],
            "rssi": chunk[3:7],
            "antenna_power": chunk[7:]}


def parse_inv(inv):
    if not inv.startswith(b"\x02sAN IVSingleInv"):
        raise RuntimeError("Failed to read from device.")
    else:
        data = map(parse_chunk, chunks((inv[1:-1]).split()[4:], 11))
        return list(data)


def retrieve_serials(duration, threshold):
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect((ip, 2111))
    result = []

    def retrieve():
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            # s.send(b"\x02sMN IVSingleInv F\x03")
            # data = s.recv(8192)
            data = example_data[0]
            result.append(parse_inv(data))
            sleep(0.5)  # TODO: remove this when using actual data

    t = threading.Thread(target=retrieve)
    t.start()
    sleep(duration)
    t.do_run = False
    t.join()
    # s.close()

    uiis = list(map(lambda inv: inv["uii"].decode("ascii"), flatten(result)))
    unique = set(filter(lambda uii: uiis.count(uii) > threshold, uiis))

    return list(map(lambda uii:
                    {"uii": uii,
                     "timestamp": time(),
                     "scannerid": uuid},
                    unique))
