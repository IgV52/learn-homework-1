"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
      try:
        n = (input("Как дела? ")).lower()
        while n != "хорошо":
          n=(input("Как дела? ")).lower()
        break
      except (KeyboardInterrupt):
        return print("Пока!")
    
if __name__ == "__main__":
    hello_user()
