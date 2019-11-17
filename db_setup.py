import db_connectors as dc
cursor = dc.cursor

cursor.execute('''CREATE TABLE readings(
    uui text,
    timestamp date,
    scannerid text)''')
