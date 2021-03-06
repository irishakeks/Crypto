import sys
from PyQt5 import QtWidgets
import mainDesign
import atbash,scytale, caesar, polib, Kardano, Rishelie, Rishelie2, Gronsefald, Vigener, Pleifer, Hill, \
    Vernam, Gammirovanie, Cryptoanal1
from Crypto import Alberti


class MainApp(QtWidgets.QMainWindow, mainDesign.Ui_MainWindow):
    def __init__(self,):
        super().__init__()
        self.setupUi(self)  # Инициализация нашего дизайна

        self.ciphers_values = [atbash, scytale, caesar, polib, Kardano, Rishelie, Rishelie2, Alberti, Gronsefald,
                               Vigener, Pleifer, Hill, Vernam, Gammirovanie, Cryptoanal1]
        self.ciphers_keys = ["Атбаш", "Скитала", "Цезаря", "Квадрат Полибия", "Решетка Кардано", "Шифр Ришелье",
                            "Шифр Ришелье 2.0", "Диск Альберти", "Шифр Гронсфельда", "Шифр Виженера", "Шифр Плейфера",
                             "Криптoсистема Хилла", "Шифр Вернама", 'Метод гаммирования', "Частотный криптоанализ"]
        self.ciphers_dict = dict(zip(self.ciphers_keys, self.ciphers_values))
        self.cipherLlistWidget.addItems(self.ciphers_keys)

        self.chooseCipherButton.clicked.connect(self.open_window)

    def open_window(self):
        cipher_name = self.cipherLlistWidget.currentItem().text()
        cipher_module = self.ciphers_dict[cipher_name]
        cipher = cipher_module.Cipher()
        cipher.show()
        cipher.exec_()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()

    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
