from PyQt5 import QtWidgets
import PleiferDesign
from collections import OrderedDict

class Cipher(QtWidgets.QDialog, PleiferDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)
        self.swapButton.clicked.connect(self.swap)

        self.alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz."
        self.alf += chr(2045)
        self.alf_list = []
        self.ROW = 6
        self.COL = 9
        for char in self.alf:
            self.alf_list.append(char)

    def encrypt(self):
        keys = ""
        keys += self.get_key()
        input_old = ""
        input_old = self.textEdit.toPlainText()
        zero = ''
        if keys == zero:  # проверка, что ключ не пуст
            self.show_msg(4)
            return -1

        if input_old == zero:  # проверка, что входной текст не пуст
            self.show_msg(3)
            return -1

        count_open = 0  # проверка корректности входного текста
        for elem in input_old:
            for symbol in self.alf:
                if elem == symbol:
                    count_open += 1

        if count_open != len(input_old):
            self.show_msg(1)
            return -1

        count_key = 0  # проверка корректности ключа
        for elem_key in keys:
            for symbol in self.alf:
                if elem_key == symbol:
                    count_key += 1

        if count_key != len(keys):
            self.show_msg(2)
            return -1

        key = []
        for i in keys:
            key.append(i)

        key_n = list(OrderedDict.fromkeys(key))

        matrix_key = [[0 for x in range(self.COL)] for y in range(self.ROW)]

        count = 0
        isExit = False
        for i in range(self.ROW):
            if isExit:
                break
            for j in range(self.COL):
                if isExit:
                    break
                elif count < len(key_n):
                    matrix_key[i][j] = key_n[count]
                    count += 1
                # Если ключ записали в матрицу
                elif count >= len(key_n):
                    matrix_key = self.fill_matr_key(matrix_key, i, j, key_n)
                    isExit = True

        result = ''

        input = ""
        index = 0

        for sym in input_old:  #
            if index == len(input_old)-1:  # если последний символ
                input += sym
                index += 1
            elif input_old[index] != input_old[index+1]:  # если следующий символ не равен предыдущему
                input += sym
                index += 1
            elif input_old[index] == input_old[index+1]:  # если подряд два одинаковых символа
                input += sym
                input += chr(2045)
                index += 1

        if len(input)%2 != 0:
            input += chr(2045)

        a = 0
        b = 0
        c = 0
        d = 0

        for indx in range(len(input)):
            if indx % 2 == 0:
                for i in matrix_key:
                    for j in i:
                        if j == input[indx]:
                            a = matrix_key.index(i)
                            b = i.index(input[indx])

                            next = input[indx + 1]
                            for i in matrix_key:
                                for j in i:
                                    if j == next:
                                        c = matrix_key.index(i)
                                        d = i.index(next)

                                        if a == c:
                                            result += matrix_key[a][(b+1)%9]
                                            result += matrix_key[c][(d+1)%9]
                                        elif b == d:
                                            result += matrix_key[(a+1)%6][b]
                                            result += matrix_key[(c+1)%6][d]
                                        elif a != c and b != d:
                                            result += matrix_key[a][d]
                                            result += matrix_key[c][b]


        self.textBrowser.setPlainText("".join(x for x in result))

    def fill_matr_key(self, matrix_key, i, j, key_n):
        indx = 0
        new_alf = []
        # удаление элементов ключа из алфавита
        for el in self.alf_list:
            if el not in key_n:
                new_alf.append(el)

        self.alf_list = new_alf

        flag = False  # Не начало строки?
        # Если это не начало строки
        if j != 0:
            flag = True
        for ii in range(i, self.ROW):
            if flag:
                for jj in range(j, self.COL):
                    matrix_key[ii][jj] = self.alf_list[indx]
                    indx += 1

                    flag = False
            else:
                for jj in range(self.COL):
                    matrix_key[ii][jj] = self.alf_list[indx]
                    indx += 1

        return matrix_key

    def show_msg(self, par):
        self.msg = QtWidgets.QMessageBox()
        if par == 1:
            self.msg.setText("Недопустимые символы в открытом тексте!")
        elif par == 2:
            self.msg.setText("Недопустимые символы в ключе!")
        elif par == 3:
            self.msg.setText("Введите текст!")
        elif par == 4:
            self.msg.setText("Введите ключ!")
        self.msg.exec_()
        return -1

    def decrypt(self):
        keys = ""
        keys += self.get_key()

        input = ""
        input = self.textEdit.toPlainText()

        count_open = 0  # проверка открытого текста на недопустимые символы
        for elem in input:
            for symbol in self.alf:
                if elem == symbol:
                    count_open += 1

        if count_open != len(input):
            self.show_msg(1)

        count_key = 0
        for elem_key in keys:
            for symbol in self.alf:
                if elem_key == symbol:
                    count_key += 1

        if count_key != len(keys):
            self.show_msg(2)

        zero = ''
        if keys == zero:
            self.show_msg(4)

        if input == zero:
            self.show_msg(3)


        key = []
        for i in keys:
            key.append(i)

        key_n = list(OrderedDict.fromkeys(key))

        matrix_key = [[0 for x in range(self.COL)] for y in range(self.ROW)]

        count = 0
        isExit = False
        for i in range(self.ROW):
            if isExit:
                break
            for j in range(self.COL):
                if isExit:
                    break
                elif count < len(key_n):
                    matrix_key[i][j] = key_n[count]
                    count += 1
                # Если ключ записали в матрицу
                elif count >= len(key_n):
                    matrix_key = self.fill_matr_key(matrix_key, i, j, key_n)
                    isExit = True

        result = ''

        if len(input)%2 != 0:
            input += chr(2045)

        a = 0
        b = 0
        c = 0
        d = 0

        for indx in range(len(input)):
           if indx%2 == 0:
                for i in matrix_key:
                    for j in i:
                        if j == input[indx]:
                            a = matrix_key.index(i)
                            b = i.index(input[indx])

                            next = input[indx + 1]
                            for i in matrix_key:
                                for j in i:
                                    if j == next:
                                        c = matrix_key.index(i)
                                        d = i.index(next)

                                        if a == c:
                                            if b == 0 and d == 0:
                                                result += matrix_key[a][8]
                                                result += matrix_key[c][8]
                                            elif b == 0 and d != 0:
                                                result += matrix_key[a][8]
                                                result += matrix_key[c][d-1]
                                            elif b != 0 and d == 0:
                                                result += matrix_key[a][b-1]
                                                result += matrix_key[c][8]
                                            else:
                                                result += matrix_key[a][(b-1)%9]
                                                result += matrix_key[c][(d-1)%9]
                                        elif b == d:
                                            if a == 0 and c == 0:
                                                result += matrix_key[5][b]
                                                result += matrix_key[5][d]
                                            elif a == 0 and c != 0:
                                                result += matrix_key[5][b]
                                                result += matrix_key[c-1][d]
                                            elif a != 0 and c == 0:
                                                result += matrix_key[a-1][b]
                                                result += matrix_key[5][d]
                                            else:
                                                result += matrix_key[(a-1)%6][b]
                                                result += matrix_key[(c-1)%6][d]
                                        elif a != c and b != d:
                                            result += matrix_key[a][d]
                                            result += matrix_key[c][b]

        self.textBrowser.setPlainText("".join(x for x in result))

    def get_key(self):
        key = self.keyEdit.text()
        return key

    def swap(self):
        input_text = self.textEdit.toPlainText()
        tmp = self.textBrowser.toPlainText()
        self.textBrowser.setPlainText(input_text)
        self.textEdit.setPlainText(tmp)