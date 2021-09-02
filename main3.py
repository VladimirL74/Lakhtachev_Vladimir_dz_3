

def thesaurus(*names):
    dict_of_names = {}
    for name in names:
        key = name[0].capitalize()
        if key not in dict_of_names:
            dict_of_names[key] = []
        dict_of_names[key].append(name)
    print(dict_of_names)


thesaurus("Сергей", "Алексей", "Владимир", "Владислав", "Борис", "Анастасия", "Ольга", "Наталья", "Александр")
