from PyQt5 import QtWidgets
import HillDesign
import math

class Cipher(QtWidgets.QDialog, HillDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)
        self.swapButton.clicked.connect(self.swap)

        self.Alpha = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя_., "


    def encrypt(self):
        input = ""
        input = self.textEdit.toPlainText()

        key = ""
        key += self.get_key()

        zero = ''
        if key == zero:  # проверка, что ключ не пуст
            self.show_msg(4)
            return -1

        if input == zero:  # проверка, что входной текст не пуст
            self.show_msg(3)
            return -1

        count_open = 0  # проверка корректности входного текста
        for elem in input:
            for symbol in self.Alpha:
                if elem == symbol:
                    count_open += 1

        if count_open != len(input):
            self.show_msg(1)
            return -1

        count_key = 0  # проверка корректности ключа
        for elem_key in key:
            for symbol in self.Alpha:
                if elem_key == symbol:
                    count_key += 1

        if count_key != len(key):
            self.show_msg(2)
            return -1

        # если длина ключа не является корнем какого-то числа, дописываем пробелы, пока не станет корнем
        while math.sqrt(len(key)) % 1 != 0:
            key += " "

        n = int(math.sqrt(len(key)))

        # переводим ключ в индексы согласно алфавиту
        ind_key = []
        for el in key:
            ind_key.append(self.Alpha.index(el))

        # если длина вх текста не кратна н, заполняем пробелами, пока не станет
        while len(input) % n != 0:
            input += " "

        # переводим вх текст в индексы согласно алфавиту
        ind_input = []
        for el in input:
            ind_input.append(self.Alpha.index(el))

        matrix_key = []

        index = 0
        # делаем из ключа матрицу размером н на н
        for i in range(n):
            matrix_key.append([])
            for j in range(n):
                matrix_key[i].append(ind_key[index])
                index += 1

        # делим вх текст на н-граммы и перемножаем матрицы
        ind_result = []
        for i in range(0, len(ind_input), n):
            tmp = i + n
            new = ind_input[i:tmp]
            mult = self.multiplication_matrix(new, matrix_key)
            ind_result.append(mult)

        # переводим индексы в буквы
        result = ''
        for o in ind_result:
            for p in o:
                result += self.Alpha[p]

        self.textBrowser.setPlainText("".join(x for x in result))


    def multiplication_matrix(self, m1, m2):
        m3 = []
        s = 0
        t = []
        for j in range(0, len(m2[0])):
            for i in range(0, len(m1)):
                s = s + m1[i] * m2[i][j]
            m3.append(s % 37)
            s = 0

        return m3


    def decrypt(self):

        input = ""
        input = self.textEdit.toPlainText()

        key = ""
        key += self.get_key()

        zero = ''
        if key == zero:  # проверка, что ключ не пуст
            self.show_msg(4)
            return -1

        if input == zero:  # проверка, что входной текст не пуст
            self.show_msg(3)
            return -1

        count_open = 0  # проверка корректности входного текста
        for elem in input:
            for symbol in self.Alpha:
                if elem == symbol:
                    count_open += 1

        if count_open != len(input):
            self.show_msg(1)
            return -1

        count_key = 0  # проверка корректности ключа
        for elem_key in key:
            for symbol in self.Alpha:
                if elem_key == symbol:
                    count_key += 1

        if count_key != len(key):
            self.show_msg(2)
            return -1

        while math.sqrt(len(key)) % 1 != 0:
            key += " "

        n = int(math.sqrt(len(key)))

        ind_key = []
        for el in key:
            ind_key.append(self.Alpha.index(el))

        while len(input) % n != 0:
            input += " "

        ind_input = []
        for el in input:
            ind_input.append(self.Alpha.index(el))

        matrix_key = []

        index = 0

        for i in range(n):
            matrix_key.append([])
            for j in range(n):
                matrix_key[i].append(ind_key[index])
                index += 1
        det = 0
        det = self.deter(matrix_key)
        if det == 0:
            self.show_msg(5)

        inverse_det = self.Euclid(37, det)

        # составляем матрицу с минорами, сразу же умножаем на обратный элемент к определителю и все это по модулю
        new_matrix = []

        for i in range(n):
            new_matrix.append([])
            for j in range(n):
                new_matrix[i].append(0)
        for i in range(n):
            for j in range(n):
                koef = (pow((-1), (i + j)))
                det_min = self.deter(self.minor(matrix_key, i, j))
                new_matrix[i][j] = (koef * det_min) % 37


        # транспонируем матрицу
        transp = self. transpon_matrix(new_matrix, n, inverse_det)

        # делим вх текст на н-граммы и перемножаем матрицы
        ind_result = []
        for i in range(0, len(ind_input), n):
            tmp = i + n
            new = ind_input[i:tmp]
            mult = self.multiplication_matrix(new, transp)
            ind_result.append(mult)

        # переводим индексы в буквы  _з_б.и
        result = ''
        for o in ind_result:
            for p in o:
                result += self.Alpha[p]

        self.textBrowser.setPlainText("".join(x for x in result))



    def transpon_matrix(self, matrix, n, inver):
        transp = []
        for i in range(n):
            transp.append([])
            for j in range(n):
                transp[i].append(0)
        for i in range(n):
            for j in range(n):
                transp[j][i] = (matrix[i][j] * inver) % 37
        return transp

    def Euclid(self, a, b):
        x2 = 1
        x1 = 0
        y2 = 0
        y1 = 1
        q = 0
        r = 0
        x = 0
        y = 0

        while b > 0:
            q = a // b
            r = a % b
            x = x2 - q * x1
            y = y2 - q * y1
            a = b
            b = r
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y

        while y2 < 0:
            y2 += 37
        return y2

    def deter(self, a):
        det = 0
        rank = len(a[0])

        if rank == 1:
            det = a[0][0]

        elif rank == 2:
            det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
        elif rank > 2:
            for i in range(rank):
                minor = self.minor(a, 0, i)
                first = pow(-1, i)
                second = a[0][i]
                d = self.deter(minor)
                det += first*second*d

        det %= 37
        if det < 0:
            det += 37

        return det

    def minor(self, a, row, column):
        n = len(a[0])
        buf = []
        for i in range(n-1):
            buf.append([])
            for j in range(n-1):
                buf[i].append(0)
        for i in range(n):
            for j in range(n):
                if i != row or j != column:
                    if i > row and j < column:
                        buf[i-1][j] = a[i][j]
                    elif i < row and j > column:
                        buf[i][j - 1] = a[i][j]
                    elif i > row and j > column:
                        buf[i - 1][j - 1] = a[i][j]
                    elif i < row and j < column:
                        buf[i][j] = a[i][j]
        return buf

    def swap(self):
        input_text = self.textEdit.toPlainText()
        tmp = self.textBrowser.toPlainText()
        self.textBrowser.setPlainText(input_text)
        self.textEdit.setPlainText(tmp)


    def get_key(self):
        key = self.keyEdit.text()
        return key

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
        elif par == 5:
            self.msg.setText("Неподходящий ключ!")
        self.msg.exec_()
        self.msg.exec_()
        return -1