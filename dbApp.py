from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col


# import dbData
# print(dbData.table)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Program Files (x86)\\SQLITE\\myDB.db'
Bootstrap(app)
db = SQLAlchemy(app)


# Declare your table
class ItemTable(Table):
    UserID = Col('UserID')
    username = Col('username')
    password = Col('Password')


# Get some objects
class Item(object):
    def __init__(self,  UserID, username, password):
        self.UserID = UserID
        self.username = username
        self.password = password


class Users(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)


users = Users.query.all()
table = ItemTable(users)
for user in users:
    print(str(user.UserID) + ' ' + user.username + ' ' + user.password)



# connects default URL of server to render home.html
# @app.route('/')
# def home_route():
#    return render_template("home.html")


# connects /hello path of server to render PaulN.html
@app.route('/')
def hello_route():
    user = Users.query.filter_by(UserID=1).first()
    print(user.username)
    return render_template("PaulN.html", table=table)


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)