import mongo_connector as mc
from pymongo import errors

readings = mc.readings


def input_scan_data(data):
    try:
        readings.insert_many(data)
    except errors.ServerSelectionTimeoutError:
        print("offline")
