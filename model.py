db_list = []


def read_db(path: str) -> list:
    global db_list
    if len(db_list) == 0: #Проверка на непустоту телефонной книги для избежания повторной записи
        with open(path, 'r', encoding='UTF-8') as file:
            my_list = file.readlines()
            for line in my_list:
                id_dict = dict()
                line = line.strip().split(';')
                id_dict['lastname'] = line[0]
                id_dict['firstname'] = line[1]
                id_dict['phone'] = line[2]
                id_dict['comment'] = line[3]
                db_list.append(id_dict)
    else:
        print('Телефонная книга уже открыта')

#Добавленная часть
def write_db(path: str):
    with open(path, 'w', encoding='UTF-8') as file:
        for item in db_list:
            file.writelines('{};{};{};{}\n'.format(item['lastname'], item['firstname'], item['phone'], item['comment']))

#Конец добавленной части