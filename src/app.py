import sys, os
from flask import render_template

# Need to import all resources
from server.app_server import server
from api.rest_endpoint import server as rest_api_server
from api.web_endpoint import server as web_api_server

if __name__ == '__main__':
    server.run()
