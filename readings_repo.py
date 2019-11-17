import db_connectors as dc
from pymongo import errors

readings_mongo = dc.readings
readings_sql = dc.cursor


def input_scan_data(data):
    try:
        return readings_mongo.insert_many(data)
    except errors.ServerSelectionTimeoutError:
        return None


def write_to_cache(data):
    for element in data:
        readings_sql.execute(
            "INSERT INTO readings (uii, scannerid, timestamp) VALUES (?,?,?);",
            [element["uii"], element["scannerid"], element["timestamp"]]
        )


def check_cache():
    """Returns true if there is any cached data in the database."""
    return readings_sql.execute("SELECT COUNT(*) FROM readings;").fetchone()[0] > 0


def read_from_cache():
    """Read all cached data from the database."""
    return list(map(lambda row: {"uii": row[0],
                                 "scannerid": row[1],
                                 "timestamp": row[2]},
                    readings_sql.execute(
                        "SELECT uii, scannerid, timestamp FROM readings;"
                    ).fetchmany()))


def clear_cache():
    """Used to clear the cache once the data was successfully uploaded."""
    readings_sql.execute("DELETE * FROM readings;")
