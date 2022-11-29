#Отгадай число
#Игроку нужно отгадать число которое загадал компьютер
from tkinter import *
import random


the_number = int(random.randint(1, 101))

class Aplication(Frame):
    """GUI-приложение загадывающее число"""
    def __init__(self, master):
        super(Aplication, self).__init__(master)
        self.grid()
        self.draw_widget()


    def draw_widget(self):
        Label(self,
              text="отгадайте число которое загадал  компьютер"
              ).grid(row=0, column=0, sticky=W)
        Label(self,
              text="Компьютер загадал число от 1 до 100, введите число в поле ниже"
              ).grid(row=1, column=0, sticky=W)
        self.number_ent = Entry()
        self.number_ent.grid(row=2, column=0, sticky=W)
        Button(self,
               text="проверить число",
               command=self.right
               ).grid(row=3, column=0, sticky=W)
        self.message = Text(width=30, height=5, wrap=WORD)
        self.message.grid(row=4, column=0, sticky=W)

    def right(self):
        number = int(self.number_ent.get())
        string = ""
        if number > the_number:
            string = "Загаданное число меньше"
            self.message.delete(0.0, END)
            self.message.insert(0.0, string)
        elif number < the_number:
            string = "Загаданное число больше"
            self.message.delete(0.0, END)
            self.message.insert(0.0, string)
        elif number == the_number:
            string = "Поздравляю вы отгадали число"
            self.message.delete(0.0, END)
            self.message.insert(0.0, string)
        else:
            string = "Я не знаю таких параметров"
            self.message.delete(0.0, END)
            self.message.insert(0.0, string)


root = Tk()
root.title("Секрет долгожителя")
app = Aplication(root)
root.mainloop()
