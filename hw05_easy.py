import os
import sys
import shutil
# Задание-1:


def directory():
    answer = ''

    while answer != '3':

        answer = input('Выберите пункт меню:\n'
                       '1. Создать папки dir_1 - dir_9\n'
                       '2. Удалить папки dir_1 - dir_9\n'
                       '3. Выход\n')
        if answer == '3':
            break
        if answer == '1':
            for i in range(1, 10):
                dir_path = os.path.join(os.getcwd(), f'dir_{i}')
                print(dir_path)
                try:
                    os.mkdir(dir_path)
                except FileExistsError:
                    print('Такая директория уже существует')
        elif answer == '2':
            for i in range(1, 10):
                dir_path = os.path.join(os.getcwd(), f'dir_{i}')
                print(dir_path)
                try:
                    os.rmdir(dir_path)
                except FileExistsError:
                    print('Такой директории не существует')


if __name__ == '__main__':
    directory()


# Задание-2:


with os.scandir(path='.') as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_dir():
            print(entry.name)


# Задание-3:


source_full_name = sys.argv[0]
source_name = source_full_name[:-3]
source_extension = source_full_name[-3:]
new_file = source_name + '_copy' + source_extension
shutil.copy(source_full_name, new_file)


# functions #


def create(path):
    try:
        os.mkdir(path)
    except OSError:
        print("Создать директорию не удалось")
    else:
        print("Успешно создана директория ")


def delete(path):
    if os.path.isfile(path):
        os.remove(path)
    if os.path.isdir(path):
        os. rmdir(path)

def files(dummy):
    dirs = os.listdir(path=os.getcwd())
    print(dirs)


def change_dir(dir_name):
    try:
        os.chdir(dir_name)
        print('Текущая директория {}'.format(os.getcwd()))
    except FileNotFoundError:
        print('Не удалось перейти в директорию {}'.format(dir_name))


def full_path(dummy):
    path = os.getcwd()
    print(path)


def ping(dummy):
    print("pong")


def copy_file(file_name):
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_name_copy = str("copy_" + file_name)
    file_path = os.path.join(os.getcwd(), file_name_copy)
    with open(file_name) as inp:
        with open(file_path, 'w') as out:
            out.write(inp.read())


def print_help(dummy):
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - копия файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> сменить директорию на указанную")
    print("ls - отображение списка файлов")
    print("pwd - отображение полного пути текущей директории")