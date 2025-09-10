from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Atlas connection (replace with your connection string)
client = MongoClient("mongodb+srv://sarthakjadhav4848:vbEp6MZz1byJlmls@cluster0.v7ho4.mongodb.net/?retryWrites=true&w=majority")
db = client["testdb"]
collection = db["formdata"]

# API route: return JSON data from file
@app.route("/api")
def get_data():
    with open("data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

# Frontend form route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]

            # Insert into MongoDB
            collection.insert_one({"name": name, "email": email})

            return redirect(url_for("success"))
        except Exception as e:
            return render_template("form.html", error=str(e))

    return render_template("form.html")

# Success page
@app.route("/success")
def success():
    return "Data submitted successfully"

if __name__ == "__main__":
    app.run(debug=True)
