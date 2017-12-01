from flask import Flask, render_template
from models import *
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def corporation():
    print datetime.now()
    admin = Corporation(Name='admin', ClinicKey=54, CreateTime=datetime.now())
    db.session.add(admin)
    db.session.commit()
    return render_template('corporation.html')


@app.route('/branch')
def branch():
    return render_template('branch.html')

if __name__ == '__main__':
    db.init_app(app)
    app.run()