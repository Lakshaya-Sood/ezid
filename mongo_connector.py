from pymongo import MongoClient
import ssl

ATLAS_SECRET = open("./mongodb_secret.txt").readlines()[0].strip()
ATLAS_USER = "ezid_usr"

CONNECTION_URL = "mongodb+srv://" + ATLAS_USER + ":" + ATLAS_SECRET + "@ezid-8j9dg.gcp.mongodb.net/test?retryWrites=true&w=majority"
DB_NAME = "ezid"

client = MongoClient(CONNECTION_URL, ssl_cert_reqs=ssl.CERT_NONE)
db = client[DB_NAME]
readings = db["readings"]
