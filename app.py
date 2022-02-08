import os,sys,json, time, sqlalchemy

from flask import Flask, session,request,jsonify,redirect,url_for,abort,render_template,flash
from functools import wraps
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
from sqlalchemy.sql.expression import cast
from sqlalchemy import create_engine
from flask_table import Table, col

app = Flask(__name__)
app.secret_key ="kichu1739 "

# Check for environment variable
if not os.getenv("postgres://yzeeqrtrugucvb:9f14029371dc4742b2aabdeba4ce82468536eef4c5da208d18b60bb09af29686@ec2-184-73-243-101.compute-1.amazonaws.com:5432/d7c0g2ejfkih3q"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False 
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("postgres://yzeeqrtrugucvb:9f14029371dc4742b2aabdeba4ce82468536eef4c5da208d18b60bb09af29686@ec2-184-73-243-101.compute-1.amazonaws.com:5432/d7c0g2ejfkih3q"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
    if __name__ == "__main__":
        app.run(debug=True)

@app.route("/")
def login_page():
    return render_template("Signin.html")
@app.route("/Signup")
def Signup():
    return render_template("Signup.html")
@app.route("/books", methods=["POST","GET"])
def book_search():
    if request.method=="POST":
        username=request.form.get("username_login")
        password=request.form.get("password_login")if username=="" or password=="":
        return render_template("error.html", message="Your password or username field is empty. please, return again and correct your faults.", type_error="login")


out_id=db.execute("select id from users where username=:username and password=:password",{"username":username,"password":password})
if out_id.rowcount==0:
    return render_template("error.html", message="Your password or username is not correct or may be you don't have an account. please, return back and correct your faults.", type_error="login")

        if(not("user_id" in session)):
            session["user_id"]=[]
            print("add new data to session")
        new_id=out_id.fetchone()[0]
       
        if ((len(session["user_id"])>0 and new_id!=session["user_id"][-1]) or (len(session["user_id"])==0)):
            session["user_id"].append(new_id)
        print(f"session now ={session['user_id']}")
        db.commit()
         return render_template("book_search_page.html",search_flag=0,books_list=[])



