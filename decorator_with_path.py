from datetime import datetime
import pathlib
from pathlib import Path

def make_log_path(*path):
    path_log = Path(pathlib.Path.home(), *path)

    def make_log_(func):

        def new_func(*args, **kwargs):
            log_date = datetime.today()
            res = func(*args, **kwargs)
            with open(path_log, 'w', encoding='UTF-8') as f:
                f.write(f'Дата и время вызова: {log_date}\n'
                        f'Имя: \n'
                        f'Аргументы:{str(args)}\n'
                        f'Возвращаемое значение: {res}\n\n')
                res = func(*args, **kwargs)
            return res

        return new_func

    return make_log_