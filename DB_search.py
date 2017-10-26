from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
from bson.objectid import ObjectId

import json
import ast
import bson
import collections


# This function prints all the documents in the "workshops" collection
def print_WS():
    try:
        entries = WS_collection.find()
        for document in entries:
            print document

    except Exception, e:
        print str(e)

# This function returns the document inside the "workshops" collection by name
def search_WS(workshop_name):
    try:
        doc = WS_collection.find_one({"name": workshop_name})
        return doc

    except Exception, e:
        print str(e)

# This function returns the document's ID inside the "workshops" collection by name
def search_WS_ID(workshop_name):
    try:
        # Cursor
        # mongodb_cursor = WS_collection.find({"name": workshop_name}, {"name": 1})

        # Dictionary
        query_dictionary = WS_collection.find_one({"name": workshop_name}, {"name": 1})

        return query_dictionary['_id']

    except Exception, e:
        print str(e)

# This function returns the document inside the "workshop_name" collection by ObjectID
def search_WS_by_ID(WS_id):
    try:

        doc = WS_collection.find_one({"_id": ObjectId(WS_id)})

        return doc
    except Exception, e:
        print str(e)

# This function prints all the documents in the "workshops_units" collection
def print_WSU():
    try:
        entries = WSU_collection.find()
        for document in entries:
            print document

    except Exception, e:
        print str(e)

# This function returns the document inside the "workshops_units" collection by name
def search_WSU(workshop_unit_name):
    try:
        doc = WSU_collection.find_one({"name": workshop_unit_name})
        # print doc
        return doc

    except Exception, e:
        print str(e)

# This function returns the document's ID inside the "workshop_units" collection by name
def search_WSU_ID(workshop_unit_name):
    try:
        # Cursor
        # mongodb_cursor = WS_collection.find({"name": workshop_unit_name}, {"name": 1})

        # Dictionary
        query_dictionary = WSU_collection.find_one({"name": workshop_unit_name}, {"name": 1})

        return query_dictionary['_id']

    except Exception, e:
        print str(e)

# This function returns the document inside the "workshop_unit_name" collection by ObjectID
def search_WSU_by_ID(WSU_id):
    try:
        doc = WSU_collection.find_one({"_id": ObjectId(WSU_id)})

        return doc
    except Exception, e:
        print str(e)

# This function prints all the documents in the "rooms" collection
def print_rooms():
    try:
        entries = rooms_collection.find()
        for document in entries:
            print document

    except Exception, e:
        print str(e)

# This function returns the document inside the "rooms" collection by name
def search_room(room_name):
    try:
        doc = WS_collection.find_one({"name": room_name})
        # print doc
        return doc

    except Exception, e:
        print str(e)

# This function returns the document inside the "rooms" collection by ObjectID
def search_room_ID(room_name):
    try:
        doc = rooms_collection.find_one({"name": room_name}, {"name": 1})

        return doc['_id']
    except Exception, e:
        print str(e)

# This function returns the document inside the "workshop_unit_name" collection by ObjectID
def search_room_by_ID(WSU_id):
    try:
        doc = rooms_collection.find_one({"_id": ObjectId(WSU_id)})

        return doc
    except Exception, e:
        print str(e)

# This function searches users based on username and returns that document
def search_user(username):
    try:
        user_doc = rooms_collection.find_one({'users.username': username})
        return user_doc

    except Exception, e:
        print str(e)

# This function searches for a user with the specified IP and returns that document
def search_user_by_IP(user_IP):
    try:
        user_doc = rooms_collection.find_one({'users.userip': user_IP})
        return user_doc
    except Exception, e:
        print str(e)

# This function searches for the specified user's IP
def search_user_IP(username):
    try:
        user_IP
    except Exception, e:
        print str(e)
# This function searches the entire "test" Database for a document with the specified ObjectID and returns it
def search_DB_by_ID(document_ID):
    try:
        doc = WS_collection.find_one({"_id": ObjectId(document_ID)})
        if doc is not None:
            return doc

        doc = WSU_collection.find_one({"_id": ObjectId(document_ID)})
        if doc is not None:
            return doc

        doc = rooms_collection.find_one({"_id": ObjectId(document_ID)})
        if doc is not None:
            return doc

    except Exception, e:
        print str(e)


client = MongoClient("mongodb://admin:Utep123@129.108.18.143/test")

# Database used is called test
db = client.test

# Collections used
WS_collection = db.workshops
WSU_collection = db.workshop_units
rooms_collection = db.rooms

print_WS()
# print_WSU()
# print_rooms()
# print(search_user("Marco"))
# print(search_WSU("wsu2"))
# print(search_WS_ID("Hijacking"))
# print(search_DB_by_ID(search_room_ID("Test Room 1")))

print client.test.getUsers()
