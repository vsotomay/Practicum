from flask import Flask, render_template, request, jsonify, send_file, make_response
import os, sys
import pymongo
from bson.objectid import ObjectId

import socket
import fcntl
import struct

app = Flask(__name__)


conn = pymongo.MongoClient("mongodb://admin:Utep123@129.108.18.143/test")
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
                        teamlist = teamlist + ' -- ' + (val[k])
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

def get_roomkey(roomname):
    roomkey = ""
    for item in db.rooms.find({"name": roomname}, {"_id": 0, "room_key": 1}):
        for elem in item:
            if not isinstance(item[elem], list):
                roomkey = item[elem]
            else:
                for val in item[elem]:
                    for k in val:
                        roomkey = val[k]
    return roomkey

def user_exists(username):
    if db.rooms.find({'users.username': username}).count() > 0:
        return 1
    else:
        return 0



@app.route('/', methods=['GET', 'POST'])
def index():

    rh_num = get_wsu_num("Route Hijacking")
    bo_num = get_wsu_num("Buffer Overflow")

    return render_template("index.html", rh_num = int(rh_num), bo_num=int(bo_num), get_users=get_users)


@app.route('/room', methods=['GET', 'POST'])
def room():

    if request.method == 'POST':

        id = ObjectId()
        roomname = request.form["roomname"]
        roomkey = request.form["roomkey"]
        username = request.form["username"]
        ip_addr = request.environ["REMOTE_ADDR"]
        port = request.environ.get('REMOTE_PORT')
        wsu = request.form["wsu"]

        db.rooms.insert(
            {"_id": id, "name": roomname, "room_key": roomkey, "users":
            [{"username": username, "user_ip": ip_addr, "user_port": port}],
            "workshop_unit": wsu}
        )

        filename = "static/rdp/rdp-" + username + ".rdp"
        f = open(filename,'w')
        f.write("full address:s:129.108.18.142:5000\nloadbalanceinfo:s:" + username)
        f.close()

        return render_template('download.html',username=username)

    return render_template('index.html')


@app.route('/team', methods=['GET', 'POST'])
def team():

    rh_num = get_wsu_num("Route Hijacking")
    bo_num = get_wsu_num("Buffer Overflow")

    if request.method == 'POST':

        roomname = request.form["roomname"]
        roomkey = request.form["roomkey"]
        username = request.form["username"]
        ip_addr = request.environ["REMOTE_ADDR"]
        port = request.environ.get('REMOTE_PORT')

        lead_roomkey = get_roomkey(roomname)

        if lead_roomkey == roomkey:

            exists = user_exists(username)

            if exists == 0:
                db.rooms.update(
                    { "name" : roomname },
                    { "$push" : { "users": {"username": username, "user_ip": ip_addr, "user_port": port}} }
                )
            else:
                db.rooms.update(
                    { "users.username": username },
                    { "$set": { "users.$.user_ip": "1.1.0.0", "users.$.user_port": port } }
                )


            filename = "static/rdp/rdp-" + username + ".rdp"
            f = open(filename,'w')
            f.write("full address:s:129.108.18.142:5000\nloadbalanceinfo:s:" + username)
            f.close()

            return render_template('download.html',username=username)

        else:
            return render_template('index.html', rh_num = int(rh_num), bo_num=int(bo_num), get_users=get_users, message="ROOM KEY INCORRECT")

    return render_template('index.html')

@app.route('/download')
def download():
	try:
	    username = request.args.get('username')
	    filename_dir = "static/rdp/rdp-" + username + ".rdp"
	    filename = "rdp-" + username + ".rdp"

	    os.system("sh /Users/plusvictoria/Repositories/Practicum/test.sh")

	    return send_file(filename_dir, attachment_filename=filename, as_attachment=True)
	except Exception as e:
		return str(e)


@app.route('/admin')
def admin():
    return render_template("admin.html")



if __name__ == "__main__":
    app.run(host= '0.0.0.0')
    #app.run()