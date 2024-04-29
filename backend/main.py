from flask import Flask, render_template, request, url_for, redirect, session, jsonify
import pymongo
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.secret_key = "testing"
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.get_database("ParkingLot")
user_records = db.users
booking_records = db.bookings


@app.route("/api/signup", methods=["post"])
def index():
    message = ""
    if request.method == "POST":
        user = request.json["fullname"]
        email = request.json["email"]

        password1 = request.json["password"]

        user_found = user_records.find_one({"name": user})
        email_found = user_records.find_one({"email": email})
        if user_found:
            message = "There already is a user by that name"
            return jsonify({"success": False, "message": message})
        if email_found:
            message = "This email already exists in database"
            return jsonify({"success": False, "message": message})
        else:
            user_input = {"name": user, "email": email, "password": password1}
            user_records.insert_one(user_input)

            user_data = user_records.find_one({"email": email})
            new_email = user_data["email"]
            return jsonify({"success": True, "email": new_email})


@app.route("/api/login", methods=["post"])
def login():
    if request.method == "POST":
        email = request.json["email"]
        password = request.json["password"]
        user = user_records.find_one({"email": email})
        print(email)
        print(password)
        if user:
            if user["password"] == password:
                print(user)
                return jsonify({"success": True})
            else:
                return jsonify({"success": False})
        else:
            return jsonify({"success": False})


@app.route("/api/book", methods=["post"])
def book():
    if request.method == "POST":
        location = request.json["location"]
        date = request.json["date"]
        time = request.json["time"]
        duration = request.json["duration"]
        user = request.json["user"]
        amount = request.json["amount"]
        vehicleType = request.json["vehicleType"]

        booking_input = {
            "location": location,
            "date": date,
            "time": time,
            "duration": duration,
            "amount": amount,
            "user": user,
            "vehicleType": vehicleType,
        }
        booking_records.insert_one(booking_input)
        return jsonify({"success": True})


# end of code to run it
if __name__ == "__main__":
    app.run(debug=True)
