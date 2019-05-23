from PyQt5 import QtWidgets
import Rishelie2Design
import random


class Cipher(QtWidgets.QDialog, Rishelie2Design.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)
        self.swapButton.clicked.connect(self.swap)


    def encrypt(self):
        keys = ""
        keys += self.get_key()

        input = ""
        input = self.textEdit.toPlainText()

        input_text = []
        for i in input:
            input_text.append(i)

        tmp_keys = []
        tmp_keys = keys.split("-")  # Cтрока разбилась на список типа ["1,3,2", "2,1"]
        keys_list = []  # Список для конечного варианты ключей типа [["1","3","2"], ["2", "1"]]

        # Цикл как раз преобразует данные к нужному виду, который выше
        for tmp in tmp_keys:
            tmp_list = tmp.split(",")  # Разбивает
            keys_list.append(tmp_list)  # Добавляет

        result = ''

        keys_len = self.key_len(keys_list, input_text)  # Считает общее количество элементов в ключе
        text_len = len(input)  # Длина входного текста
        # Проверка на ключа на длину
        if keys_len > text_len:
            self.show_msg("Слишком длинный ключ!")
            return()

        last_sub_key = len(keys_list) - 1  # Индекс последнего подключа
        count = 0
        # Перебор всех подключей
        for sub_key in keys_list:
            flag = self.check(sub_key)  # (проверка на ключ верный) Описание в самом методе
            if last_sub_key == count and flag == True:
                # если последний подключ, передается текст до самого конца
                res = self.swa(sub_key, input_text, True)
            elif flag == True:
                # передается только часть текста длиной с подключ
                res = self.swa(sub_key, input_text[:len(sub_key)])
            else:
                self.show_msg("Ошибка в ключе!")
                return "Ошибка в ключе!"
            result += res # прибавляем зашифрованную часть текса
            input_text = input_text[len(sub_key):]  # убираем с текста часть, которую зашифровали
            count += 1

        self.textBrowser.setPlainText("".join(x for x in result))

    # Длина всего ключа
    def key_len(self, keys, text):
        len = 0
        for sub_keys in keys:
            for el in sub_keys:
                len += 1
        return len

    def show_msg(self, text):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(text)
        self.msg.exec_()

    # Проверка на то, что в подключе не пропущено число ([1,3,2] вернет True [1,4,2] вернет False
    def check(self, sub_key):
        len_sub_key = len(sub_key)
        cou = 1
        while cou <= (len(sub_key)):
            res = str(cou) in sub_key
            if res:
                cou += 1
            else:
                return res
        return True

    # замена букв в рейнже подключа
    def swa(self, sub_key, text, is_last=False):
        result = ""
        # от 0 до длины ключа
        for i in range(len(sub_key)):
            key = int(sub_key[i]) - 1  # берется i-ый элемент подключа - 1 (т.к. индексы должны быть с 0)
            result += text[key]  # прибавляем символ с индексом == key
        # если это последний подключ
        if is_last:
            add = "".join(text[len(sub_key):])  # берем весь осташийся после шифровки текст
            result += add  # и добвляем его к результату
        return result

    # abc & 2,1,3 => bac
    # bac & 2,1,3 .. 2,3 ..

    # работает как swa, только ищет числа в порядке возрастания (1..n)
    def swa_dec(self, sub_key, text, is_last=False):
        result = ""
        count = 1
        all = False  # ключ показывает, что весь подключ преобразован
        while not all:
            for i in range(len(sub_key)):
                key = int(sub_key[i])
                if key == count:
                    # sub_key.remove(sub_key[i])
                    result += text[i]
                    count += 1
                    break
                # если подключ и результат совпадают по длине
                if len(sub_key) == len(result):
                    all = True
        # если это последний подключ
        if is_last:
            add = "".join(text[len(sub_key):])
            result += add
        return result

    def get_key(self):
        key = self.keyEdit.text()
        return key

    def decrypt(self):
        keys = ""
        keys += self.get_key()

        input = ""
        input = self.textEdit.toPlainText()

        input_text = []
        for i in input:
            input_text.append(i)

        tmp_keys = []
        tmp_keys = keys.split("-")
        keys_list = []

        for tmp in tmp_keys:
            tmp_list = tmp.split(",")
            keys_list.append(tmp_list)

        result = ''

        keys_len = self.key_len(keys_list, input_text)
        text_len = len(input)
        if keys_len > text_len:
            self.show_msg("Слишком длинный ключ!")
            return()

        last_sub_key = len(keys_list) - 1
        count = 0
        for sub_key in keys_list:
            flag = self.check(sub_key)
            if last_sub_key == count and flag == True:
                res = self.swa_dec(sub_key, input_text, True)
            elif flag == True:
                res = self.swa_dec(sub_key, input_text[:len(sub_key)])
            else:
                self.show_msg("Ошибка в ключе!")
                return "Ошибка в ключе!"
            result += res
            input_text = input_text[len(sub_key):]
            count += 1

        self.textBrowser.setPlainText("".join(x for x in result))

    def swap(self):
        input_text = self.textEdit.toPlainText()
        tmp = self.textBrowser.toPlainText()
        self.textBrowser.setPlainText(input_text)
        self.textEdit.setPlainText(tmp)