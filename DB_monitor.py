
import pymongo
from pymongo.cursor import CursorType

# client = pymongo.MongoClient("mongodb://admin:Utep123@129.108.18.143/test")
client = pymongo.MongoClient("mongodb://root:toor@129.108.18.143")

oplog = client.local.oplog.rs

first = next(oplog.find().sort('$natural', pymongo.DESCENDING).limit(-1))
ts = first['ts']

while True:
    # Get the latest (the newest entry) in the oplog
    cursor = oplog.find({'ts': {'$gt': ts}}, cursor_type=CursorType.TAILABLE_AWAIT, oplog_replay=True)
    while cursor.alive:

        for doc in cursor:
            ts = doc['ts']
            # print doc

            # TODO Run nginx script whenever there is a change in a DB

            # Check for changes done in the test database only
            # if 'test' in doc['ns']:

            # Insertion done in database
            if doc['op'] == 'i':
                print 'INSERTION in database'

            # Update to a document done in a database
            elif doc['op'] == 'u':
                print 'UPDATE to a document in database'

            # There was a deletion in a database
            elif doc['op'] == 'd':
                print 'Document got DELETED'

            # Noop
            # There are constants noops in the oplog
            # if doc['op'] == 'n':
            #     print ''
