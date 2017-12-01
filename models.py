from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}/{}?ssl_key={}&ssl_cert={}'\
    .format(config.USERNAME, config.PASSWORD, config.HOST, config.DATABASENAME, config.SSL_KEY_PATH,
            config.SSL_CERT_PATH)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)


class Corporation(db.Model):
    CorporationID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=True, nullable=False)
    CreateTime = db.Column(db.DateTime, nullable=False)
    UpdateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ClinicKey = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Corporation %r>' % self.Name


class Branch(db.Model):
    CorporationID = db.Column(db.Integer, db.ForeignKey('corporation.CorporationID'), nullable=False)
    BranchID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=True, nullable=False)
    CreateTime = db.Column(db.DateTime, nullable=False)
    UpdateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ClinicBranchList = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Branch %r>' % self.Name
