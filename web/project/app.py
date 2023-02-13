import os
from flask import Flask, render_template, request, url_for, redirect,jsonify
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://cache:6379/0'})
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://user:user123@db:3306/flask_api"
db = SQLAlchemy(app)

class Auteur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(128), nullable=False)

class Editeur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(128), nullable=False)

class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(128), nullable=False)
    nom = db.Column(db.String(128), nullable=False)

class Livres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(128), nullable=False)
    auteur = db.Column(db.String(128)) #, nullable=False) #foreign key db.ForeignKey('Auteur.id')
    editeur = db.Column(db.String(128)) #, nullable=False) #foreign key  db.ForeignKey('Editeur.id')
    description = db.Column(db.String(500)) #, nullable=False)
    isbn = db.Column(db.String(128)) #, nullable=False)
    annee_apparition = db.Column(db.Integer) #, nullable=False)
    image = db.Column(db.String(128))
    categorie = db.Column(db.String(128)) #, nullable=False) #foreign key db.ForeignKey('Categorie.id')
    date_creation = db.Column(db.DateTime) #, nullable=False)
    date_modification = db.Column(db.DateTime) #, nullable=False)

    def __repr__(self, titre):
        self.titre = titre



with app.app_context():
    db.create_all()
    sql="""
INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('The Pragmatic Programmer', '', '135957052', '2019', '', '"David Thomas', 'Andrew Hunt"','Addison Wesley,Programming
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Learning Python', '', '978-1-449-35573-9', '2013', '', 'Mark Lutz', 'O’REILLY','"Programming Languages,Python"
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('HTTP The Definitive Guide', '', '978-1-56592-509-0', '2002', '', '"David Gourley', 'Brian Totty"','O’REILLY,Web
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('High-Performance Client/Server', '', '0-471-16269-8', '1998', '', '"Chris Loosley', 'Frank Douglas"','Wiley,Distributed Systems
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Operating Systems', '', '0-13-638677-6', '1997', '', '"Andrew S. Tanenbaum', 'Albert S. Woodhull"','Prentice Hall,Operating Systems
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Concurrent Systems', '', '0-321-11788-3', '2003', '', 'Jean Bacon', 'Addison Wesley','"Operating Systems,Distributed Systems,Databases"
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('The Art of Multiprocessor Programming', '', '978-0-12-415950-1', '2121', '', '"M. Herlihy', 'V. Luchangco','N. Shavit,M.Spear",MK,Programming
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Think Python', '', '978-1-491-93936-9', '2016', '', 'Allen B. Downey', 'O’REILLY','"Programming Languages,Python"
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Data Structures in Java', '', '0-201-30564-X', '1998', '', 'Thomas A. Standish', 'Addison Wesley','"Data Structures,Java,Programming"
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Data Abstraction and Problem Solving with Java', '', '0-201-70220-7', '2001', '', '"Frank M.Carrano', 'Janet J. Prichard"','Addison Wesley,"Data Structures,Java,Programming"
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Advanced Data Structures', '', '978-1-108-73551-3', '2019', '', 'Peter Brass', 'Cambridge','Data Structures
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Fundamentals of Data Structures', '', '0-914894-20X', '1976', '', '"E. Horowitz', 'S. Sahni"','Pitman,Data Structures
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Computer Algorithms', '', '0-201-06035-3', '1988', '', 'Sara Baase', 'Addison Wesley','Algorithms
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Algorithms Unlocked', '', '978-0-262-51880-2', '2013', '', 'Thomas H. Cormen', 'The MIT Press','Algorithms
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Introduction to Algorithms', '', '978-0-262-04630-5', '2022', '', '"Thomas H. Cormen', 'Charles E. Leiserson','Ronald L. Rivest,Clifford Stein",The MIT Press,Algorithms
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Programming', '', '978-0-321-99278-9', '2014', '', 'Bjarne Stroustrup', 'Addison Wesley','"Programming,C++,Programming Languages"
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Programming Rust', '', '978-1-492-05259-3', '2021', '', '"Jim Blandy', 'Jason Orendorff','Leonora F. S. Tindall",O’REILLY,"Rust,Programming Languages,Programming"
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Foundations of Computer Science', '', '0-7167-8233-2', '1992', '', '"Alfred V. Aho', 'Jeffrey D. Ullman"','Computer Science Press,Computer Science
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Computer Science', '', '978-0-13-407642-3', '2017', '', '"Robert Sedgewick', 'Kevin Wayne"','Addison Wesley,Computer Science
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Compilers', '', '0-201-10088-6', '1988', '', '"Alfred V. Aho', 'Ravi Sethi','Jeffrey D. Ullman",Addison Wesley,Compilers
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Advanced Programming in the UNIX Environment', '', '0-201-56317-7', '1999', '', 'W. Richard Stevens', 'Addison Wesley','"C,UNIX,Programming Languages,Programming"
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Fundamentals of Data Structures in C', '', '9780-929306-40-7', '2008', '', '"E. Horowitz', 'S. Sahni','S. Anderson-Freed",Silicon Press,"Data Structures,C"
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Le Langage C', '', '978-2-10-071577-0', '2014', '', '"Brian W. Kernighan', 'Dennis M. Ritchie"','Dunod,"C,Programming Languages,Programming"
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Advanced C', '', '0-672-48417-X', '1988', '', '"Paul Anderson', 'Gail Anderson"','Hayden Books,"C,Programming Languages,Programming"
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('Topics in C Programming', '', '0-672-46290-7', '1987', '', '"Stephen G. Kochan', 'Patrick H. Wood"','Hayden Books,"C,Programming Languages,Programming"
' );

INSERT INTO Livres (titre, description, isbn, annee_apparition, image, auteur, editeur, categorie)
VALUES ('L’informatique répartie sous Unix', '', '0399-4198', '1992', '', '"Michel Gabassi', 'Bertrand Dupouy"','EYROLLES,"C,UNIX,Distributed Systems,Programming Languages,Programming"
' ); """
    
    db.session.execute(sql)

    db.session.commit()

    # db.session.add(User('admin', 'admin@example.com'))
    # db.session.add(User('guest', 'guest@example.com'))
    # db.session.commit()

    # users = User.query.all()


   # print(users)



@app.route("/")
@cache.cached(timeout=30, query_string=True)
def hello_world():
    # livres = Livres.query.all()
    return jsonify(hello='hello')


# @app.route("/biblio", methods=["GET", "POST"])
# def home(): #générer une page web qui affiche la liste de tous les livres disponibles dans la bibliothèque
#     livres = Livres.query.all()
#     return render_template ('biblio.html', livres=livres)


#@app.route('/biblio/<int:id>')
#def afficher_details(id): #afficher details pour livre choisi
 #   livre = Livres.query.get(id)

