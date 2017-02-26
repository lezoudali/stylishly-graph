import os

from py2neo import Graph


USERNAME = os.environ['STYLISHLY_GRAPH_USERNAME']
PASSWORD = os.environ['STYLISHLY_GRAPH_PASSWORD']
DB_URL = os.environ['STYLISHLY_GRAPH_URL']


graph = Graph(DB_URL, username=USERNAME, password=PASSWORD)
