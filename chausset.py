import ChaussetUI

class Chausset:
    def __init__(self):
        self._set_gui(ChaussetUI.ChaussetUI())
        self._set_socket(None)

    def _set_gui(self, gui):
        self._gui = gui
        return self

    def _set_socket(self, socket):
        self._socket = socket
        return self

    def run(self):
        self._gui.open()

if __name__ == "__main__":
    app = Chausset()
    app.run()
