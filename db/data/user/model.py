from py2neo import Node
from db.core import graph


class User:

    def __init__(self, user_id):
        self._node = Node(self.__class__.__name__, id=user_id)

    @property
    def id(self):
        return self._node.get('user_id')

    def save(self):
        graph.create(self._node)

    def __repr__(self):
        return '<User id={}>'.format(self.id)
