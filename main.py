from flask import Flask, render_template
from flask import request
import requests
import smtplib


app = Flask(__name__)
response = requests.get("https://api.npoint.io/5808b1a3304a496f4c65")
api = response.json()

@app.route("/")
def home():
    return render_template("index.html",data=api)

@app.route("/about")
def about_section():
    return render_template("about.html")

@app.route("/contact")
def contact_section():
    return render_template("contact.html")

@app.route("/form-entry",methods=["POST"])
def login():
    name = request.form["username"]
    email = request.form["mailid"]
    phone = request.form["cell"]
    message = request.form["mess"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_id, password=password)
        connection.sendmail(from_addr=email_id, to_addrs="harshavibodkhe@gmail.com",
                            msg=f"Subject:New Visitor :)\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}")
    return '<h1>Successfully Sent. Thanks for visiting!</h1>'


@app.route("/post/<int:num>")
def post_section(num):
    return render_template("post.html",data=api,id=num)


email_id = "lily21042002@gmail.com"
password = "lfcseehyhcqgjhzh"





if __name__ == "__main__":
    app.run(debug=True)
