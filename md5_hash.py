import hashlib
import os
from logger import decorator

'''
md5_hash v.2 из домашнего задания pypro_hw4 (https://github.com/zilon4eg/pypro_hw4.git)
'''

def md5_generator(path):
    '''
    Построчный генератор md5 hash из файла
    :param path: путь к файлу
    :return: md5 hash строки
    '''
    with open(os.path.join(os.getcwd(), path), encoding='utf-8') as file:
        for line in file:
            hash_object = hashlib.md5((line).encode())
            yield hash_object.hexdigest()


@decorator('log.txt')
def file_to_md5_file(path):
    '''
    Генерирует md5 hash из файла с помощью генератора md5_generator
    :param path: путь к файлу
    :return: список md5 hash из строк файла
    '''
    md5_hash = []
    for hash in md5_generator(path):
        md5_hash.append(hash)
    return md5_hash


if __name__ == '__main__':
    print(file_to_md5_file('data\countries_url.txt'))