from flask import current_app as app, g
# from .app import conf
from utils import utils
engine = None


def set_engine(e):
    global engine
    engine = e


def create():
    pass


def read():
    # engine = g.conf.get_db_engine()
    q = '''
    select * from user_agent 
    order by 1'''
    return utils.to_json(engine.execute(q))

def update():
    pass

def delete():
    pass


