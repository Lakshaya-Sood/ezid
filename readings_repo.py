import mongo_connector as mc

readings = mc.readings


def input_scan_data(data):
    readings.insert_many(data)
