import tkinter
import application


class TkinterWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('640x480')


def main():
    window = TkinterWindow()
    app = application.Calculator(window)
    app.pack(fill='both', expand=1, padx=10, pady=10)
    app.mainloop()


if __name__ == '__main__':
    main()
