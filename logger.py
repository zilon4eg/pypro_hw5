from _datetime import datetime


def limit_size_file(line_limit_size, path):
    '''
    Ограничивает количество строк в файле. Если строк больше чем line_limit_size, уяляет первые строки.
    :param line_limit_size: ограничение максимального количества строк в файле
    :param path: путь к файлу
    '''
    lines = 0
    with open(path, 'r', encoding='utf-8') as document:
        for line in document:
            lines += 1
    if line_limit_size >= lines:
        return
    else:
        temp = []
        with open(path, 'r', encoding='utf-8') as document:
            for line in document:
                temp.append(line)
        for count in range(lines - line_limit_size):
            temp.pop(0)
        with open(path, 'w', encoding='utf-8') as document:
            for element in temp:
                document.write(element)


def add_in_txt(text, path='noname.txt'):
    '''
    Дописывает текст в файл
    :param text: текст для записи
    :param path: путь и имя файла для записи
    '''
    with open(path, 'a', encoding='utf-8') as document:
        document.write(f'{text}' + '\n')


def decorator(log_path='log.txt', log_limit_size=50):
    '''
    Декоратор для сбора логов
    '''
    def decorator_(old_function):
        log = []
        log.append({'datetime': str(datetime.now())[:-7]})
        def new_function(*args, **kwargs):
            log.append({'name': old_function.__name__})
            log.append({'parameters': [args, kwargs]})

            result = old_function(*args, **kwargs)

            log.append({'result': result})
            add_in_txt(log, log_path)
            limit_size_file(log_limit_size, log_path)
            return result
        return new_function
    return decorator_