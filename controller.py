import model
import view

def input_handler(inp: int):
    match inp: 
        case 1:
            view.show_all(model.db_list)
        case 2:
                model.read_db('database.txt')
                view.db_success(model.db_list)
        case 3:
            model.write_db('database.txt')
        case 4:
            model.db_list.append(view.create_contact())
        case 5:
            view.change_contact(model.db_list)
        case 6:
            view.delete_contact(model.db_list)
        case 7:
            view.find_contact(model.db_list)
        case 8:
            view.exit_program()



while True:
    user_inp = view.main_menu()
    input_handler(user_inp)