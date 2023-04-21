from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def jukebox():
    return render_template("index.html")

@app.route('/fetch',methods = ['POST', 'GET'])
def fetch():
    result = request.form
    print(result)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)