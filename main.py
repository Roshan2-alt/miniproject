from flask import Flask, render_template, request, url_for, redirect, session,jsonify
import pymongo
import bcrypt

app = Flask(__name__)
app.secret_key = "testing"
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.get_database('total_records')
records = db.register

@app.route("/api/signup", methods=['post'])
def index():
    message = ''
    if "email" in session:
        return redirect(url_for("logged_in"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        
        password1 = request.form.get("password")
        
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return jsonify({"success": False, "message": message})
        if email_found:
            message = 'This email already exists in database'
            return jsonify({"success": False, "message": message})
        else:
            user_input = {'name': user, 'email': email, 'password': password1}
            records.insert_one(user_input)
            
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            return jsonify({"success": True, "email": new_email})
        
@app.route("/api/login", methods=['post'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = records.find_one({"email": email})
        print(user)
        print(password)
        if user:
            if user['password'] == password:
                print(user)
                return jsonify({"success": True})
            else:
                return jsonify({"success": False})
        else:
            return jsonify({"success": False})

#end of code to run it
if __name__ == "__main__":
  app.run(debug=True)