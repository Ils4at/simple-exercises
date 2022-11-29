#сумашедший сказочник
#Создает рассказ на основе пользовательского ввода
from tkinter import *


class Aplication(Frame):
    """GUI-приложение, создающее рассказ но основе пользовательского ввода"""
    def __init__(self, master):
        super(Aplication, self).__init__(master)
        self.grid()
        self.create_widget()


    def create_widget(self):
        """Создает элементыуправления, с помощтю которых пользователь будет вводит
        исходные данные и получать готовый рассказ"""
        Label(self,
              text="Введите данные для создания новоого рассказа"
              ).grid(row=0, column=0, sticky=W)
        Label(self,
              text="Имя человека:"
              ).grid(row=1, column=0, sticky=W)
        self.person_ent = Entry()
        self.person_ent.grid(row=1, column=1, sticky=W)
        Label(self,
              text="Существительное во мн.ч.:"
              ).grid(row=2, column=0, sticky=W)
        self.noun_ent = Entry()
        self.noun_ent.grid(row=2, column=1, sticky=W)
        Label(self,
              text="глагол в инфинитив:"
              ).grid(row=3, column=0, sticky=W)
        self.verb_ent = Entry()
        self.verb_ent.grid(row=3, column=1, sticky=W)
        Label(self,
              text="Прилагательное "
              ).grid(row=4, column=0, sticky=W)
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text="нетерпеливый",
                    variable=self.is_itchy,
                    ).grid(row=5, column=0, sticky=W)
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text="радостный",
                    variable=self.is_joyous,
                    ).grid(row=5, column=1, sticky=W)
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text="пронизывающий",
                    variable=self.is_electric,
                    ).grid(row=5, column=2, sticky=W)
        Label(self,
              text="Body part"
              ).grid(row=6, column=0, sticky=W)
        self.body_part = StringVar()
        self.body_part.set(None)
        body_parts = ["большой палец", "пупок", "продолговатый мозг"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text=part,
                        variable=self.body_part,
                        value=part,
                        ).grid(row=6, column=column, sticky=W)
            column += 1
        Button(self,
               text="Получить рассказ",
               command=self.tell_story
               ).grid(row=7, column=0, sticky=W)
        self.story_txt = Text(self, width=75, height=20, wrap=WORD)
        self.story_txt.grid(row=8, column=0, columnspan=4)

    def tell_story(self):
        """Заполняет текстовую область очередной историей на основе пользовательского ввода."""
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "нетерпеливый"
        if self.is_joyous.get():
            adjectives += "радостный"
        if self.is_electric.get():
            adjectives += "пронизывающий"
        body_part = self.body_part.get()
        #создание рассказа
        story = f"знаменитый путишественик {person} ужесовсем отчаялся довершить дело всей своей жизни - поиска " \
                f"затерянного города, в котором, по легенде обитали: {noun.title()}. Но однажд" \
                f" {noun} и {person} столкнулись лицом к лицу. Мощное {adjectives} ни с чем не сравнимое чуство" \
                f"охватило путишественника. После стольких лет поисков цель бфла наконец достигнута." \
                f"{person} ощутил, как на его {body_part} скатилась слезтнка. И тут внезапно" \
                f"{noun} перешли в атаку, и {person} был мгновенно ими сожран. Мораль? Если " \
                f"задумали {verb} надо делать это осторожно."
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)


root = Tk()
root.title("Секрет долгожителя")
app = Aplication(root)
root.mainloop()
