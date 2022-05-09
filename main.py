from decorator import make_log
from decorator_with_path import make_log_path

if __name__ == '__main__':
    @make_log_path('path')    # Путь в формате: 'PycharmProjects', 'decorators', 'logger.txt'
    def summator(a, b):
        return a + b


    @make_log
    def summator_(a, b):
        return a + b



    # print(summator(4, 5))
    # print(summator_(4, 5))