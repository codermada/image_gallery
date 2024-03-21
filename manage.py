from flask_script import Manager, Shell
from flask_migrate import Migrate, init, upgrade, migrate

from app import create_app, db
from app.models import Image, Description

app = create_app('devConfig')
manager = Manager(app)
migration = Migrate(app, db)


def shell_context():
    return dict(db=db, Image=Image, Description=Description)

def migration_context():
    return dict(i=init, u=upgrade, m=migrate)

manager.add_command('shell', Shell(make_context=shell_context))
manager.add_command('db', Shell(make_context=migration_context))

if __name__ == '__main__':
    manager.run()
