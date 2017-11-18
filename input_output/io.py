import pandas
import requests
from numpy import array
import numpy as np
import csv
import scipy as sp
from numpy.core import multiarray

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
    @staticmethod
    def load_csv_for_classification(inputFilePath):
        with open(inputFilePath) as csv_file:
            data_file = csv.reader(csv_file)
            temp = next(data_file)
            n_samples = int(temp[0])
            n_features = int(temp[1])
            target_names = np.array(temp[2:])
            data = np.empty((n_samples, n_features))
            target = np.empty((n_samples,), dtype=np.int)

            for i, ir in enumerate(data_file):
                data[i] = np.asarray(ir[:-1], dtype=np.float64)
                target[i] = np.asarray(ir[-1], dtype=np.int)

        return Bunch(data=data, target=target,
                     target_names=target_names,
                     DESCR="",
                     feature_names=['sepal length (cm)', 'sepal width (cm)',
                                    'petal length (cm)', 'petal width (cm)'])

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

    @staticmethod
    def get_ndarray_from_web_txt(url):
        text = Input.internet_read_text_file(url)
        input_array = text.split('\n')
        float_array = []
        for line in input_array:
            float_line = [float(i) for i in line.split(' ')]
            float_array.append(float_line)
        X = array(float_array)
        return X

    @staticmethod
    def get_dat_file(file_path):
        try:  # SciPy >= 0.16 have face in misc
            dat = Input.face(gray=True)
        except ImportError:
            dat = sp.face(gray=True)
        return dat

    @staticmethod
    def face(gray=False):
        import bz2
        import os
        with open(os.path.join('C:\\Users\\vladimir.kornilov\\Python\\ProjectOfDataMining\\!Datasets\\image.dat'), 'rb') as f:
            rawdata = f.read()
        data = bz2.decompress(rawdata)
        fromstring = multiarray.fromstring
        face = fromstring(data, dtype='uint8')
        face.shape = (768, 1024, 3)
        if gray is True:
            face = (0.21 * face[:, :, 0] + 0.71 * face[:, :, 1] + 0.07 * face[:, :, 2]).astype('uint8')
        return face

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
    def write_to_txt_file_two_value(filePath, list1, list2):
        try:
            with open(filePath, 'w', encoding='utf-8') as file:
                for x, y in zip(list1, list2):
                    file.write(str(x) + " [" + str(y) + " class/cluster]\n")
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




class Bunch(dict):
    """Container object for datasets

    Dictionary-like object that exposes its keys as attributes.

    >>> b = Bunch(a=1, b=2)
    >>> b['b']
    2
    >>> b.b
    2
    >>> b.a = 3
    >>> b['a']
    3
    >>> b.c = 6
    >>> b['c']
    6

    """

    def __init__(self, **kwargs):
        super(Bunch, self).__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __dir__(self):
        return self.keys()

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setstate__(self, state):
        # Bunch pickles generated with scikit-learn 0.16.* have an non
        # empty __dict__. This causes a surprising behaviour when
        # loading these pickles scikit-learn 0.17: reading bunch.key
        # uses __dict__ but assigning to bunch.key use __setattr__ and
        # only changes bunch['key']. More details can be found at:
        # https://github.com/scikit-learn/scikit-learn/issues/6196.
        # Overriding __setstate__ to be a noop has the effect of
        # ignoring the pickled __dict__
        pass