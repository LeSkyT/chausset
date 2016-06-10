import abc


class Controller:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._view = None

    def _set_view(self, view):
        self._view = view
