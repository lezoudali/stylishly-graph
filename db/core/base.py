from abc import ABCMeta, abstractproperty

from .graph import graph


class BaseModel:
    __metaclass__ = ABCMeta

    @abstractproperty
    def node(self):
        pass

    @property
    def node_label(self):
        return self.__class__.__name__

    def save(self):
        graph.create(self.node)

    def __repr__(self):
        return '<{}>'.format(self.node_label)
