import requests as r


def start_scan():
    r.post("http://169.254.57.201/api/MIStartInventory")


def stop_scan():
    r.post("http://169.254.57.201/api/MIStopInventory")

    
def parse_serial(entry):
    # assuming that last 7 bytes of EPC are the serial
    entry["serial"] = int("".join(map(lambda s: hex(s)[2:],
                                      entry["EPC"][-7:])), 16)
    return entry
    

def retrieve_serials():
    data = r.get("http://169.254.57.201/api/QuickstartInventoryVar").json()
    
    return map(parse_serial, data["data"]["QuickstartInventoryVar"]["Tags"])
