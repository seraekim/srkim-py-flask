import decimal, datetime, json, logging, time
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from werkzeug.wsgi import LimitedStream


class Stream(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, env, res):
        stream = LimitedStream(env['wsgi.input'], int(env.get('CONTENT_LENGTH') or 0))
        env['wsgi.input'] = stream
        app_iter = self.app(env, res)
        try:
            stream.exhaust()
            for event in app_iter:
                yield event
        finally:
            if hasattr(app_iter, 'close'):
                app_iter.close()


class DB:

    exec = None
    mongo = None
    def __init__(self, app):
        app.wsgi_app = Stream(app.wsgi_app)

        file_logger = logging.FileHandler('logs/' + time.strftime('%Y-%m-%d') + '.log', mode='a', delay=False)
        app.logger.addHandler(file_logger)

        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/bpkias'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        app.config['MY_OWN_DB_DBNAME'] = 'dbname'

        db = SQLAlchemy(app)
        # DB.session = db.session
        DB.exec = db.engine.execute
        DB.mongo = PyMongo(app, config_prefix='MY_OWN_DB')


    # @classmethod
    # def execute(cls, sql):
    #     return cls.exec(sql)


def to_json(res, is_str=True):
    def encoder(obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
    # f = open('test.txt', 'w')
    if is_str:
        return json.dumps([dict(r) for r in res], default=encoder, ensure_ascii=False)
    else:
        return json.loads(json.dumps([dict(r) for r in res], default=encoder, ensure_ascii=False))

