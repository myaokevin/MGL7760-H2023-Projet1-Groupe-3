import os
from flask import Flask, render_template, request, url_for, redirect,jsonify
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://cache:6379/0'})
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://user:user123@db:3306/flask_api"
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
with app.app_context():
    db.create_all()

    # db.session.add(User('admin', 'admin@example.com'))
    # db.session.add(User('guest', 'guest@example.com'))
    # db.session.commit()

    # users = User.query.all()
    # print(users)

@app.route("/")
@cache.cached(timeout=30, query_string=True)
def hello_world():
    livres = Livres.query.all()
    return jsonify(livres)




