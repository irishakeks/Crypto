from PyQt5 import QtWidgets
import AlbertiDesign
import random

class Cipher(QtWidgets.QDialog, AlbertiDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)
        self.swapButton.clicked.connect(self.swap)

        self.outside_rus = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя'
        self.outside_eng = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

        self.inside_rus = "ЫгКЪЭяпРоНЩЁзДАМЮтцхфчШЛижвОЬынбеУСЙёдГюъХПмэаИлшсЕБьТкЗрФщВЧйЖЯЦу"
        self.inside_eng = "OGuiKLZbErphJcTwYMfoNAFVsDBRvxlXHeangtjmzQPCIWqdySUk"

    def encrypt(self):

        input_text = self.textEdit.toPlainText()

        result = ""

        iter = 0
        for letter in input_text:
            flag = False
            for element in self.outside_rus:
                index = 0
                if letter == element:
                    index = self.outside_rus.index(element) + iter
                    flag = True
                    if index > 65:
                        index = index % 66

                    result += self.inside_rus[index]
                    iter = iter+1

            for elem in self.outside_eng:
                index = 0
                if letter == elem:
                    index = self.outside_eng.index(elem) + iter
                    flag = True
                    if index > 51:
                        index = index % 52

                    result += self.inside_eng[index]
                    iter = iter + 1

            if flag == False:
                result += letter
        self.textBrowser.setPlainText("".join(x for x in result))



    def decrypt(self):

        input_text = ""
        input_text = self.textEdit.toPlainText()

        result = ""

        iter = 0

        for letter in input_text:
            flag = False
            for element in self.inside_rus:
                index = 0
                if letter == element:
                    index = self.inside_rus.index(element) - iter
                    flag = True
                    if index < 0:
                        index = 66 - abs(index)
                        # index = index % 66
                    result += self.outside_rus[index]
                    iter = iter+1

            for elem in self.inside_eng:
                index = 0
                if letter == elem:
                    index = self.inside_eng.index(elem) - iter
                    flag = True
                    if index < 0:
                        index = 52 - abs(index)
                       # index = index % 52
                    result += self.outside_eng[index]
                    iter = iter + 1

            if flag == False:
                result += letter

        self.textBrowser.setPlainText("".join(x for x in result))

    def swap(self):
        input_text = self.textEdit.toPlainText()
        tmp = self.textBrowser.toPlainText()
        self.textBrowser.setPlainText(input_text)
        self.textEdit.setPlainText(tmp)
