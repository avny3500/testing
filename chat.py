from flask import render_template,Flask,json,jsonify,redirect,url_for,request

import pandas as pd
app = Flask(__name__)
@app.route("/")
def main():
	return render_template("chat2.html")
	
@app.route("/cht/<iid>",methods=['GET','POST'])
def chat(iid):
	if request.method == "POST":
		msg = request.form['msg']
		reply = msg
		if msg == "/bot":
			
		dct = {"reply":reply}
	return jsonify(dct)

@app.route("/webhook")
def hook():
	pass
app.run()
