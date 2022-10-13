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

        self.ui.btn_1.clicked.connect(lambda: self.ui.lineEdit.insert('1')
                                      if self.ui.lineEdit.hasFocus() else self.ui.lineEdit_2.insert('1'))
        self.ui.btn_2.clicked.connect(lambda: self.ui.lineEdit.insert('2')
                                      if self.ui.lineEdit.hasFocus() else self.ui.lineEdit_2.insert('2'))
        self.ui.btn_3.clicked.connect(lambda: self.ui.lineEdit.insert('3')
                                      if self.ui.lineEdit.hasFocus() else self.ui.lineEdit_2.insert('3'))
        self.ui.btn_4.clicked.connect(lambda: self.ui.lineEdit.insert('4')
                                      if self.ui.lineEdit.hasFocus() else self.ui.lineEdit_2.insert('4'))
        self.ui.btn_5.clicked.connect(lambda: self.ui.lineEdit.insert('5')
                                      if self.ui.lineEdit.hasFocus() else self.ui.lineEdit_2.insert('5'))
        self.ui.btn_6.clicked.connect(lambda: self.ui.lineEdit.insert('6')
                                      if self.ui.lineEdit.hasFocus() else self.ui.lineEdit_2.insert('6'))
        self.ui.btn_7.clicked.connect(lambda: self.ui.lineEdit.insert('7')
                                      if self.ui.lineEdit.hasFocus() else self.ui.lineEdit_2.insert('7'))
        self.ui.btn_8.clicked.connect(lambda: self.ui.lineEdit.insert('8')
                                      if self.ui.lineEdit.hasFocus() else self.ui.lineEdit_2.insert('8'))
        self.ui.btn_9.clicked.connect(lambda: self.ui.lineEdit.insert('9')
                                      if self.ui.lineEdit.hasFocus() else self.ui.lineEdit_2.insert('9'))
        self.ui.btn_zerro.clicked.connect(lambda: self.ui.lineEdit.insert('0')
                                          if self.ui.lineEdit.hasFocus() else self.ui.lineEdit_2.insert('0'))
        self.ui.btn_tochka.clicked.connect(lambda: self.ui.lineEdit.insert('.')
                                           if self.ui.lineEdit.hasFocus() else self.ui.lineEdit_2.insert('.'))
        self.ui.ereise_button.clicked.connect(lambda: self.ui.lineEdit.backspace()
                                              if self.ui.lineEdit.hasFocus() else self.ui.lineEdit_2.backspace())

        self.ui.clear_button.clicked.connect(lambda: self.ui.lineEdit.clear())
        self.ui.clear_button.clicked.connect(lambda: self.ui.lineEdit_2.clear())
        self.ui.clear_button.clicked.connect(lambda: self.ui.lineEdit_3.clear())
        self.ui.clear_button.clicked.connect(lambda: self.ui.lineEdit_4.clear())
        self.ui.clear_button.clicked.connect(lambda: self.ui.lineEdit_5.clear())
        self.ui.clear_button.clicked.connect(lambda: self.ui.lineEdit.setFocus())

    def calculation(self):
        # We calculate the cost per year, month and day with rounding to two digits
        # and pass the value to the appropriate fields.
        try:
            inupt_number1 = float(self.ui.lineEdit.text())
            inupt_number2 = int(self.ui.lineEdit_2.text())
            cost_year = round((inupt_number1 / inupt_number2), 2)
            cost_month = round((inupt_number1 / inupt_number2 / 12), 2)
            cost_day = round((inupt_number1 / inupt_number2 / 365), 2)
            self.ui.lineEdit_3.setText(str(cost_year))
            self.ui.lineEdit_4.setText(str(cost_month))
            self.ui.lineEdit_5.setText(str(cost_day))
        except ZeroDivisionError:
            self.ui.lineEdit_3.setText('"This is unacceptable."')
        except ValueError:
            self.ui.lineEdit_3.setText('"Only integer."')


app = QtWidgets.QApplication([])
application = MainProject()
application.show()
sys.exit(app.exec())
