from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

#PROFILE
class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(20),unique=True)
    mobile = db.Column(db.String(10), unique=True)
    country = db.Column(db.String(15))
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, name, mobile, country, email, username, password):
        self.name = name
        self.mobile = mobile
        self.country = country
        self.email = email
        self.username = username
        self.password = password

class ProfileSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    mobile = fields.String(required=True)
    country = fields.String(required=True)
    email = fields.String(required=True)
    username = fields.String(required=True)

#WALLET
class Wallet(db.Model):
    __tablename__ = 'wallets'
    id = db.Column(db.Integer, primary_key=True)
    profileID = db.Column(db.Integer, db.ForeignKey('profiles.id', onupdate='CASCADE', ondelete='CASCADE'))
    totalbalance = db.Column(db.Integer)
    list_of_coin = db.Column(db.String(150))

    def __init__(self, profileID, totalbalance, list_of_coin={}):
        self.profileID = profileID
        self.totalbalance = totalbalance
        self.list_of_coin = list_of_coin

class WalletSchema(ma.Schema):
    id = fields.Integer()
    profileID = fields.Integer()
    totalbalance = fields.Integer()
    list_of_coin = fields.String()
