# python run_script.py runserver --host 0.0.0.0 --threaded

from app_name import app
from flask_script import Manager
manager = Manager(app)

if __name__ == '__main__':
    manager.run()

