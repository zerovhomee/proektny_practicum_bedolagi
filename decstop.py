import tkinter as tk
from tkinter import font
from tkinter import scrolledtext
import sys
from cv2_veniashvilly import f
 



class Main:
    def window(self):
        window = tk.Tk()
        window["bg"] = "white"
        window.title('Сard recognition')
        window.geometry('1000x600')
        button_font = tk.font.Font(size = 16)
        instruction_font = tk.font.Font(size = 25)

        frame = tk.Frame(window, 
                         padx = 15, 
                         bg = "white")
        frame.grid(row = 0, 
                   column = 1, 
                   sticky = tk.W)
        
        command_frame = tk.Frame(window, 
                                 bg = "gray", 
                                 bd = 10, 
                                 highlightcolor = "white", 
                                 height = 500, 
                                 width = 600, 
                                 highlightthickness=20)
        
        command_frame.grid(row = 0, 
                           column = 0, 
                           ipadx = 60, 
                           ipady = 40)
        

        lbl_name = tk.Label(frame, 
                            text = 'Card recognition App')       
        lbl_name.grid(row = 0)       

        btn_start = tk.Button(frame, 
                              text='Начать сканирование',
                              font = button_font,
                              width = 20, 
                              height = 2, 
                              command = f)        
        btn_start.grid(row = 1, 
                       pady = 50)
        

        btn_instruction = tk.Button(frame, 
                                    text='''Инструкция по 
использованию''', 
                                    font = button_font,
                                    width = 20, 
                                    height = 2,
                                    command = lambda: self.view_instruction(command_frame, instruction_font))      
        btn_instruction.grid(row = 2, 
                             pady = 50)


        btn_quit = tk.Button(frame, 
                             text='Выйти',
                             font = button_font,
                             width = 20, 
                             height = 2, 
                             command = sys.exit)        
        btn_quit.grid(row = 3, 
                      pady = 50)
        
        window.mainloop()

    def view_instruction(self, window:tk.Tk, instruction_font):
        text_Label = tk.Label(window, text = """1. Для начала нажмите 
кнопку \"Начать сканирование\"\n\n
2. Далее, вы увидите в левом окне 
появится ваша камера. 
На ней будут распозноваться карточки\n\n
3. Для выхода из программы 
нажмите кнопку \"Выход\"""",
                               font = instruction_font,
                               bg = "gray",
                               foreground="white")
        
        text_Label.place(x=10, y=10)
        




if __name__ == "__main__":
    program = Main()
    program.window()