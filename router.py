from flask import Flask, render_template, request, jsonify
import csv

app = Flask(__name__)


def get_csv():
    teamlist = ''
    with open('static/teamlist.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            teamlist = teamlist + ' ' + row['username'] + ', '
        return teamlist

def set_csv(un, rk):
     writer = open('static/teamlist.csv','a')
     writer.seek(0,2)
     writer.writelines("\r")
     writer.writelines( (',').join([un, rk]))



@app.route('/', methods=['GET', 'POST'])
def index():

    teamlist = get_csv()
    return render_template("index.html", teamlist = teamlist)

@app.route('/team', methods=['GET', 'POST'])
def team():

    if request.method == 'POST':

        username = request.form["username"]
        roomkey = request.form["roomkey"]
        set_csv(username, roomkey)

        teamlist = get_csv()

        return render_template('index.html', teamlist = teamlist)

    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template("admin.html")



if __name__ == "__main__":
    app.run()
