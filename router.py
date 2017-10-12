from flask import Flask, render_template, request, jsonify
import csv
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)


conn = pymongo.MongoClient("mongodb://admin:Utep123@129.108.18.142/test")
db = conn.test
db.authenticate("admin", "Utep123")

for item in db.rooms.find():
    print (item)

for item in db.workshops.find():
    print (item)

def get_users(roomname):
    teamlist = ""
    for item in db.rooms.find({"name": roomname}, {"_id": 0, "users.username":1}):
        for elem in item:
            if not isinstance(item[elem], list):
                teamlist = teamlist + ' ' + item[elem]
            else:
                for val in item[elem]:
                    for k in val:
                        teamlist = teamlist + ' ' + (val[k])
    return teamlist


def get_wsu_num(name):
    count = 0
    for item in db.workshops.find({"name" : name}, {"_id": 0, "num_ws_units": 1}):
        for elem in item:
            if not isinstance(item[elem], list):
                count = item[elem]
            else:
                for val in item[elem]:
                    for k in val:
                        count = val[k]
    return count

@app.route('/', methods=['GET', 'POST'])
def index():

    rh_num = get_wsu_num("Hijacking")

    return render_template("index.html", teamlist = "", rh_num = int(rh_num))


@app.route('/room', methods=['GET', 'POST'])
def room():

    if request.method == 'POST':

        id = ObjectId()
        roomname = request.form["roomname"]
        roomkey = request.form["roomkey"]
        username = request.form["username"]
        ip_addr = request.environ["REMOTE_ADDR"]
        wsu = request.form["wsu"]

        db.rooms.insert({"_id": id, "name": roomname, "room_key": roomkey, "users": [{"username": username, "user_ip": ip_addr}], "workshop_unit": wsu})

        return render_template('index.html', teamlist = "")

    return render_template('index.html')


@app.route('/team', methods=['GET', 'POST'])
def team():

    if request.method == 'POST':

        roomname = request.form["roomname"]
        roomkey = request.form["roomkey"]
        username = request.form["username"]
        ip_addr = request.environ["REMOTE_ADDR"]
        #ip_addr = "172.19.203.236"

        db.rooms.update(
           { "name" : roomname },
           { "$push" : { "users": {"username": username, "user_ip": ip_addr}} }
        )

        return render_template('index.html', teamlist = "")

    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template("admin.html")



if __name__ == "__main__":
    app.run()