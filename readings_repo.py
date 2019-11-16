import mongo_connector as mc

readings = mc.readings

def input_scan_data(data):
    # do some while inserting in database
    readings.insert_one(data)