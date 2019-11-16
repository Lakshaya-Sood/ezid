import requests as r

def start_scan():
    r.post("http://169.254.57.201/api/MIStartInventory")

def stop_scan():
    r.post("http://169.254.57.201/api/MIStopInventory")

def retrieve_serials():
    data = r.get("http://169.254.57.201/api/QuickstartInventoryVar").json()

    return data
