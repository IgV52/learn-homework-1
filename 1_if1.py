"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age_user = int(input("Сколько вам лет?: "))
    if 0 < age_user < 7:
      return print("Вы должны быть в детском саду")
    elif 7 <= age_user < 18:
      return print("Вы должны быть в школе")
    elif 18 <= age_user < 24:
      return print("Вы должны быть в ВУЗе")
    else:
      return print("Вы должны уже работать")

if __name__ == "__main__":
    main()
