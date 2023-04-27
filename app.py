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

userid = ""
genreList = ""
songdata = list()
likedsongs = list()

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home", methods = ["POST", "GET"])
def jukebox():
    global userid, genreList
    try:
        user = request.form
        userid = dict(user)["userid"]
    except:    
        pass
    q1 = "SELECT distinct genre from Song;"
    cur_object.execute(q1)
    genreList = cur_object.fetchall()
    for attr in genreList:
        print(attr[0])
    return render_template("index.html", data = [userid,genreList])

@app.route("/view", methods = ["POST"])
def selectView(*kargs):
    pass


@app.route('/home/fetch', methods=['POST', 'GET'])
def fetch():
    global userid, genreList, songdata
    result = request.form
    dictSong = dict(result)
    try:
        if(dictSong['Searched'] == "1"):
            print(dictSong)
            if(dictSong["genre"] == "" and dictSong["title"] == ""):
                q1 = "SELECT * from song;"
            else:
                q1 = "SELECT * from song where genre = '" + dictSong["genre"] + "' or title = '" + dictSong["title"] + "';"
            cur_object.execute(q1)
            # q2 = "select * from playlist_contains where playlist_index = 1;"

            songdata = cur_object.fetchall()      
            return render_template("index.html", data = [userid,genreList,songdata])
    except:
        songname = dict(result)['Selected']
        # print(songname['Selected'])
        q1 = "select song_id from song where title = '" + songname + "';"
        cur_object.execute(q1)
        song_id = cur_object.fetchall()[0][0]
        q2 = "INSERT INTO playlist_contains values('" + userid + "', 1, '" + song_id + "');"
        try:
            cur_object.execute(q2)  
            con.commit()
        except:
            print("Already Exits")    
        # try:
        # except:
        #     print("SQL ERROR !")    
        return render_template("index.html", data = [userid, genreList, songdata])


# @app.route('/home/fetch/like', methods = ['POST', 'GET'])
# def like():
#     global userid, genreList, songdata
#     result = request.form
#     songname = dict(result)['Selected']
#     # print(songname['Selected'])
#     q1 = "select song_id from song where title = '" + songname + "';"
#     cur_object.execute(q1)
#     song_id = cur_object.fetchall()[0][0]
#     q2 = "INSERT INTO playlist_contains values('" + userid + "', 1, '" + song_id + "');"
#     try:
#         cur_object.execute(q2)  
#         con.commit()
#     except:
#         print("Already Exits")    
#     # try:
#     # except:
#     #     print("SQL ERROR !")    
#     return render_template("index.html", data = [userid, genreList, songdata])

@app.route('/user', methods = ['POST', 'GET'])
def user():
    global userid, likedsongs
    result = request.form
    dictresult = dict(result)
    print(dictresult)
    try:
        if(dictresult['userid'] == userid):
            q1 = "Select song.title, song.song_id from song, playlist_contains as pc, users as u where song.song_id = pc.song_id and pc.user_id = u.user_id and pc.Playlist_Index = 1;"
            cur_object.execute(q1)
            ls = cur_object.fetchall()
            return render_template("user.html", likedsongs = ls)
    except:
        disliked = dictresult['Disliked']
        q1 = "delete from playlist_contains where song_id = '" + disliked+ "' and user_id = '" + userid+ "' and playlist_index = 1;"
        cur_object.execute(q1)
        con.commit()
        q2 = q1 = "Select song.title, song.song_id from song, playlist_contains as pc, users as u where song.song_id = pc.song_id and pc.user_id = u.user_id and pc.Playlist_Index = 1;"
        cur_object.execute(q2)
        ls = cur_object.fetchall()
        return render_template("user.html", likedsongs = ls)    




if __name__ == '__main__':
    app.run(debug=True)
