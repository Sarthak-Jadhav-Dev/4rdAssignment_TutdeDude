from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (make sure MongoDB is running on your system)
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]        # Database name
collection = db["todo_items"] # Collection name

@app.route("/")
def home():
    # Render the To-Do form
    return render_template("todo.html")

@app.route("/submittodoitem", methods=["POST"])
def submittodoitem():
    # Get data from form (POST request)
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    # Store in MongoDB
    todo_item = {
        "itemName": item_name,
        "itemDescription": item_description
    }
    collection.insert_one(todo_item)

    return jsonify({"message": "To-Do item saved successfully!", "data": todo_item})

if __name__ == "__main__":
    app.run(debug=True)
