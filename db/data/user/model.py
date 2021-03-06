from py2neo import Node

from db.core import BaseModel


class User(BaseModel):

    def __init__(self, user_id):
        self._node = Node(self.node_label, id=user_id)

    @property
    def node(self):
        return self._node

    @property
    def id(self):
        return self._node.get('id')
