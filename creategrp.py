from flask import Flask,request,render_template,jsonify
import pandas as pd
import hashlib as hsh
import random as ran
app = Flask(__name__)

@app.route("/")
def main():
	return render_template("crtgrp.html")
	
@app.route("/add",methods=["GET","POST"])
def add():
	nm = request.form['nm']
	addgrp(nm)
	return jsonify({"status":"true"})
def addgrp(name):
	a = pd.read_csv("chatids.csv")
	a.loc[str(len(a["chatid"]))]=genhash(name)
	a.to_csv("chatids.csv",index=False)

def genhash(name):
	key = ["avy","okay","mobile","tuti","first","last","google"]
	ky = ran.choice(key)+str(ran.randint(1,1000))+name
	hs = hsh.sha256(ky.encode()).hexdigest()
	return hs
	
app.run()