from flask import Flask
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

import config
from model.abc import db
from service.fetch_data import FetchDataCommand

server = Flask(__name__)
server.debug = config.DEBUG
server.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db.init_app(server)

migrate = Migrate(server, db)
manager = Manager(server)
manager.add_command('db', MigrateCommand)
manager.add_command('fetch-stations-data', FetchDataCommand)

if __name__ == '__main__':
    manager.run()
