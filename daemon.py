import logging
import reader as r
from gpiozero import LED, Button
from pymongo import MongoClient


def push_data(data):
    # client = MongoClient(
    #     "mongodb+srv://ezid_usr:8ObxwonM7WBclGOr@ezid-8j9dg.gcp.mongodb.net/test?retryWrites=true&w=majority"
    # )
    # db = client.test
    # collection = db.test
    # collection.insert_one(data)
    print(data)
    print("\n\n\n\n")


def event_loop():
    button = Button(4)
    while True:
        button.wait_for_press()
        push_data(r.retrieve_serials(10))
