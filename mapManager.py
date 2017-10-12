import pymongo

client = pymongo.MongoClient("mongodb://admin:Utep123@localhost/test")
db = client.test
db.authenticate("admin","Utep123")

collection = db.rooms
file = open("maps.conf", "a")
file.write("\n")
workshops = []
ips = {}
for item in collection.find({}, {'users.user_ip': 1, 'workshop_unit':1,  '_id':0}):
    for item_key in item:
        if not isinstance(item[item_key], list):
            workshops.append(item[item_key])
        else:
            for ip in item[item_key]:
                for ip_key in ip:
                    ips[ip[ip_key]] = workshops[len(workshops) -1]

counter = 1
previousws = ""
for key in ips:
    currentws = ips[key]
    if currentws == previousws:
        counter = counter +1
    else:
        counter = 1
    s = key+ " "+ips[key]+"-"+`counter`+";\n"
    previousws = currentws
    file.write(s)
