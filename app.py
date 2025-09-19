import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_url = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def hello_world():

    try:
        db.session.query(Test).all()
        return '<h1> Successs! Connected to DB!</h1>'
    except Exception as e:
        return f'<h1> Error! Could not connect to DB!</h1><p>{e}</p>'

if __name__ == '__main__':
    app.run(debug=True)