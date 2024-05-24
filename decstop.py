from tkinter import *
from cv2_veniashvilly import main
import sys


class Main:
    def calculate(self):
        print('Hello world')

    def window(self):
        window = Tk()
        window.title('Сard recognition')
        window.geometry('400x300')

        frame = Frame( window, padx = 10, pady = 10 )
        frame.pack(expand=True)

        lbl_name = Label(frame, text='Card recognition App')
        lbl_name.grid(row = 1, column = 2)

        btn_start = Button(frame, text='Начать сканирование', command = main)
        btn_start.grid(row = 5 , column = 2)

        btn_instruction = Button(frame, text='Инструкция по использованию', command = self.calculate)
        btn_instruction.grid(row = 8 , column = 2)

        btn_quit = Button(frame, text='Выйти', command = sys.exit)
        btn_quit.grid(row = 10 , column = 2)


        window.mainloop()


if __name__ == "__main__":
    program = Main()
    program.window()