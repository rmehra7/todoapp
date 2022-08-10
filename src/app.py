from server.app_server import server
import sys, os
from flask import render_template

# Need to import all resources
from api.rest_endpoint import server
from api.web_endpoint import server

if __name__ == '__main__':
    server.run()
