from PyQt5 import QtWidgets
import polibDesign


class Cipher(QtWidgets.QDialog, polibDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)
        self.swapButton.clicked.connect(self.swap)

    def encrypt(self):  # если зашифровка, передаем в функцию 1
        self.polib(1)

    def decrypt(self):  # если расшифровка, передаем в функцию -1
        self.polib(-1)



    def polib(self, koef):


        input_text = self.textEdit.toPlainText()

        upper_english = [["A", "B", "C", "D", "E"],
                         ["F", "G", "H", "I", "J"],
                         ["K", "L", "M", "N", "O"],
                         ["P", "Q", "R", "S", "T"],
                         ["U", "V", "W", "X", "Y"],
                         ["Z", "B", "C", "D", "E"]]

        lower_english = [["a", "b", "c", "d", "e"],
                         ["f", "g", "h", "i", "j"],
                         ["k", 'l', 'm', 'n', 'o'],
                         ['p', 'q', 'r', 's', 't'],
                         ['u', 'v', 'w', 'x', 'y'],
                         ['z', 'b', 'c', 'd', 'e']]

        upper_rus = [['А', "Б", "В", "Г", "Д", "Е"],
                     ["Ё", "Ж", "З", "И", "Й", "К"],
                     ["Л", "М", "Н", "О", "П", "Р"],
                     ["С", "Т", "У", "Ф", "Х", "Ц"],
                     ["Ч", "Ш", "Щ", "Ь", "Ы", "Ъ"],
                     ["Э", "Ю", "Я", "Г", "Д", "Е"]]

        lower_rus =  [["а","б", "в", "г", "д", "е"],
                      ["ё", "ж", "з", "и", "й", "к"],
                      ["л", "м", "н", "о", "п", "р"],
                      ["с", "т", "у", "ф", "х", "ц"],
                      ["ч", "ш", "щ", "ь", "ы", "ъ"],
                      ["э", "ю", "я", "г", "д", "е"]]

        alf_list = [upper_english, lower_english, upper_rus, lower_rus]

        result = ""
        for symbol in input_text:
            in_alf = False
            flag = False
            for alf in alf_list:
                for str in alf:
                    if symbol in str:
                        result += self.alf(alf, symbol, koef)
                        in_alf = True
                        flag = True
                        break
                if flag: break
            if not in_alf:
                result += symbol

        self.textBrowser.setPlainText("".join(x for x in result))

    def alf(self, alphabet, symbol, koef):
            for string in alphabet:
                for element in string:
                    if koef == 1:
                        symbol1 = self.exceptions_enc(symbol)
                    else:
                        symbol1 = self.exceptions_dec(symbol)
                    if symbol1:
                        return symbol1
                    if symbol == element:
                        index = string.index(element)
                        indexU = alphabet.index(string)
                        symbol1 = alphabet[indexU+koef][index]
                        return symbol1

    def exceptions_dec(self, symbol):  # исключения для расшифровки
        if symbol == "A":
            return "Z"
        elif symbol == "a":
            return "z"
        elif symbol == "B":
            return "V"
        elif symbol == "C":
            return "W"
        elif symbol == "D":
            return "X"
        elif symbol == "E":
            return "Y"
        elif symbol == "b":
            return "v"
        elif symbol == "c":
            return "w"
        elif symbol == "d":
            return "x"
        elif symbol == "e":
            return "y"
        elif symbol == "А":
            return "Э"
        elif symbol == "Б":
            return "Ю"
        elif symbol == "В":
            return "Я"
        elif symbol == "Г":
            return "Ь"
        elif symbol == "Д":
            return "Ы"
        elif symbol == "Е":
            return "Ъ"
        elif symbol == "а":
            return "э"
        elif symbol == "б":
            return "ю"
        elif symbol == "в":
            return "я"
        elif symbol == "г":
            return "ь"
        elif symbol == "д":
            return "ы"
        elif symbol == "е":
            return "ъ"

        return False

    def exceptions_enc(self, symbol):  # исключения для зашифровки
        if symbol == "Z":
            return "A"
        elif symbol == "z":
            return "a"
        elif symbol == "Э":
            return "А"
        elif symbol == "Ю":
            return "Б"
        elif symbol == "Я":
            return "В"
        elif symbol == "э":
            return "а"
        elif symbol == "ю":
            return "б"
        elif symbol == "я":
            return "в"

        return False

    def swap(self):
        input_text = self.textEdit.toPlainText()
        tmp = self.textBrowser.toPlainText()
        self.textBrowser.setPlainText(input_text)
        self.textEdit.setPlainText(tmp)