from py2neo import Node
from .core import graph


class User(Node):

    def __init__(self, user_id):
        self._node = Node.__init__(self.__class__.__name__, id=user_id)

    @property
    def id(self):
        return self._node.get('user_id')

    def save(self):
        graph.create(self._node)

    def __repr__(self):
        return '<User id={}>'.format(self.id)
