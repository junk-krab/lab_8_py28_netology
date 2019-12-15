#https://github.com/netology-code/py-homework-basic/tree/master/2.4.files

with open("recipes.txt", encoding='utf8') as file:
    dishes = []
    cook_book = dict()

    for line in file:
        dish = line.strip()
        dishes.append(dish)
        person_count = int(file.readline())
        ingridients_list = []
        for line in file:
            if len(line) > 1:
                ingridient = dict()
                f = line.split("|")
                ingridient["ingridient_name"] = f[0]
                ingridient["quantity"] = int(f[1])
                ingridient["measure"] = f[2].strip()
                ingridients_list.append(ingridient.copy())
            else:
                break
        cook_book[dish] = ingridients_list
    print(cook_book)


    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        for dish in dishes:
            for ingridient in cook_book[dish]:
                new_shop_list_item = dict(ingridient)
                new_shop_list_item['quantity'] *= person_count
                if new_shop_list_item['ingridient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
        return shop_list


