import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow


class MainProject(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainProject, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        # Setting the icon of the main window and
        #  binding the input key to perform functions.
        self.setWindowIcon(QIcon('electronics_chip_wireless_gadget_smart_icon_229600.ico'))
        self.ui.btn_ravno.clicked.connect(self.calculation)
        self.ui.btn_1.clicked.connect(self.clik_1)
        self.ui.btn_2.clicked.connect(self.clik_2)
        self.ui.btn_3.clicked.connect(self.clik_3)
        self.ui.btn_4.clicked.connect(self.clik_4)
        self.ui.btn_5.clicked.connect(self.clik_5)
        self.ui.btn_6.clicked.connect(self.clik_6)
        self.ui.btn_7.clicked.connect(self.clik_7)
        self.ui.btn_8.clicked.connect(self.clik_8)
        self.ui.btn_9.clicked.connect(self.clik_9)
        self.ui.btn_zerro.clicked.connect(self.clik_0)
        self.ui.btn_tochka.clicked.connect(self.clik_point)
        self.ui.ereise_button.clicked.connect(self.clik_backspace)
        self.ui.clear_button.clicked.connect(lambda: self.ui.lineEdit.clear())
        self.ui.clear_button.clicked.connect(lambda: self.ui.lineEdit_2.clear())
        self.ui.clear_button.clicked.connect(lambda: self.ui.lineEdit_3.clear())
        self.ui.clear_button.clicked.connect(lambda: self.ui.lineEdit_4.clear())
        self.ui.clear_button.clicked.connect(lambda: self.ui.lineEdit_5.clear())
        self.ui.clear_button.clicked.connect(lambda: self.ui.lineEdit.setFocus())

    def clik_1(self):

        if self.ui.lineEdit.hasFocus():
            self.ui.lineEdit.insert('1')
        elif self.ui.lineEdit_2.hasFocus():
            self.ui.lineEdit_2.insert('1')
        else:
            self.ui.lineEdit_3.insert('1')

    def clik_2(self):
        if self.ui.lineEdit.hasFocus():
            self.ui.lineEdit.insert('2')
        elif self.ui.lineEdit_2.hasFocus():
            self.ui.lineEdit_2.insert('2')
        else:
            self.ui.lineEdit_3.insert('2')

    def clik_3(self):
        if self.ui.lineEdit.hasFocus():
            self.ui.lineEdit.insert('3')
        elif self.ui.lineEdit_2.hasFocus():
            self.ui.lineEdit_2.insert('3')
        else:
            self.ui.lineEdit_3.insert('3')

    def clik_4(self):
        if self.ui.lineEdit.hasFocus():
            self.ui.lineEdit.insert('4')
        elif self.ui.lineEdit_2.hasFocus():
            self.ui.lineEdit_2.insert('4')
        else:
            self.ui.lineEdit_3.insert('4')

    def clik_5(self):
        if self.ui.lineEdit.hasFocus():
            self.ui.lineEdit.insert('5')
        elif self.ui.lineEdit_2.hasFocus():
            self.ui.lineEdit_2.insert('5')
        else:
            self.ui.lineEdit_3.insert('5')

    def clik_6(self):
        if self.ui.lineEdit.hasFocus():
            self.ui.lineEdit.insert('6')
        elif self.ui.lineEdit_2.hasFocus():
            self.ui.lineEdit_2.insert('6')
        else:
            self.ui.lineEdit_3.insert('6')

    def clik_7(self):
        if self.ui.lineEdit.hasFocus():
            self.ui.lineEdit.insert('7')
        elif self.ui.lineEdit_2.hasFocus():
            self.ui.lineEdit_2.insert('7')
        else:
            self.ui.lineEdit_3.insert('7')

    def clik_8(self):
        if self.ui.lineEdit.hasFocus():
            self.ui.lineEdit.insert('8')
        elif self.ui.lineEdit_2.hasFocus():
            self.ui.lineEdit_2.insert('8')
        else:
            self.ui.lineEdit_3.insert('8')

    def clik_9(self):
        if self.ui.lineEdit.hasFocus():
            self.ui.lineEdit.insert('9')
        elif self.ui.lineEdit_2.hasFocus():
            self.ui.lineEdit_2.insert('9')
        else:
            self.ui.lineEdit_3.insert('9')

    def clik_0(self):
        if self.ui.lineEdit.hasFocus():
            self.ui.lineEdit.insert('0')
        elif self.ui.lineEdit_2.hasFocus():
            self.ui.lineEdit_2.insert('0')
        else:
            self.ui.lineEdit_3.insert('0')

    def clik_point(self):
        if self.ui.lineEdit.hasFocus():
            self.ui.lineEdit.insert('.')
        elif self.ui.lineEdit_2.hasFocus():
            self.ui.lineEdit_2.insert('.')
        else:
            self.ui.lineEdit_3.insert('.')

    def clik_backspace(self):
        if self.ui.lineEdit.hasFocus():
            self.ui.lineEdit.backspace()
        elif self.ui.lineEdit_2.hasFocus():
            self.ui.lineEdit_2.backspace()
        else:
            self.ui.lineEdit_3.backspace()

    def calculation(self):

        try:
            x = float(self.ui.lineEdit.text())  # Amount of credit
            y = float(self.ui.lineEdit_2.text())  # Credit period
            z = float(self.ui.lineEdit_3.text())  # Percent
            z = z / 1200
            j = x * z
            a = (1 + z) ** y
            s = 1 - (1 / a)
            d = round(j / s, 2)

            overpayment_on_the_loan = round(d * y - x, 2)

            self.ui.lineEdit_4.setText(str(d))
            self.ui.lineEdit_5.setText(str(overpayment_on_the_loan))

        except ZeroDivisionError:
            self.ui.lineEdit_4.setText('"This is unacceptable."')
        except ValueError:
            self.ui.lineEdit_4.setText('"Only integer."')


app = QtWidgets.QApplication([])
application = MainProject()
application.show()
sys.exit(app.exec())
