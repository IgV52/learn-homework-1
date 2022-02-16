"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    lot_list = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    
    total_summ_all_phone = 0
    average_total_sell_all_phone = 0
    info_sell = []
    for i in lot_list:
        for value in i.values():
            if isinstance(value, str):
                model = value
            if isinstance(value, list):
                lot_items = [i for i in value]
                sum_lot_sell_model = 0
                average_lot_sell_model = 0
                for sold in lot_items:
                    sum_lot_sell_model += sold
                total_summ_all_phone += sum_lot_sell_model
                average_lot_sell_model = sum_lot_sell_model / len(lot_items)
                average_total_sell_all_phone += average_lot_sell_model
                info_sell.append(f"Сумма всех проданных телефонов {model} : {sum_lot_sell_model} их среднее количество продаж {average_lot_sell_model}")
    info_sell.append(f'Сумма всех проданных телефонов {total_summ_all_phone} и их среднее количество продаж {average_total_sell_all_phone}')
    return print(*info_sell, sep = "\n")


  
if __name__ == "__main__":
    main()
