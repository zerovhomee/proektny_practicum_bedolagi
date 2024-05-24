from tkinter import *


root = Tk()
root.title('My App') #заголовок
lbl1 = Label(root, text='Привет')
lbl1.grid(column=0, row=0)
lbl1.place(x=10,y=10)

def clicked():
    print('Я же сказал...')

btn1 = Button(root, text='Не нажимай', command = clicked)
btn1.place(x= 10 ,y= 50)



if __name__ == '__main__':
  #выполнение кода до загрузки
  root.mainloop() #отображение окна