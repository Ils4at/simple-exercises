#Меню ресторана
#Пользователю показываеться несложнноеменю ресторана
from tkinter import *


class Aplication(Frame):
    """GUI приложение где пользователю будет выводиться меню ресторана"""
    def __init__(self, master):
        super(Aplication, self).__init__(master)
        self.grid()
        self.draw_widget()

    def draw_widget(self):
        """Создаем элементы управления, с помощью которых пользователь будет выбирать блюда из меню и получать счет"""
        Label(self,
              text="Первые блюда"
              ).grid(row=0, column=0, sticky=W)
        Label(self,
              text="Лапша по домашнему"
              ).grid(row=1, column=0, sticky=W)
        self.ramen = BooleanVar()
        Checkbutton(self,
                    text="150",
                    variable=self.ramen
                    ).grid(row=1, column=1, sticky=W)
        Label(self,
              text="Борщь"
              ).grid(row=2, column=0, sticky=W)
        self.borch = BooleanVar()
        Checkbutton(self,
                    text="160",
                    variable=self.borch
                    ).grid(row=2, column=1, sticky=W)
        Label(self,
              text="Солянка"
              ).grid(row=3, column=0, sticky=W)
        self.solynka = BooleanVar()
        Checkbutton(self,
                    text="120",
                    variable=self.solynka
                    ).grid(row=3, column=1, sticky=W)
        Label(self,
              text="Вторые блюда"
              ).grid(row=4, column=0, sticky=W)
        Label(self,
              text="Плов"
              ).grid(row=5,  column=0, sticky=W)
        self.plov = BooleanVar()
        Checkbutton(self,
                    text="229",
                    variable=self.plov
                    ).grid(row=5, column=1, sticky=W)
        Label(self,
              text="Манты"
              ).grid(row=6, column=0, sticky=W)
        self.mantu = BooleanVar()
        Checkbutton(self,
                    text="340",
                    variable=self.mantu
                    ).grid(row=6, column=1, sticky=W)
        Label(self,
              text="Десерт на выбор"
              ).grid(row=7, column=0, sticky=W)
        #переключатель между десертами
        self.dessert = StringVar()
        self.dessert.set(None)
        desserts = [['шоколадный брауни', 120], ['Капкейки', 343], ['Чизкейк', 123]]
        column = 0
        for item in desserts:
            i = 0
            j = 1
            Radiobutton(self,
                        text=item[i],
                        variable=self.dessert,
                        value=item[j]
                        ). grid(row=8, column=column, sticky=W)
            column += 1
        #кнопка отсылки данных
        Button(self,
               text="Расчитать заказ",
               command=self.order
               ).grid(row=9, column=0, sticky=W)
        self.order_acc = Text(self, width=35, height=10, wrap=WORD)
        self.order_acc.grid(row=10, column=0, columnspan=9)

    def order(self):
        """заполняет текстовую область суммой заказ."""
        adjectives = 0
        if self.ramen.get():
            adjectives += 150
        if self.borch.get():
            adjectives += 160
        if self.solynka.get():
            adjectives += 130
        if self.plov.get():
            adjectives += 229
        if self.mantu.get():
            adjectives += 340
        dessert = self.dessert.get()
        self.order_acc.delete(0.0, END)
        self.order_acc.insert(0.0, f"Стоимость ваша заказа состовляет {adjectives + int(dessert)}")

root = Tk()
root.title("Меню ресторана")
app = Aplication(root)
root.mainloop()
