import pandas
import requests


class Input:
    # Чтение csv таблиц из интернета
    # url - адрес файла в интернете
    @staticmethod
    def internet_read_csv(url):
        print('Чтение CSV с ' + url + '...')
        try:
            return pandas.read_csv(url)
        except TimeoutError:
            print('Истекло время ожидания')
        except Exception:
            print('Неизвестная ошибка!')

    # Чтение csv таблиц из файла
    @staticmethod
    def local_read_csv(file_path):
        print('Чтение CSV из ' + file_path + '...')
        try:
            return pandas.read_csv(file_path, index_col=None)
        except TimeoutError:
            print('Истекло время ожидания')
        except Exception:
            print('Неизвестная ошибка!')

    # Чтение текстовых файлов с компьютера
    @staticmethod
    def local_read_text_file(file_path):
        print('Чтение данных из ' + file_path)
        try:
            file2 = ""
            with open(file_path, 'r', encoding='utf-8') as file1:
                for line in file1:
                    file2 = file2 + str(line)
            return file2
        except TimeoutError:
            print('Истекло время ожидания')
        except Exception:
            print('Неизвестная ошибка')

    # Чтение текстовых файлов из интернета
    @staticmethod
    def internet_read_text_file(url):
        print('Чтение данных с ' + url)
        try:
            return requests.get(url).text
        except TimeoutError:
            print('Истекло время ожидания')
        except Exception:
            print('Неизвестная ошибка!')


class Output:
    @staticmethod
    def write_to_txt_file(filePath, file1):
        try:
            with open(filePath, 'w', encoding='utf-8') as file2:
                file2.write(str(file1))
        except TimeoutError:
            print('Истекло время ожидания')
        except Exception:
            print('Неизвестная ошибка!')

    @staticmethod
    def write_to_csv_file(filePath, csvTable):
        try:
            csvTable.to_csv(filePath)
        except TimeoutError:
            print('Истекло время ожидания')
        except Exception:
            print('Неизвестная ошибка!')


class InputTestStub:
    @staticmethod
    def local_read_csv():
        print(Input.local_read_csv('C:\\Users\\vladimir.kornilov\\Desktop\\LessonPython\\data\\example_table.csv'))

    @staticmethod
    def internet_read_csv():
        return Input.internet_read_csv('https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv')

    @staticmethod
    def internet_read_text_file():
        return Input.internet_read_text_file(
            'https://raw.githubusercontent.com/mhyhre/Tuxis-Input-Module/master/README.rdoc')

    @staticmethod
    def local_read_text_file():
        return Input.local_read_text_file('C:\\Users\\vladimir.kornilov\\Desktop\\LessonPython\\data\\text.txt')


class OutPutTestStub:
    @staticmethod
    def write_to_txt(file1):
        Output.write_to_txt_file('csv.txt', file1)

    @staticmethod
    def write_to_csv(csv):
        Output.write_to_csv_file('table.csv', csv)
