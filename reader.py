import requests as r

base_url = "http://169.254.57.201/api/"


def fetch(method):
    """Basic data fetch. Checks the header for any errors."""
    res = r.get(base_url + method).json()

    if res["header"]["status"] != 0:
        raise RuntimeError("Fecthing data failed. Message: {}".format(
            res["header"]["message"]))
    return res


def start_scan():
    r.post(base_url + "MIStartInventory")


def stop_scan():
    r.post(base_url + "MIStopInventory")


def is_running():
    return fetch("QSIsQuickStartRunning")["data"]["QSIsQuickStartRunning"]


def parse_serial(entry):
    # assuming that last 7 bytes of EPC are the serial
    entry["serial"] = int("".join(map(lambda s: hex(s)[2:],
                                      entry["EPC"][-7:])), 16)
    return entry


def retrieve_serials():
    data = fetch("QuickstartInventoryVar")

    return map(parse_serial, data["data"]["QuickstartInventoryVar"]["Tags"])
