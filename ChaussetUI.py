import tkinter, os


class ChaussetUI(tkinter.Frame):
    def __init__(self):
        self.parent = tkinter.Tk()
        self._set_menubar()
        self._set_icon()
        self.parent.title("Chausset 1.0 Pré-Alpha - Les bonnes sockets TCP")

        super(ChaussetUI, self).__init__(self.parent)

    def open(self):
        self.parent.mainloop()

    def _set_icon(self):
        icon = os.path.dirname(__file__) + os.path.sep + 'favicon.ico'
        self.parent.iconbitmap(icon)
        return self

    def _set_menubar(self):
        self._menubar = tkinter.Menu(self.parent)
        self.parent.config(menu=self._menubar)

        connectionMenu = tkinter.Menu(self._menubar)
        connectionMenu.add_command(label="Connection", command=self._connect)
        self._menubar.add_cascade(label="Start", menu=connectionMenu)

        return self

    def _connect(self):
        connection = tkinter.Toplevel()
        connection.title("Se connecter à :")

        msg = tkinter.Label(connection, text="Veuillez sélectionner les coordonnées à contacter.")

        host_entry = tkinter.Entry(connection)
        host_entry.insert(0, "Host")

        port_entry = tkinter.Entry(connection)
        port_entry.insert(0, "Port")

        def validate():
            print("connect to : " + host_entry.get() + ":" + port_entry.get())

        validate_button = tkinter.Button(connection, text="Connection", command=validate)

        msg.grid(row=0, columnspan=2)
        host_entry.grid(row=1, column=0)
        port_entry.grid(row=1, column=1)

        validate_button.grid(row=2, column=1)

        return self