from hw05_easy import *


def utility():
    answer = ''
    current_folder = os.getcwd()

    while answer != '5':

        answer = input('Выберите пункт меню:\n'
                       '1. Перейти в папку\n'
                       '2. Просмотреть содержимое текущей папки\n'
                       '3. Удалить папку\n'
                       '4. Создать папку\n'
                       '5. Выход\n')
        if answer == '5':
            break

        elif answer == '4':
            dir_name = input("Введите название создаваемой директории: ")
            print('Новая папка создана')
            create(os.path.join(current_folder, dir_name))

        elif answer == '3':
            dir_name = input("Введите название директории, которую желаете удалить: ")
            delete(os.path.join(current_folder, dir_name))

        elif answer == '2':
            files()
            print(current_folder)

        elif answer == '1':
            dir_name = input('В какую директорию перейти?')
            if change_dir(dir_name):
                print('Перешли в директорию {}'.format(current_folder))
            else:
                print('Переход не удался')


if __name__ == '__main__':
    utility()
