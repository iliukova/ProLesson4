import dish
import category
import menu

dish_1 = dish.Dish('Страва 1', 100)
dish_2 = dish.Dish('Страва 2', 101)
dish_3 = dish.Dish('Страва 3', 102)
dish_4 = dish.Dish('Страва 4', 103)
dish_5 = dish.Dish('Страва 5', 104)
dish_6 = dish.Dish('Страва 6', 105)
dish_7 = dish.Dish('Страва 7', 106)
dish_8 = dish.Dish('Страва 8', 107)
dish_9 = dish.Dish('Страва 9', 108)
dish_10 = dish.Dish('Страва 10', 109)

cat_1 = category.Category('Основні страви')
cat_1.add_dish(dish_1)
cat_1.add_dish(dish_2)
cat_1.add_dish(dish_3)
cat_1.add_dish(dish_4)
cat_1.add_dish(dish_5)

cat_2 = category.Category('Перші страви')
cat_2.add_dish(dish_6)
cat_2.add_dish(dish_7)
cat_2.add_dish(dish_8)
cat_2.add_dish(dish_9)
cat_2.add_dish(dish_10)

menu = menu.Menu()
menu.add_category(cat_1)
menu.add_category(cat_2)

print(menu)
