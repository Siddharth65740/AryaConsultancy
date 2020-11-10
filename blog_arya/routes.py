from  flask import Flask,render_template,redirect,url_for,flash,request,jsonify
from blog_arya import app,db

@app.route("/")
def home():
    alpha_list=list=[chr(x) for x in range(65,91)]
    return render_template("index.html",title="Arya Consultancy",alpha_list=alpha_list)

@app.route("/community")
def community():

     return render_template("community.html",title="Arya Consultancy")

@app.route("/gyandeep")
def gyandeep():

     return render_template("gyandeep.html",title="Arya Consultancy")

@app.route("/hdp")
def hdp():

     return render_template("hdp.html",title="Arya Consultancy")

@app.route("/diy")
def diy():

     return render_template("DIY.html",title="Arya Consultancy")

@app.route("/lc")
def lc():

     return render_template("lc.html",title="Arya Consultancy")

@app.route("/aganwadi")
def aganwadi():

     return render_template("aganwadi.html",title="Arya Consultancy")

@app.route("/bridge")
def bridge():

     return render_template("bridgecourse.html",title="Arya Consultancy")

@app.route("/eep")
def eep():

     return render_template("eep.html",title="Arya Consultancy")

@app.route("/csr")
def csr():

     return render_template("csr.html",title="Arya Consultancy")

@app.route("/education")
def education():

     return render_template("Educationawarness.html",title="Arya Consultancy")

@app.route("/index")
def index():

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





