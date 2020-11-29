from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# import dbData
# print(dbData.table)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Program Files (x86)\\SQLITE\\myDB.db'
Bootstrap(app)
db = SQLAlchemy(app)
engine = create_engine('sqlite:///C:\\Program Files (x86)\\SQLITE\\myDB.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


# Declare your  phone numbers table
class PNTable(Table):
    UserID = Col('UserID')
    phone_number = Col('phone_number')


# Declare your  emailtable
class EmailTable(Table):
    UserID = Col('UserID')
    email_address = Col('email_address')


# Declare your table
class UserTable(Table):
    UserID = Col('UserID')
    username = Col('username')
    password = Col('Password')


# Get some objects
class User(object):
    def __init__(self,  UserID, username, password):
        self.UserID = UserID
        self.username = username
        self.password = password


class Emails(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(255), unique=True, nullable=False)


class PhoneNumbers(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(255), unique=True, nullable=False)


emails = Emails.query.all()
emailTable = EmailTable(emails)


phone_numbers = PhoneNumbers.query.all()
pnTable = PNTable(phone_numbers)


class Users(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)


users = Users.query.all()
table = UserTable(users)
for user in users:
    print(str(user.UserID) + ' ' + user.username + ' ' + user.password)



# connects default URL of server to render home.html
# @app.route('/')
# def home_route():
#    return render_template("home.html")


# connects / path of server to render PaulN.html
@app.route('/', methods=["GET", "POST"])
def hello_route():
    # user = Users.query.filter_by(UserID=1).first()
    if request.form:
        print("UserID: " + str(request.form.get("ID")))
        email = Emails(email_address=request.form.get("email"), UserID=request.form.get("ID"))
        session.add(email)
        session.commit()
        phone_number = PhoneNumbers(phone_number=request.form.get("phone_number"), UserID=request.form.get("ID"))
        session.add(phone_number)
        session.commit()
    print("Home")
    return render_template("PaulN.html", table=table)


@app.route('/input/')
def input_route():
    return render_template("Input.html")


@app.route('/emails/')
def emails_route():
    # user = Users.query.filter_by(UserID=1).first()
    print("Emails")
    return render_template("PaulN.html", table=emailTable)


@app.route('/phones/')
def phones_route():
    # user = Users.query.filter_by(UserID=1).first()
    print("Phone Numbers")
    return render_template("PaulN.html", table=pnTable)


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)