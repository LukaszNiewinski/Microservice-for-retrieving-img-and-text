# configure Flask CLI tool
from flask.cli import FlaskGroup
import project
import Model



cli = FlaskGroup(project.app)


@cli.command("create_db")
def create_db():
    Model.db.drop_all()
    Model.db.create_all()
    Model.db.session.commit()


if __name__ == "__main__":
    cli()
