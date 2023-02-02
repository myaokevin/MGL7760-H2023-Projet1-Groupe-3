from flask.cli import FlaskGroup

from project import db, User
from web import project


cli = FlaskGroup(project)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="yao@kevin.com"))
    db.session.commit()


if __name__ == "__main__":
    cli()
