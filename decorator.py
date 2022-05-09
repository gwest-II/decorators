from datetime import datetime


def make_log(func):

    def new_func(*args, **kwargs):
        log_date = datetime.today()
        res = func(*args, **kwargs)
        with open('logger.txt', 'w', encoding='UTF-8') as f:
            f.write(f'Дата и время вызова: {log_date}\n'
                    f'Имя: {func}\n'
                    f'Аргументы:{str(args)}, {str(kwargs)}\n'
                    f'Возвращаемое значение: {res}\n\n')
            res = func(*args, **kwargs)
        return res

    return new_func
