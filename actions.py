from flask import Flask

import models
from models import Faculty, Departments
from database import session
from sqlalchemy import select

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/add_faculty/<string:name>/<float:finances>')
def add_faculty(name, finances):
    f = Faculty(name=name, finances=finances)
    try:
        session.add(f)
        session.commit()
    except:
        session.rollback()
        return f'faculty {name} almost exist'
    return f'faculty {name} added'

@app.route('/change_faculty/<string:oldname>/<string:newname>/<float:finances>')
def change_faculty(oldname, newname, finances):
    stmt = select(Faculty).where(Faculty.name==oldname)
    f = session.scalars(stmt).one()
    f.name = newname
    f.finances = finances
    session.add(f)
    session.commit()
    return f'faculty {oldname} changed to {newname}'

if __name__ == '__main__':
    app.run()

