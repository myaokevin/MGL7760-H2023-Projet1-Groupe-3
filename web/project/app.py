import os
from flask import Flask, render_template, request, url_for, redirect,jsonify
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://user:user1234@db:3307/flask_api"
db = SQLAlchemy(app)

class Livres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(128), nullable=False)
    auteur = db.Column(db.Integer) #, nullable=False) #foreign key
    editeur = db.Column(db.Integer) #, nullable=False) #foreign key
    description = db.Column(db.String(500)) #, nullable=False)
    isbn = db.Column(db.String(128)) #, nullable=False)
    annee_apparition = db.Column(db.Integer) #, nullable=False)
    image = db.Column(db.String(128))
    categorie = db.Column(db.Integer) #, nullable=False) #foreign key
    date_creation = db.Column(db.DateTime) #, nullable=False)
    date_modification = db.Column(db.DateTime) #, nullable=False)

    def __repr__(self, titre):
        self.titre = titre

@app.route("/")
def hello_world():
    return jsonify(hello="world")




