from flask import Flask, request, jsonify, render_template
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
pwd = os.environ.get('PASSWORD')

# create connection object
con = mysql.connector.connect(
    host="localhost", user="root",
    password=pwd,
     database = "Jukebox", auth_plugin = 'mysql_native_password')

# Cursor Object Created
cur_object = con.cursor()


@app.route("/")
def jukebox():
    return render_template("index.html")

@app.route("/user.html")
def jukebox1():
    return render_template("user.html")

@app.route("/view", methods = ["POST"])
def selectView(*kargs):
    query1 = "show tables;"
    cur_object.execute(query1)
    table1 = cur_object.fetchall()
    print('\n Table Description:')
    for attr in table1:
        print(attr)
    pass
    return render_template("index.html", table1 = table1)


@app.route('/fetch', methods=['POST', 'GET'])
def fetch():
    result = request.form
    print(result)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
