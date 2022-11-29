# нужно написать число на английском
import random


NUMBERS = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
           'eleven', 'twelve', 'thirteen', 'fourteen', ' fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
           'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six',
           'twenty-seven', 'twenty-eight', 'twenty-nine', 'thirty', 'thirty-one', 'thirty-two', 'thirty-three',
           'thirty-four', 'thirty-five', 'thirty-six', 'thirty-seven', 'thirty-eight', 'thirty-nine', 'forty',
           'forty-one', 'forty-two', 'forty-three', 'forty-four', 'forty-five', 'forty-six', 'forty-seven',
           'forty-eight', 'forty-nine', 'fifty', 'fifty-one', 'fifty-two', 'fifty-three', 'fifty-four', 'fifty-five',
           'fifty-six', 'fifty-seven', 'fifty-eight', 'fifty-nine', 'sixty', 'sixty-one', 'sixty-two', 'sixty-three',
           'sixty-four', 'sixty-five', 'sixty-six', 'sixty-seven', 'sixty-eight', 'sixty-nine', 'seventy',
           'seventy-one', 'seventy-two', 'seventy-three', 'seventy-four', 'seventy-five', 'seventy-six',
           'seventy-seven', 'seventy-eight', 'seventy-nine', 'eighty', 'eighty-one', 'eighty-two', 'eighty-three',
           'eighty-four', 'eighty-five', 'eighty-six', 'eighty-seven', 'eighty-eight', 'eighty-nine', 'ninety',
           'ninety-one', 'ninety-two', 'ninety-three', 'ninety-four', 'ninety-five', 'ninety-six', 'ninety-seven',
           'ninety-eight', 'ninety-nine', 'one hundred')

ORDINAL_NUMBERS = ('first', 'second', 'third', 'fourth', 'fifth', 'sixth', ' seventh', 'eighth', 'ninth', 'tenth',
                   'eleventh', 'twelfth', 'thirteenth', 'fourteenth', ' fifteenth', 'sixteenth', 'seventeenth',
                   'eighteenth', 'nineteenth', 'twentieth', 'twenty-first', 'twenty-second', 'twenty-third',
                   'twenty-fourth', 'twenty-fifth', 'twenty-sixth', 'twenty-seventh', 'twenty-eighth', 'twenty-ninth',
                   'thirtieth', 'thirty-first', 'thirty-second', 'thirty-third', 'thirty-fourth', 'thirty-fifth',
                   'thirty-sixth', 'thirty-seventh', 'thirty-eighth', 'thirty-ninth', 'fortieth', 'forty-first',
                   'forty-second', 'forty-third', 'forty-fourth', 'forty-fifth', 'forty-sixth', 'forty-seventh',
                   'forty-eighth', 'forty-ninth', 'fiftieth', 'fifty-first', 'fifty-second', 'fifty-third',
                   'fifty-fourth', 'fifty-fifth', 'fifty-sixth', 'fifty-seventh', 'fifty-eighth', 'fifty-ninth',
                   'sixtieth', 'sixty-first', 'sixty-second', 'sixty-third', 'sixty-fourth', 'sixty-fifth',
                   'sixty-sixth', 'sixty-seventh', 'sixty-eighth', 'sixty-ninth', 'seventieth', 'seventy-first',
                   'seventy-second', 'seventy-third', 'seventy-fourth', 'seventy-fifth', 'seventy-sixth',
                   'seventy-seventh', 'seventy-eighth', 'seventy-ninth', 'eightieth', 'eighty-first', 'eighty-second',
                   'eighty-third', 'eighty-fourth', 'eighty-fifth', 'eighty-sixth', 'eighty-seventh', 'eighty-eighth',
                   'eighty-ninth', 'ninetieth', 'ninety-first', 'ninety-second', 'ninety-third', 'ninety-fourth',
                   'ninety-fifth', 'ninety-sixth', 'ninety-seventh', 'ninety-eighth', 'ninety-ninth', 'hundredth')

num = []
for i in range(1, 101):
    num.append(i)
random.shuffle(num)


def exercise(a):
    for item in num:
        print(f"напишите по английски {item}")
        answer = input("введите свой ответ: ")
        if answer == a[item - 1]:
            print("правильно следующее число")
        else:
            print(f"неправильно, правильно пишетсься {a[item - 1]}")


print("Добро пожаловать в программу для тренировки написания чисел по английскому"
      "На выбор можно выбрать либо счет до 100 или просто цифры до 100 ")

choice = None

while choice != "0":
    choice = input("""Для начала выберите что хотите повторить:
    1. Цифры до 100
    2. Порядковые числительные до 100
    3. Выход
    
    Ваш выбор:  """)
    if choice == "1":
        exercise(NUMBERS)
    elif choice == "2":
        exercise(ORDINAL_NUMBERS)
    elif choice == "0":
        print("Конец упражнения надеюсь вам было полезно!!")
    else:
        print("Я не знаю такого ответа проверьте правильность!")
input("Нажмите интер для выхода")
