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

        self.grille0 = [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                        0, 1, 0,0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0]
        self.grille90 = [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0,
                         1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        self.grille180 = [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
                     0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]
        self.grille270 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
                        1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]

        self.eng = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtUuVvWwXxYyZz'
        self.rus = 'АаБбВвГгДдЕеЁёЖжЗзИиКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя'

    def encrypt(self):

        input_text = self.textEdit.toPlainText()

        result = ""
        alf = self.choose_alf(input_text)

        for letter in self.grille0:

            if letter == 1:
                if self.index != len(input_text):
                    symbol = self.take_symb(input_text)
                    result += symbol
                elif self.index == len(input_text) and len(result)%64!=0:
                    result += self.rand_symb(alf)
                else:
                    break
            elif letter == 0 and self.index != len(input_text):
                result += self.rand_symb(alf)
            elif letter == 0 and self.index == len(input_text):
                if len(result)%64!=0:
                    result += self.rand_symb(alf)
                else:
                    break

                    #len(result)//64!=0:

               #result += symbol


        self.textBrowser.setPlainText("".join(x for x in result))

# проверки на длину результата

    def take_symb(self, input_text):
        #for symbol in input_text:
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
            alf_size = 64
        a = random.randint (0, alf_size)
        random_symb = alf[a]
        return random_symb



    def decrypt(self):
        pass
