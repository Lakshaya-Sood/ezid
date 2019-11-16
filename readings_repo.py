import db_connectors as dc

readings_mongo = dc.readings
readings_sql = dc.cursor


def input_scan_data(data):
    return readings_mongo.insert_many(data)

def write_to_cache(uui,timestamp,scannerid):
    return readings_sql.execute("INSERT INTO readings (uui, timestamp, scannerid)VALUES (?,?,?);",
    [uui,timestamp,scannerid])

def read_from_cache(uui,timestamp,scannerid):
    cur = readings_sql.execute("SELECT * FROM readings WHERE uui=? AND timestamp=? AND scannerid=?;",
    [uui,timestamp,scannerid])
    return cur.fetchmany()

