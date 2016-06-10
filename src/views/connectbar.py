import os
import tkinter

from lib.mvc import *


class ConnectBar(View):
    def __init__(self, master):
        super(ConnectBar, self).__init__(master)
        self.config(width=600, height=25)
        self.master = master
        self._host = None
        self._port = None
        self._connected = False

        self._connect_layout()

    def _connect_layout(self):
        host_msg = tkinter.Label(self, text="Host : ")
        host_input = tkinter.Entry(self)
        port_msg = tkinter.Label(self, text="Port : ")
        port_input = tkinter.Entry(self)
        go_button = tkinter.Button(self, text="Connect.")

        host_msg.grid(row=0, column=0)
        host_input.grid(row=0, column=1)
        port_msg.grid(row=0, column=2)
        port_input.grid(row=0, column=3)
        go_button.grid(row=0, column=4)

        host_input.focus_set()

        def connect():
            self._host = host_input.get()
            self._port = port_input.get()

            img_path = os.curdir + os.path.sep + "Imgs" + os.path.sep + "loading.gif"
            loading_msg = tkinter.Label(self, text="Connecting to host %s on port %s ..." % (self._host, self._port))
            loading = GifView(self, img_path)

            host_msg.destroy()
            host_input.destroy()
            port_msg.destroy()
            port_input.destroy()
            go_button.destroy()

            loading.grid(row=0, column=0)
            loading_msg.grid(row=0, column=1)

        go_button.config(command=connect)

__all__ = ["ConnectBar"]