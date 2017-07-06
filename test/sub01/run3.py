# python run3.py runserver --host 0.0.0.0
# The web server should now be accessible from any computer in the network at http://
# a.b.c.d:5000, where “a.b.c.d” is the external IP address of the computer running the
# server.

from flask_script import Manager
from run import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
