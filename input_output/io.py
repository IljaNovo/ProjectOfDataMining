import pandas
import requests
from numpy import array

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

    @staticmethod
    def get_ndarray_from_txt(path):
        text = Input.local_read_text_file(path)
        input_array = text.split('\n')
        float_array = []
        for line in input_array:
            float_line = [float(i) for i in line.split(' ')]
            float_array.append(float_line)
        X = array(float_array)
        return X


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

    @staticmethod
    def write_array_to_txt_file(filePath, array):
        try:
            with open(filePath, 'w', encoding='utf-8') as file2:
                for line in array:
                    file2.write(str(line)+"\n")
        except TimeoutError:
            print('Истекло время ожидания')
        except Exception:
            print('Неизвестная ошибка!')



