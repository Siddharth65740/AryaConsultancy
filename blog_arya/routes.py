from  flask import Flask,render_template,redirect,url_for,flash,request,jsonify
from blog_arya import app,db

@app.route("/")
def home():
    alpha_list=list=[chr(x) for x in range(65,91)]
    return render_template("index.html",title="Arya Consultancy",alpha_list=alpha_list)

@app.route("/dashboard")
def Dashboard():

    return render_template("index.html",title="Arya Consultancy")

@app.route("/about")
def About():

    return render_template("index.html",title="Arya Consultancy")

# @app.route("/")
#
# def index():
#
#     msg = Message("Hello",
#                   sender="siddharth24092001@gmail.com")





