import requests as r
import socket

base_url = "http://169.254.57.201/api/"
ip = "169.254.57.201"


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


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


def retrieve_serials(iterations):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 2111))

    result = []

    for i in range(iterations):
        s.send(b"\x02sMN IVSingleInv F\x03")
        data = s.recv(8192)
        print(parse_inv(data))
