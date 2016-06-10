from lib.mvc import *
from src.views import *

if __name__ == "__main__":
    window = Window()
    window.set_title("Chausset")
    window.set_icon("favicon.ico")

    connection = ConnectBar(window)
    connection.pack()

    window.open()