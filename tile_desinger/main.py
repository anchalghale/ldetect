''' Main script of tile designer '''
import tkinter as tk

import pygubu


class Application:
    ''' The tkinter application class '''

    def __init__(self, root):
        self.builder = builder = pygubu.Builder()
        self.builder.add_from_file('gui.ui')
        self.builder.connect_callbacks(self)
        self.mainwindow = builder.get_object('main_frame', root)
        root.title('Tile Designer')
        root.geometry('640x480+0+480')


def main():
    ''' Main function of the script '''
    root = tk.Tk()
    Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
