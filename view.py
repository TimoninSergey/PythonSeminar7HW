def main_menu() -> int:
    print('Главное меню.')
    menu_list = [
    'Показать все контакты',
    'Открыть файл',
    'Сохранить файл',
    'Создать контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Найти контакт',
    'Выход'
    ]
    for i in range(len(menu_list)):
        print(f'    {i+1}. {menu_list[i]}')
    user_input = int(input('Введите команду : '))
    return user_input

def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()

def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False


def exit_program():
    print('Завершение программы')
    exit()

def create_contact():
    print('Создание нового контакта.')
    new_contact = dict()
    new_contact['lastname'] = input('    Введите фамилию: ')
    new_contact['firstname'] = input('    Введите имя: ')
    new_contact['phone'] = input('    Введите телефон: ')
    new_contact['comment'] = input('    Введите комментарий: ')
    return new_contact

#Добавленная часть
def find_contact(db: list):
    find_item = input('Введите нужное в поиск: ')
    for i in range(len(db)):
        if find_item in db[i].values():
            for v in db[i].values():
                print(f'{v}', end=' ')
                print()

def change_contact(db: list):
    contact = input('Какой контакт вы хотите изменить? Введите фамилию, имя или номер: ')
    contact_list = []
    for i in range(len(db)):
        if contact in db[i].values():
            index = 0
            contact_list.append((index, db[i]))
            print(index)
            for v in db[i].values():
                print(f'{v}', end=' ')
            index = index + 1
    changing_contact = int(input('Введите номер изменяемого контакта: '))
    cont_for_change = contact_list[changing_contact][1]
    cont_for_change['lastname'] = input('    Введите новую фамилию: ')
    cont_for_change['firstname'] = input('    Введите новое имя: ')
    cont_for_change['phone'] = input('    Введите новый телефон: ')
    cont_for_change['comment'] = input('    Введите новый комментарий: ')

def delete_contact(db: list):
    contact = input('Какой контакт вы хотите удалить? Введите фамилию, имя или номер: ')
    contact_list = []
    for i in range(len(db)):
        if contact in db[i].values():
            index = 0
            contact_list.append((index, db[i]))
            print(index)
            for v in db[i].values():
                print(f'{v}', end=' ')
            index = index + 1
    deleting_contact = int(input('Введите номер удаляемого контакта: '))
    cont_for_delete = contact_list[deleting_contact][1]
    db.remove(cont_for_delete)
    
#Конец добавленной части