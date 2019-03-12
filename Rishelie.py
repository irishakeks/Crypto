from PyQt5 import QtWidgets
import RishelieDesign
import random

class Cipher(QtWidgets.QDialog, RishelieDesign.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.encryptButton.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)

        self.eng = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        self.rus = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЫыЪъЭэЮюЯя'

        self.grille = [0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0]



# popopopopopopopopopopopopopopopopo
    def encrypt(self):

        keys = ""
        keys += self.get_key()

        input_text = ""
        input_text = self.textEdit.toPlainText()

        self.index = 0

        self.len_text = len(input_text)

        result = ""
        alf = self.choose_alf(input_text)

        result = self.change(result,alf, input_text, keys, 0)

        self.textBrowser.setPlainText("".join(x for x in result))


    # 123 4567 89 10396
    # str_list = str.split(splice)(" ")
    # for str in str_list:
    # int(el)

    def change(self, result,alf, input_text,keys, enc_dec):
        #key1, key2, key3, key4, key5, key6, key7, key8 = keys.split(" ")
        #keys = [key1, key2, key3, key4, key5, key6, key7, key8]

        list_keys_len = [3, 2, 4, 8, 5, 3, 7, 2]

        input_text_without0 = ''
        index = 0
        count = 0

        if len(input_text) != 57 and enc_dec == 1:
            self.show_msg()

        if enc_dec == 1:
            for letter in self.grille:
                if letter == 1:
                    len_key = list_keys_len[index]
                    while len_key > 0:
                        input_text_without0 += input_text[count]
                        count = count + 1
                        len_key = len_key - 1
                    index = index + 1
                else:
                    count = count + 1




        tmp_keys = []
        tmp_keys = keys.split("-")
        keys_list = []


        for str in tmp_keys:
            keys_list.append(str.split(","))

        iter = 0
        for letter in self.grille:
            letter = int(letter)
            if letter == 0 and enc_dec == 0:
                result += self.rand_symb(alf)
            elif letter == 1:
                # если зашифровка и входной текст не закончился
                if enc_dec == 0 and self.index != len(input_text):
                    result += self.permutation(keys_list[iter], input_text, alf)
                    iter += 1
                # если входной текст закончился и это зашифровка
                elif enc_dec == 0 and self.index == len(input_text):
                    a = list_keys_len[iter]
                    while a != 0:
                        result += self.rand_symb(alf)
                        a = a - 1
                    iter = iter + 1

                elif enc_dec == 1:
                    result += self.permutation_dec(keys_list[iter], input_text_without0)
                    iter += 1
        return result



    def permutation(self,ckey, input_text, alf):
        value = 0
        tmp = []
        # можно скей+1 попробовать
        for i in range(len(ckey)):
            tmp.append(" ")

        for letter in ckey:
            if self.index != len(input_text):
                tmp[int(letter)-1] = self.take_symb(input_text)
            elif self.index == len(input_text):
                tmp[int(letter) - 1] = self.rand_symb(alf)

        ttmp = ""
        for i in tmp: # делаем из списка строку
            ttmp += i
        return ttmp


    def take_symb(self, input_text):

        print(self.index)
        symb = input_text[self.index]
        self.index = self.index+1
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


    def show_msg(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText("Длина сообщения должна быть равна 57!")
        self.msg.exec_()
        return -1


    def get_key(self):
        key = self.keyEdit.text()
        return key


    def rand_symb(self, alf):
        if alf == self.eng:
            alf_size = 52
        else:
            alf_size = 66


        a = random.randint(0, alf_size - 1)
        random_symb = alf[a]

        return random_symb

    def decrypt(self):

        keys = ""
        keys += self.get_key()

        input_text = ""
        input_text = self.textEdit.toPlainText()



        self.index = 0

        self.len_text = len(input_text)

        result = ""
        alf = self.choose_alf(input_text)

        result = self.change(result,alf, input_text, keys, 1)

        self.textBrowser.setPlainText("".join(x for x in result))



    def permutation_dec(self,ckey, input_text):
        value = 0
        tmp = []
        # можно скей+1 попробовать
        for i in range(len(ckey)):
            tmp.append(" ")

        for letter in ckey:
            tmp[int(letter)-1] = self.take_symb(input_text)

        ttmp = ""
        for i in tmp: # делаем из списка строку
            ttmp += i
        return ttmp