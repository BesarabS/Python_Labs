#Замовлення
orders = ["Піцца",
          "Салат",
          "Бургер",
          "Паста"]
orders.append("Суп")
del orders[1]
orders_slice = orders[1:4]

#Категорії
categories = ("Напої",
              "Супи",
              "Основні страви",
              "Десерти")
selected_category = categories[2]

#Інгредієнти
available_ingredients = {"помідор", "огірок", "сир", "шинка", "салат"}
available_ingredients.add("базилік")
required_ingredients = {"помідор", "огірок", "олія", "часник"}
common_ingredients = available_ingredients.intersection(required_ingredients)
missing_ingredients = required_ingredients.difference(available_ingredients)

#Ціни страв
menu = {"Піцца": 120,
        "Салат": 80,
        "Бургер": 100,
        "Паста": 110}
menu["Суп"] = 90
menu["Бургер"] = 105
del menu["Салат"]
order_items = ["Піцца",
               "Бургер",
               "Суп"]
total_price = sum(menu[item] for item in order_items)

def show_results():
    print("Замовлення:", orders)
    print("Частина замовлення:", orders_slice)
    print("Категорія:", selected_category)
    print("Наявні інгредієнти:", available_ingredients)
    print("Спільні інгредієнти:", common_ingredients)
    print("Відсутні інгредієнти:", missing_ingredients)
    print("Меню:", menu)
    print("Загальна вартість замовлення:", total_price)

if __name__ == "__main__":
    show_results()