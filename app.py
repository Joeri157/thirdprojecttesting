#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Import pre-requisites.                                                     #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from filestack import Client
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Connect to external MongoDB database                                       #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

client = Client("AYGc8VBXRTGi7hUQdYZnIz")


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Homepage                                                                   #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/")  # refers to the default route
@app.route("/index")
def index():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    uploads = list(
        mongo.db.uploads.find().sort("upload_time", -1))  # .limit(2)
    return render_template(
        "index.html", uploads=uploads, categories=categories)


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Registration                                                               #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        #  Registers new users to the db
        register = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        #  put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Sing Up Succesfull, {}".format(request.form.get("username")))
        return redirect(url_for("profile", username=["user"]))

    return render_template("register.html")


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Log In                                                                     #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/login", methods=["GET", "POST"])
def login():
    # check if username exists in db
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({
            "username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Profile                                                                    #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab's the session username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        uploads = list(mongo.db.uploads.find())
        return render_template(
            "profile.html", username=username, uploads=uploads)

    return redirect(url_for("login"))


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Log out                                                                    #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Add Upload                                                                 #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/add_upload", methods=["GET", "POST"])
def add_upload():
    categories = mongo.db.categories.find().sort("category_name", 1)
    if request.method == "POST":
        upload = {
            "category_name": request.form.get("catergory_name"),
            "upload_title": request.form.get("upload_title"),
            "upload_description": request.form.get("upload_description"),
            "upload_image": request.form.get("upload_image"),
            "upload_time": datetime.now().strftime("%Y-%m-%d, %H:%M"),
            "uploaded_by": session["user"]
            }
        mongo.db.uploads.insert_one(upload)
        flash("Congratulations {}, upload was succesfull!".format(
                session["user"]))
        return redirect(url_for("index"))

    return render_template("add_upload.html", categories=categories)


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Edit Upload                                                                #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/edit_upload/<id>", methods=["GET", "POST"])
def edit_upload(id):
    upload = mongo.db.uploads.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        mongo.db.uploads.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "category_name": request.form.get("catergory_name"),
                "upload_title": request.form.get("upload_title"),
                "upload_description": request.form.get("upload_description"),
                "upload_image": request.form.get("upload_image"),
                "upload_time": datetime.now().strftime("%Y-%m-%d, %H:%M"),
                "uploaded_by": session["user"]
            }}
        )
        flash(
            "Well done {},upload succesfully updated!".format(session["user"]))
        return redirect(url_for("index"))

    return render_template("edit_upload.html", upload=upload)


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Delete Upload                                                              #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/delete_upload/<id>")
def delete_upload(id):
    mongo.db.uploads.remove({"_id": ObjectId(id)})
    flash("Upload succesfully deleted")
    return redirect(url_for("index"))


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Add a comment                                                              #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/add_comment/<id>", methods=["GET", "POST"])
def add_comment(id):
    upload = mongo.db.uploads.find_one({"_id": ObjectId(id)})
    new_comment = {
        "comment_by": session["user"],
        "comment_time": datetime.now().strftime("%Y-%m-%d, %H:%M"),
        "comment_description": request.form.get("comment_description")
    }

    if request.method == "POST":
        mongo.db.uploads.update_one(
            {"_id": ObjectId(id)},
            {"$push": {"comments": new_comment}}
        )
        flash(
            "Comment succesfully added, {}".format(session["user"]))
        return redirect(request.referrer)

    return render_template(request.referrer, upload=upload)


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Edit Comment                                                               #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/edit_comment/<id>", methods=["GET", "POST"])
def edit_comment(id):
    if request.method == "POST":
        mongo.db.uploads.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"comments": [{
                "comment_by": session["user"],
                "comment_time": datetime.now().strftime("%Y-%m-%d, %H:%M"),
                "comment_description": request.form.get(
                    "comment_description")}]}})
        flash("Comment succesfully changed")
        return redirect(request.referrer)
    return redirect(request.referrer)


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Delete Comment                                                             #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/delete_comment/<id>")
def delete_comment(id):
    mongo.db.uploads.update_one(
        {"_id": ObjectId(id)},
        {"$pull": {"comments": {
            "comment_by": session["user"]}}})
    flash("Comment succesfully deleted")
    return redirect(request.referrer)


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Categories                                                                 #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/all_categories")
def all_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("all_categories.html", categories=categories)


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Browse categories                                                          #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/category_page/<category_name>", methods=["GET"])
def category_page(category_name):
    uploads = mongo.db.uploads.find({"category_name": category_name})
    return render_template("category.html", uploads=uploads)


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Upload on a single page                                                    #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/upload_page/<id>", methods=["GET", "POST"])
def upload_page(id):
    upload = mongo.db.uploads.find_one({"_id": ObjectId(id)})
    return render_template("upload.html", upload=upload)


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Search                                                                     #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    uploads = list(mongo.db.uploads.find({"$text": {"$search": query}}))
    return render_template("index.html", uploads=uploads)


#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #
#  Development/Production environment test for debug                          #
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  #

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# return to debug=false when actual deployment / project submit.
