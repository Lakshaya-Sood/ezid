import mongo_connector as mc
from pymongo import errors

readings = mc.readings


def input_scan_data(data):
    try:
        return readings_mongo.insert_many(data)
    except errors.ServerSelectionTimeoutError:
        print("offline")

def write_to_cache(uui,timestamp,scannerid):
    return readings_sql.execute("INSERT INTO readings (uui, timestamp, scannerid)VALUES (?,?,?);",
    [uui,timestamp,scannerid])

def read_from_cache(uui,timestamp,scannerid):
    cur = readings_sql.execute("SELECT * FROM readings WHERE uui=? AND timestamp=? AND scannerid=?;",
    [uui,timestamp,scannerid])
    return cur.fetchmany()


