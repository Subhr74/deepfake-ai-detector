from flask import Flask,request,jsonify
from flask_cors import CORS
import os
import sqlite3

from predict import predict_image
from video_predict import analyze_video
from gradcam import generate_heatmap
from database import init_db
from auth import generate_token

app=Flask(__name__)

CORS(app)

UPLOAD="uploads"
HEATMAP="heatmaps"

os.makedirs(UPLOAD,exist_ok=True)
os.makedirs(HEATMAP,exist_ok=True)

init_db()

@app.route("/signup",methods=["POST"])
def signup():

    data=request.json

    conn=sqlite3.connect("users.db")
    c=conn.cursor()

    c.execute("INSERT INTO users(username,password) VALUES(?,?)",
    (data["username"],data["password"]))

    conn.commit()
    conn.close()

    return jsonify({"msg":"user created"})

@app.route("/login",methods=["POST"])
def login():

    data=request.json

    conn=sqlite3.connect("users.db")
    c=conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?",
    (data["username"],data["password"]))

    user=c.fetchone()

    conn.close()

    if user:

        token=generate_token(data["username"])

        return jsonify({"token":token})

    return jsonify({"error":"invalid login"})

@app.route("/detect-image",methods=["POST"])
def detect_image():

    file=request.files["file"]

    path=os.path.join(UPLOAD,file.filename)

    file.save(path)

    result,prob=predict_image(path)

    heatmap=generate_heatmap(path)

    return jsonify({
    "result":result,
    "probability":prob,
    "heatmap":heatmap
    })

@app.route("/detect-video",methods=["POST"])
def detect_video():

    file=request.files["file"]

    path=os.path.join(UPLOAD,file.filename)

    file.save(path)

    result=analyze_video(path)

    return jsonify({"result":result})

if __name__=="__main__":

    app.run(debug=True)