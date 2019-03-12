from PyQt5 import QtWidgets
import KardanoDesign
import random

class Cipher(QtWidgets.QDialog, KardanoDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)
        self.index = 0

        self.len_text = 0

        self.grille0 = [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                        0, 1, 0,0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0]

        self.grille90 = [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0,
                         1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]

        self.grille180 = [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
                          0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]

        self.grille270 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
                          1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]

        self.eng = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        self.rus = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя'



    def encrypt(self):
        input_text = ""
        input_text = self.textEdit.toPlainText()
        self.index = 0

        self.len_text = len(input_text)
        shtuka = len(input_text)

        result = ""
        alf = self.choose_alf(input_text)

        xyinya = 0

        while shtuka > 0:

            if self.index != self.len_text:
                result = self.fgrille0(input_text, result, alf, xyinya)

            if self.index != self.len_text:
                result = self.fgrille90(result, input_text, xyinya)

            if self.index != self.len_text:
                result = self.fgrille180(result, input_text, xyinya)

            if self.index != self.len_text:
                result = self.fgrille270(result, input_text, xyinya)
            shtuka = shtuka - 64
            xyinya = xyinya + 64

        self.textBrowser.setPlainText("".join(x for x in result))

    def fgrille0(self,input_text, result, alf, xyinya):

        for letter in self.grille0:

            if letter == 1:  # если символ из решетки единица

                # если входной текст не закончился и остаток от деления длины результата на 64 не 0 или длина рез 0
                if self.index != self.len_text and (len(result)%64 != 0 or len(result) == xyinya):
                    symbol = self.take_symb(input_text)  # берем символ из вх текста и пишем его в результат
                    result += symbol

                # если входной текст закончился, но в результате не 64 символа, пишем рандомный
                elif self.index == self.len_text and len(result)%64 != 0:
                    result += self.rand_symb(alf)

                # если текст закончился и в результате 64 символа
                elif self.index == self.len_text and (len(result)%64 != 0 or len(result) == xyinya):
                    return result

                # а если текст не закончился, остаток от деления длины рез на 64 не 0
                elif self.index != self.len_text and len(result)%64 != 0:
                    return result

            # если символ из решетки 0, входной текст еще есть и остаток от деления дл рез на 64 не 0 или рез пустой
            elif letter == 0 and self.index != self.len_text and (len(result)%64 != 0 or len(result) == xyinya):
                result += self.rand_symb(alf)  # пишем рандомный символ

            elif letter == 0 and self.index == self.len_text:  # если 0 и входного текста нет
                if len(result)%64 != 0:  # если меньше 64 символов в результате, то + ранд символ
                    result += self.rand_symb(alf)
                else:
                    return result
            # если  вх текст еще есть,
            elif self.index != self.len_tex and (len(result)%64 != 0 or len(result) != xyinya):
                return result


        return result



    def fgrille90(self, result,input_text, xyinya):

        indx = xyinya
        for letter in self.grille90:
            if letter == 1 and self.index != self.len_text:
                result = self.rep(indx, self.take_symb(input_text), result)
                # result = result.replace(result[indx], self.take_symb(input_text))
            indx += 1
        return result

    def fgrille180(self, result,input_text, xyinya):
        indx = xyinya
        for letter in self.grille180:
            if letter == 1 and self.index != self.len_text:
                result = self.rep(indx, self.take_symb(input_text), result)
            indx += 1
        return result

    def rep(self, ind, char, string):
        tmp = string[:ind] + char + string[ind+1:]
        return tmp



    def fgrille270(self, result,input_text, xyinya):

        indx = xyinya
        for letter in self.grille270:
            if letter == 1 and self.index != self.len_text:
                result = self.rep(indx, self.take_symb(input_text), result)
            indx += 1
            # result = result.replace(result[indx], self.take_symb(input_text))

        return result





    def take_symb(self, input_text):

        #for symbol in input_text:
        print(self.index)
        symb = input_text[self.index]
        self.index = self.index+1
        #input_text = input_text[1,len(input_text)]
        return symb

    def choose_alf(self, input_text):
        for symbol in input_text:
            for letter in self.eng:
                if symbol == letter:
                    alf = self.eng
                    return alf
                else:
                    alf = self.rus
            return alf


    def rand_symb(self, alf):
        if alf == self.eng:
            alf_size = 52
        else:
            alf_size = 66


        a = random.randint(0, alf_size - 1)
        random_symb = alf[a]

        return random_symb






    def decrypt(self):

        # На входе строка шифртекста, нужно расшифровать
        # Нужно делить на 64 симв, потом переставлять
        #
        input_text = ""
        input_text = self.textEdit.toPlainText()
        self.index = 0

        self.len_text = len(input_text)
        shtuka = len(input_text)

        result = ""

        if len(input_text)%64 != 0:
            self.show_msg()

        indx = 0
        while shtuka > 0:

            if self.index != self.len_text:
                result = self.grille_dec(self.grille0, result, input_text, indx)

            if self.index != self.len_text:
                result = self.grille_dec(self.grille90, result, input_text, indx)

            if self.index != self.len_text:
                result =self.grille_dec(self.grille180, result, input_text, indx)

            if self.index != self.len_text:
                result = self.grille_dec(self.grille270, result, input_text, indx)
            shtuka = shtuka - 64
            indx = indx + 64

        self.textBrowser.setPlainText("".join(x for x in result))



    def grille_dec(self, grille, result, input_text, indx):

        for symbol in grille:

            if symbol == 1 and  indx < len(input_text):

                result += input_text[indx]
            indx = indx + 1

        return result

    def show_msg(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText("Длина сообщения должна быть кратна 64!")
        self.msg.exec_()
        return -1
