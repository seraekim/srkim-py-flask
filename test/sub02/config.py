import logging
import time
from flask_sqlalchemy import SQLAlchemy
from flask import g

fmt = '[%(levelname).1s] %(asctime)s.%(msecs)03d File "%(pathname)s", line %(lineno)d, in %(funcName)s, %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.DEBUG)


class Config:

    def __init__(self, app):
        self.app = app

        # log
        # self.app.debug = True

        formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

        stream_logger = logging.StreamHandler()
        stream_logger.setFormatter(formatter)
        file_logger = logging.FileHandler('logs/'+time.strftime('%Y-%m-%d') + '.log', mode='a', encoding='utf-8', delay=False)
        file_logger.setFormatter(formatter)
        self.app.logger.addHandler(stream_logger)
        self.app.logger.addHandler(file_logger)

        # db
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:init1234!@localhost:5433/test'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(app)

    def get_db_engine(self):
        return self.db.engine

    def get_logger(self):
        return self.app.logger

