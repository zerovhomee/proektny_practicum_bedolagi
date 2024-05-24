from tkinter import *
from cv2_veniashvilly import main


class Main:
    def window(self):
        root = Tk()
        root.title('My App')
        lbl1 = Label(root, text='Привет')
        lbl1.grid(column=0, row=0)
        lbl1.place(x=10,y=10)
        btn1 = Button(root, text='Не нажимай', command = main)
        btn1.place(x= 10 ,y= 50)


        root.mainloop()


if __name__ == "__main__":
    program = Main()
    program.window()