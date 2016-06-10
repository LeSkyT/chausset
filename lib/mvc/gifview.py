import tkinter
from PIL import Image, ImageTk, ImageSequence
from time import sleep
import threading


class GifView(tkinter.Label):
    def __init__(self, master, image_path):
        super(GifView, self).__init__(master)
        self._image = Image.open(image_path)
        self._animation_thread = GifAnimation(self, self._image)
        self._animation_thread.start()

    def __del__(self):
        self._animation_thread.stop()


class GifAnimation(threading.Thread) :
    def __init__(self, canvas, image):
        super(GifAnimation, self).__init__()
        self._stop = threading.Event()
        self._canvas = canvas
        self._image = image

    def stop(self):
        self._stop.set()
        return self

    def is_running(self):
        return not self._stop.is_set()

    def run(self):
        while self.is_running():
            for frame in ImageSequence.Iterator(self._image):
                if not self.is_running():
                    break
                img = ImageTk.PhotoImage(frame)
                self._canvas.config(image=img)

                sleep(frame.info["duration"] / 1000)
