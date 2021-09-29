def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Andrés", "lastname": "Garcia"}

    super_list = [
        {"firstname": "Andrés", "lastname": "Rozo"},
        {"firstname": "Camilo", "lastname": "Vanegas"},
        {"firstname": "Amaparo", "lastname": "Rozo"},
        {"firstname": "Gloria", "lastname": "Vanegas"},
        {"firstname": "Facundo", "lastname": "Garcia"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 2.2, 3.3, 4.4, 5.5]
    }

    print("super_list:")
    for i in super_list:
        for key, values in i.items():
            print(key,": ", values);

    print("super_dicts:")
    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == '__main__':
    run()