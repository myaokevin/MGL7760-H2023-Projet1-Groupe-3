import os
from flask import Flask, render_template, request, url_for, redirect
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis',
              'CACHE_REDIS_URL': 'redis://cache:6379/0'})
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://user:user123@db:3306/flask_api"
db = SQLAlchemy(app)


class Livres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    isbn = db.Column(db.String(128))
    annee_apparition = db.Column(db.Integer)
    image = db.Column(db.String(128))
    auteur = db.Column(db.String(128))
    editeur = db.Column(db.String(256))
    categorie = db.Column(db.String(256))
    date_creation = db.Column(db.DateTime(timezone=True),
                              server_default=func.now())

    def __repr__(self):
         return f'<Livres {self.titre}>'

with app.app_context():
    db.create_all()
    db.session.add(Livres(titre='L’informatique répartie sous Unix',
                          description='',
                          isbn='0399-4198', annee_apparition='1992', image='', auteur='Michel Gabassi',
                          editeur='Bertrand Dupouy', categorie='EYROLLES,C,UNIX,Distributed Systems,Programming Languages,Programming'))

    db.session.commit()


@app.route("/")
@cache.cached(timeout=30, query_string=True)
def hello_world():
    livres = Livres.query.all()
    return render_template('index.html', livres=livres)


# @app.route("/biblio", methods=["GET", "POST"])
# def home():  # générer une page web qui affiche la liste de tous les livres disponibles dans la bibliothèque
    
#     db.session.commit()
#     livres = Livres.query.all()