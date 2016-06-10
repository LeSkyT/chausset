import abc
import tkinter


class View(tkinter.Frame):
    __metaclass__ = abc.ABCMeta

    def __init__(self, master=None):
        super(View, self).__init__(master)
        self._vars = {}
        if isinstance(master, View):
            for (instance, value) in master._get_vars():
                self[instance] = value

    def _set_view(self, view):
        self._view = view

    def __set__(self, instance, value):
        self._vars[instance] = value
        return self

    def __get__(self, instance, owner):
        return self._vars[instance]

    def _get_vars(self):
        return self._vars

    def __del__(self):
        # TODO: Implement me
        yield None

