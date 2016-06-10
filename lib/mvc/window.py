import os
import tkinter
from os.path import dirname, sep

from src.views.connectbar import ConnectBar

class Window(tkinter.Frame):
    def __init__(self):
        self._parent = tkinter.Tk()
        super(Window, self).__init__(self._parent)
        self._prepare_env()

    def _prepare_env(self):
        path = dirname(dirname(dirname(__file__)))
        os.chdir(path)
        return self


    def set_title(self, title):
        self._parent.title(title)
        return self

    def set_icon(self, icon):
        path = os.curdir + sep + icon
        self._parent.iconbitmap(path)
        return self


    def set_view(self, view):
        if self._view is not None:
            del self._view
        assert isinstance(view, object)
        self._view = view

    def open(self):
        self.pack()
        self._parent.mainloop()


__all__ = ["Window"]