"""
Selector module provides high usability interface to lxml tree
"""
import logging
from abc import ABCMeta, abstractmethod

from selection.selector_list import SelectorList

__all__ = ('SelectorInterface',)
XPATH_CACHE = {}
logger = logging.getLogger('grab.selector.selector')
metaclass_ABCMeta = ABCMeta('metaclass_ABCMeta', (object, ), {})


class SelectorInterface(metaclass_ABCMeta):
    __slots__ = ('_node',)

    def __init__(self, node):
        self._node = node

    def select(self, query):
        return self._wrap_node_list(self.process_query(query), query)

    def _wrap_node_list(self, nodes, query):
        selector_list = []
        for node in nodes:
            selector_list.append(self.__class__(node))
        return SelectorList(selector_list, self.__class__, query)

    @abstractmethod
    def is_text_node(self):
        "Not implemented"

    @abstractmethod
    def html(self):
        "Not implemented"

    @abstractmethod
    def attr(self):
        "Not implemented"

    @abstractmethod
    def text(self):
        "Not implemented"

    @abstractmethod
    def number(self):
        "Not implemented"

    @abstractmethod
    def rex(self):
        "Not implemented"
