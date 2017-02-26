from py2neo import Node

from db.core import BaseModel


class Story(BaseModel):

    def __init__(self, story_id):
        self._node = Node(self.nodel_label, id=story_id)

    @property
    def node(self):
        return self._node

    @property
    def id(self):
        return self._node.get('id')
