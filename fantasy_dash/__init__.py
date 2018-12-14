from flask import Flask

app = Flask(__name__)

from fantasy_dash import routes
