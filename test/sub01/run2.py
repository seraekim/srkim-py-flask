# Flask context globals
"""
Variable name | Context             | Description
current_app   | Application context | The application instance for the active application.
g             | Application context | An object that the application can use for temporary storage
              |                     | during the handling of a request. This variable is reset with each request.
request       | Request context     | The request object, which encapsulates the contents of
              |                     | a HTTP request sent by the client.
session       | Request context     | The user session, a dictionary that the application can use
              |                     | to store values that are “remembered” between requests.

"""
from flask import current_app
from run import app

# name = current_app.name # RuntimeError: Working outside of application context.
app_ctx = app.app_context()
app_ctx.push()
name = current_app.name
# app_ctx.pop() # RuntimeError: Working outside of application context.
print(current_app.name)
app_ctx.pop()

url_map = app.url_map
print(url_map)

