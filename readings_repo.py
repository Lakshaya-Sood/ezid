import db_connectors as dc
from pymongo import errors

readings_mongo = dc.readings
readings_sql = dc.cursor


def input_scan_data(data):
    try:
        return readings_mongo.insert_many(data)
    except errors.ServerSelectionTimeoutError:
        return None


def write_to_cache(uui, timestamp, scannerid):
    return readings_sql.execute("INSERT INTO readings (uui, timestamp, scannerid) VALUES (?,?,?);",
                                [uui, timestamp, scannerid])


def check_cache():
    """Returns true if there is any cached data in the database."""
    return readings_sql.execute("SELECT COUNT(*) FROM readings;").fetchone()[0] > 0


def read_from_cache(uui, timestamp, scannerid):
    cur = readings_sql.execute("SELECT * FROM readings WHERE uui=? AND timestamp=? AND scannerid=?;",
                               [uui, timestamp, scannerid])
    return cur.fetchmany()


def clear_cache():
    """Used to clear the cache once the data was successfully uploaded."""
    readings_sql.execute("DELETE * FROM readings;")
