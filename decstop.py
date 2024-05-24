from tkinter import *
from cv2_veniashvilly import main
''''
root = Tk()
root.title('My App') #заголовок
lbl1 = Label(root, text='Привет')
lbl1.grid(column=0, row=0)
lbl1.place(x=10,y=10)

def clicked():
    root = Tk()
    root.title('My App') #заголовок
    lbl1 = Label(root, text='Я же сказал...')
    lbl1.grid(column=0, row=0)
    lbl1.place(x=10,y=10)

btn1 = Button(root, text='Не нажимай', command = clicked)
btn1.place(x= 10 ,y= 50)



if __name__ == '__main__':
  #выполнение кода до загрузки
  root.mainloop() #отображение окна
  '''

class Main:
    def __init__(self):
        self.cv2_main = self.cv2_veniashvilly.main()

    def main():
        self.cv2_main()

if __name__ == "__main__":
    main = Main()
    main.main()