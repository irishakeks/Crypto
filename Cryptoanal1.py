from PyQt5 import QtWidgets
import operator
import cry_1
import FileDialog
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import model

class Cipher(QtWidgets.QDialog, cry_1.Ui_AtbashForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна
        self.CalcBut.clicked.connect(self.encrypt)
        self.ClearBut.clicked.connect(self.clear)
        self.OneKeyBut.clicked.connect(self.first)
        self.TwoKeyBut.clicked.connect(self.second)
        self.openBut.clicked.connect(self.open)
        self.SaveBut.clicked.connect(self.save)
        self.adressButton.clicked.connect(self.open_freq)
        self.saveFreqButton.clicked.connect(self.saveFreq)
        self.tableWidget.setColumnCount(4)
        self.wikiButton.setChecked(True)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(['Буква', 'Встречаемость', 'Частота', 'Частота по теории'])

        self.text_freq = None
        self.rusABC = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self.rusABC_lower = self.rusABC.lower()
        self.engABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.engABC_lower = self.engABC.lower()

        self.Rus = ({'о': 10.97}, {'е': 8.45},{'а': 8.01}, {"и": 7.35}, {"н": 6.7}, {"т": 6.26}, {"с": 5.47},
                    {"р": 4.73}, {"в": 4.54}, {"л": 4.4}, {"к": 3.49}, {"м": 3.21}, {"д": 2.98}, {"п": 2.81},
                    {"у": 2.62}, {"я": 2.01}, {"ы": 1.9}, {"ь": 1.74}, {"г": 1.7}, {"з": 1.65}, {"б": 1.59},
                    {"ч": 1.44}, {"й": 1.21}, {"х": 0.97}, {"ж": 0.94}, {"ш": 0.73}, {"ю": 0.64}, {"ц": 0.48},
                    {"щ": 0.36}, {"э": 0.32}, {"ф": 0.26}, {"ъ": 0.04}, {"ё": 0.04})
        self.Eng = ({"e": 12.7}, {'t': 9.06}, {'a': 8.17}, {'o': 7.51}, {'i': 6.97}, {'n': 6.75}, {'s': 6.33},
                    {'h': 6.09}, {'r': 5.99}, {'d': 4.25}, {'l': 4.03}, {'c': 2.78}, {'u': 2.76}, {'m': 2.41},
                    {'w': 2.36}, {'f': 2.23}, {'g': 2.02}, {'y': 1.97}, {'p': 1.93}, {'b': 1.49}, {'v': 0.98},
                    {'k': 0.77}, {'x': 0.15}, {'j': 0.15}, {'q': 0.1}, {'z': 0.05})


    def encrypt(self):
        file_check = self.fileButton.isChecked()
        wiki_check = self.wikiButton.isChecked()
        input = ""
        input = self.textEdit.toPlainText()

        input = input.lower()
        lang = self.lang(input)
        if lang == 0:
            self.show_msg(1)
            return "dct ujdyj"

        if file_check and not self.text_freq:
            self.show_msg(0)
            return
        language = self.language(input)
        dict_freq = self.dict_freq(language)

        # считаем вхождения каждой буквы, записываем
        for letter in input:
            for key in dict_freq.keys():
                if key == letter:
                    dict_freq[key] += 1

        len = self.calc_lenght(input)

        # считаем из вхождений частоты
        for key in dict_freq.keys():
            dict_freq[key] /= len

        # сортируем
        self.sorted_first = sorted(dict_freq.items(), key=operator.itemgetter(1))
        self.sorted_first.reverse()

        if wiki_check == True:
            first_key = ''
            for el in lang:
                for i in language:
                    if el == list(i.keys())[0]:
                        first_key += self.sorted_first[language.index(i)][0]

        elif file_check == True:

            self.list_freq = self.dict_freq(language)

            new_list_freq = []
            for el in self.list_freq:
                d = {el:self.list_freq[el]}
                new_list_freq.append(d)
            new_list_freq = tuple(new_list_freq)
            tmp = self.text_freq.split(". ")

            for el in tmp:
                ttt = el.split(" ")
                if ttt[0] not in lang:
                    self.show_msg(0)
                    return " "
                self.list_freq[ttt[0]] = float(ttt[1])
            first_key = ""
            for el in lang:
                for i in new_list_freq:
                    if el == list(i.keys())[0]:
                        first_key += self.sorted_first[new_list_freq.index(i)][0]

        self.lineEdit.setText("".join(str(x) for x in first_key))

        result_first = self.change(input, first_key)

        self.textBrowser.setPlainText("".join(str(x) for x in result_first))

        dict_shift = {}
        for le in first_key:
            for l in lang:
                if le == l:
                    shift = lang.index(l) - first_key.index(le)
                    if str(shift) in list(dict_shift.keys()):
                        dict_shift[str(shift)] += 1
                    else:
                        dict_shift[str(shift)] = 0
        dict_shift = sorted(dict_shift.items(), key=operator.itemgetter(1))
        dict_shift.reverse()

        bkey = int(dict_shift[0][0])

        second_key = ''
        second_key = '{0}{1}'.format(lang[bkey:],  lang[:bkey])
        self.lineEdit_2.setText("".join(str(x) for x in second_key))

        if wiki_check == True:
            self.fill_table(result_first, language)
        elif file_check == True:
            self.fill_table(result_first, self.list_freq)


    def fill_table(self,text, language):
        lang = self.lang(text)
        q = model.Data.delete()
        q.execute()
        print(q)
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['Буква', 'Встречаемость', 'Частота', 'Частота по теории'])
        for el in lang:
            vkh = 0
            freq = 0
            for let in text:
                if let == el:
                    vkh += 1
                freq = vkh / self.calc_lenght(text)
            freq_t = 0
            if self.wikiButton.isChecked() == True:
                for i in language:
                    if el == list(i.keys())[0]:
                        freq_t = i[el]
            elif self.fileButton.isChecked() == True:
                for i in language:
                    if el == i:
                        freq_t = language[i]
            tab = model.Data.create(letter = el, vkhozhdenie=vkh, freq=freq, freq_teory=freq_t)
            tab.save()
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(el)))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(vkh)))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(freq)))
            self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(freq_t)))


    def first(self):
        input = ""
        input = self.textEdit.toPlainText()
        input = input.lower()
        key = self.lineEdit.text()
        first = self.change(input, key)


        if self.wikiButton.isChecked() == True:
            language = self.language(first)
        elif self.fileButton.isChecked() == True:
            language = self.list_freq
        self.fill_table(first, language)

        self.textBrowser.setPlainText("".join(str(x) for x in first))

    def second(self):
        input = ""
        input = self.textEdit.toPlainText()
        input = input.lower()
        key = self.lineEdit_2.text()
        second = self.change(input, key)

        if self.wikiButton.isChecked() == True:
            language = self.language(second)
        elif self.fileButton.isChecked() == True:
            language = self.list_freq

        self.fill_table(second, language)
        self.textBrowser.setPlainText("".join(str(x) for x in second))


    def change(self, text, key):
        language = self.lang(text)
        res = ""
        for letter in text:
            if letter not in key:
                res += letter
            else:
                for el in key:
                    if letter == el:
                        res += language[key.index(el)]
        return res

    def dict_freq(self, language):
        # создаем список словарей для хранения букв и частот и заполняем частоты нулями
        dict_freq = {}
        for d in language:
            a = [*d]
            dict_freq[a[0]] = 0
        return dict_freq


    def language(self, input):
        # проверяем, какому языку принадлежит текст
        for d in self.Rus:
            if input[0] == list(d.keys())[0]:
                language = self.Rus

        for di in self.Eng:
            if input[0] == list(di.keys())[0]:
                language = self.Eng
        return language

    def lang(self, input):

        if input[0] in self.rusABC_lower:
            return self.rusABC_lower
        elif input[0] in self.engABC_lower:
            return self.engABC_lower
        else:
            return 0


    def open_freq(self):
        app = FileDialog.App()
        app.show()
        if app.path:
            with open(app.path, 'r') as f:
                self.text_freq = f.read()

    def open(self):
        app = FileDialog.App()
        app.show()
        if app.path:
            with open(app.path, encoding='utf-8') as f:
                text = f.read()
                self.textEdit.setPlainText("".join(str(x) for x in text))


    def save(self):
        app = FileDialog.App(1)
        app.show()
        if app.path:
            with open(app.path, 'w') as f:
                f.write(self.textBrowser.toPlainText())


    def saveFreq(self):
        a = ""
        for el in self.sorted_first:
            i = self.sorted_first.index(el)
            g = self.sorted_first[i][0]
            a += g
            a += " "
            o = el[1]
            a += str(o)
            a += ". "
        a = a[0:-2]
        self.save_(a)


    def save_(self, a):
        app = FileDialog.App(1)
        app.show()
        if app.path:
            with open(app.path, 'w') as f:
                f.write(a)

    def calc_lenght(self, text):
        lang = self.lang(text)
        res = 0
        for let in text:
            if let in lang:
                res += 1
        return res


    def clear(self):
        self.textEdit.clear()


    def get_key(self):
            key = self.pogreshnostBut.text()
            return key


    def show_msg(self, par):
        self.msg = QtWidgets.QMessageBox()
        if par == 0:
            self.msg.setText("Не те частоты!")
        elif par == 1:
            self.msg.setText("Некорректный входной текст!")
        self.msg.exec_()

    def show_msg_text(self, text):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(text)
        self.msg.exec_()