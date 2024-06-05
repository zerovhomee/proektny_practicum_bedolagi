from tkinter import *
from cv2_veniashvilly import f
import sys


class Main:
    def calculate(self):
        print('Hello world')

    def window(self):
        window = Tk()
        window["bg"] = "gray"
        window.title('Сard recognition')
        window.geometry('500x500')

        frame = Frame(window, padx = 100, pady = 200)
        frame.grid(column = 1)

        lbl_name = Label(frame, text = 'Card recognition App')    #Ы   
        lbl_name.grid(row = 0, column = 0, sticky = N)       

        btn_start = Button(frame, text='Начать сканирование', command = f)        
        btn_start.grid(row = 30, column = 0)
        

        btn_instruction = Button(frame, text='Инструкция по использованию', command = self.calculate)       
        btn_instruction.grid(row = 50 , column = 0)


        btn_quit = Button(frame, text='Выйти', command = sys.exit)        
        btn_quit.grid(row = 70 , column = 0)


        window.mainloop()


if __name__ == "__main__":
    program = Main()
    program.window()