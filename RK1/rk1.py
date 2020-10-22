from operator import itemgetter
import re

class File:
    """Файл"""
    def __init__(self, id, name, size, dir_id):
        self.id = id
        self.name = name
        self.size = size
        self.dir_id = dir_id

class Dir:
    """Каталог файлов"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class FileDir:
    """Файлы в каталогах"""
    def __init__(self, dir_id, file_id):
        self.dir_id = dir_id
        self.file_id = file_id

# Каталоги
dirs = [
    Dir(1, 'Архитектура'),
    Dir(2, 'универ'),
    Dir(3, 'за день до конца света'),
    Dir(22, 'абиотическое разнообразие'),

    Dir(11, 'Архив странных фото'),
    Dir(33, 'избранное жить'),
]

# Файлы
files = [
    File(1, 'супрематические примитивы', 165, 1),
    File(2, 'рк', 142, 2),
    File(3, 'я не помню когда это было', 100, 3),
    File(4, 'Мультиагентный вентилятор', 210, 3),
    File(5, 'многомерный скотч', 175, 3),
    File(5, 'клеточный пожиратель', 201, 22),
    File(5, 'пластмассовый мир', 110, 22),
]

files_dirs = [
    FileDir(1,1),
    FileDir(2,2),
    FileDir(3,3),
    FileDir(3,4),
    FileDir(3,5),
    FileDir(22,2),

    FileDir(11,1),
    FileDir(33,3),
    FileDir(33,4),
    FileDir(33,5),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [(f.name, f.size, d.name)
        for d in dirs
        for f in files
        if f.dir_id==d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, fd.dir_id, fd.file_id)
        for d in dirs
        for fd in files_dirs
        if d.id==fd.dir_id]

    many_to_many = [(f.name, f.size, dir_name)
        for dir_name, dir_id, file_id in many_to_many_temp
        for f in files if f.id==file_id]

    print('Задание А1')
    res_11 = {}
    selected_dirs = [one_dir[2] for one_dir in one_to_many if one_dir[2].startswith('а') or one_dir[2].startswith('А')]
    for dir_name in selected_dirs:
        files_in_dir = [(one_file[0],one_file[1]) for one_file in one_to_many if one_file[2]==dir_name]
        res_11.update({dir_name:files_in_dir})
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    for d in dirs:
        d_files = list(filter(lambda i: i[2]==d.name, one_to_many))
        if len(d_files) > 0:
            d_sizes = [size for _,size,_ in d_files]
            d_size_max = max(d_sizes)
            res_12_unsorted.append((d.name, d_size_max))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    dirs.sort(key=lambda one_dir: one_dir.name)

    for d in dirs:
        d_files = list(filter(lambda i: i[2]==d.name, many_to_many))
        d_files_names = [x for x,_,_ in d_files]
        res_13[d.name] = d_files_names

    print(res_13)

if __name__ == '__main__':
    main()

