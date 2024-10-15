from flask import Flask

from models import Faculty
from database import session

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/add_faculty/<string:name>/<float:finances>')
def add_faculty(name, finances):
    f = Faculty(name=name, finances=finances)
    session.add(f)
    session.commit()


