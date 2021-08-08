from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo, QSettings,QByteArray,QDataStream,QIODevice
import threading
from PyQt5.QtWidgets import QApplication, QWidget,\
    QVBoxLayout, QTableWidgetItem, QTableWidget,qApp
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 471)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Graphicloads-Flat-Finance-System-settings.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(13, 31, 56);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 931, 471))
        self.tableWidget.setStyleSheet("background-color:#f2f2f2;\n"
"border:none;\n"
"font: 9pt \"Segoe UI\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.th)
        self.pushButton.setGeometry(QtCore.QRect(940, 10, 181, 31))
        self.pushButton.setStyleSheet("QPushButton{background-color: rgb(2, 57, 132);\n"
"color:white;\n"
"border:none;\n"
"border-radius:3px;;\n"
"font: 9pt \"Segoe UI\";}\n"
"QPushButton::hover{\n"
"    border:3px solid rgb(13, 31, 56);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.clicked.connect(self.th12)
        self.pushButton_20.setGeometry(QtCore.QRect(940, 410, 181, 31))
        self.pushButton_20.setStyleSheet("QPushButton{background-color: rgb(2, 57, 132);\n"
                                      "color:white;\n"
                                      "border:none;\n"
                                      "border-radius:3px;;\n"
                                      "font: 9pt \"Segoe UI\";}\n"
                                      "QPushButton::hover{\n"
                                      "    border:3px solid rgb(13, 31, 56);\n"
                                      "}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.clicked.connect(self.th3)
        self.pushButton_8.setGeometry(QtCore.QRect(940, 370, 181, 31))
        self.pushButton_8.setStyleSheet("QPushButton{background-color: rgb(2, 57, 132);\n"
                                      "color:white;\n"
                                      "border:none;\n"
                                      "border-radius:3px;;\n"
                                      "font: 9pt \"Segoe UI\";}\n"
                                      "QPushButton::hover{\n"
                                      "    border:3px solid rgb(13, 31, 56);\n"
                                      "}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.clicked.connect(self.th4)
        self.pushButton_3.setGeometry(QtCore.QRect(940, 330, 181, 31))
        self.pushButton_3.setStyleSheet("QPushButton{background-color: rgb(2, 57, 132);\n"
"color:white;\n"
"border:none;\n"
"border-radius:3px;;\n"
"font: 9pt \"Segoe UI\";}\n"
"QPushButton::hover{\n"
"    border:3px solid rgb(13, 31, 56);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(940, 50, 181, 31))
        self.lineEdit.setStyleSheet("QLineEdit{background-color: #353e4a;\n"
"color:white;\n"
"border-radius:3px;\n"
"font: 9pt \"Segoe UI\";}\n"
"QLineEdit::before{\n"
"border:2px solid rgb(53, 62, 74);\n"
"}\n"
"QLineEdit::focus{\n"
"border:2px solid rgb(13, 31, 56);\n"
"border-radius:3px;\n"
"\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(940, 90, 181, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{background-color: #353e4a;\n"
"color:white;\n"
"border-radius:3px;\n"
"font: 9pt \"Segoe UI\";}\n"
"QLineEdit::before{\n"
"border:2px solid rgb(53, 62, 74);\n"
"}\n"
"QLineEdit::focus{\n"
"border:2px solid rgb(13, 31, 56);\n"
"border-radius:3px;\n"
"\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(940, 130, 181, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit{background-color: #353e4a;\n"
"color:white;\n"
"border-radius:3px;\n"
"font: 9pt \"Segoe UI\";}\n"
"QLineEdit::before{\n"
"border:2px solid rgb(53, 62, 74);\n"
"}\n"
"QLineEdit::focus{\n"
"border:2px solid rgb(13, 31, 56);\n"
"border-radius:3px;\n"
"\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(940, 170, 181, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit{background-color: #353e4a;\n"
"color:white;\n"
"border-radius:3px;\n"
"font: 9pt \"Segoe UI\";}\n"
"QLineEdit::before{\n"
"border:2px solid rgb(53, 62, 74);\n"
"}\n"
"QLineEdit::focus{\n"
"border:2px solid rgb(13, 31, 56);\n"
"border-radius:3px;\n"
"\n"
"}")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(940, 210, 181, 31))
        self.lineEdit_5.setStyleSheet("QLineEdit{background-color: #353e4a;\n"
"color:white;\n"
"border-radius:3px;\n"
"font: 9pt \"Segoe UI\";}\n"
"QLineEdit::before{\n"
"border:2px solid rgb(53, 62, 74);\n"
"}\n"
"QLineEdit::focus{\n"
"border:2px solid rgb(13, 31, 56);\n"
"border-radius:3px;\n"
"\n"
"}")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(940, 250, 181, 31))
        self.lineEdit_6.setStyleSheet("QLineEdit{background-color: #353e4a;\n"
"color:white;\n"
"border-radius:3px;\n"
"font: 9pt \"Segoe UI\";}\n"
"QLineEdit::before{\n"
"border:2px solid rgb(53, 62, 74);\n"
"}\n"
"QLineEdit::focus{\n"
"border:2px solid rgb(13, 31, 56);\n"
"border-radius:3px;\n"
"\n"
"}")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(940, 290, 181, 31))
        self.lineEdit_7.setStyleSheet("QLineEdit{background-color: #353e4a;\n"
"color:white;\n"
"border-radius:3px;\n"
"font: 9pt \"Segoe UI\";}\n"
"QLineEdit::before{\n"
"border:2px solid rgb(53, 62, 74);\n"
"}\n"
"QLineEdit::focus{\n"
"border:2px solid rgb(13, 31, 56);\n"
"border-radius:3px;\n"
"\n"
"}")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AliSystem"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date Create"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date Expire"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Note"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_20.setText(_translate("MainWindow", "Save Edit"))
        self.pushButton_3.setText(_translate("MainWindow", "Remove"))
        self.pushButton_8.setText(_translate("MainWindow", "Load Data"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Type . ."))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Email . ."))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Name . ."))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Password . ."))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Date Create . ."))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Date Expire . . ."))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Note . ."))
    def add_guest(self):
        fi = open("data.txt","a")
        x = str(self.lineEdit.text())
        y = str(self.lineEdit_2.text())
        z = str(self.lineEdit_3.text())
        z1 = str(self.lineEdit_4.text())
        z2 = str(self.lineEdit_5.text())
        z3 = str(self.lineEdit_6.text())
        z4 = str(self.lineEdit_7.text())
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)
        self.tableWidget.setItem(numRows, 0, QTableWidgetItem(x))
        self.tableWidget.setItem(numRows, 1, QTableWidgetItem(y))
        self.tableWidget.setItem(numRows, 2, QTableWidgetItem(z))
        self.tableWidget.setItem(numRows, 3, QTableWidgetItem(z1))
        self.tableWidget.setItem(numRows, 4, QTableWidgetItem(z2))
        self.tableWidget.setItem(numRows, 5, QTableWidgetItem(z3))
        self.tableWidget.setItem(numRows, 6, QTableWidgetItem(z4))
        fi.write(f"{x}:{y}:{z}:{z1}:{z2}:{z3}:{z4}\n")
    def th(self):
        h = threading.Thread(target=self.add_guest)
        h.start()
    def load(self):
        kk = open("data.txt","r").read().splitlines()
        for i in kk:
            type=i.split(":")[0]
            email = i.split(":")[1]
            name = i.split(":")[2]
            password = i.split(":")[3]
            date_create=i.split(":")[4]
            date_expire=i.split(":")[5]
            note = i.split(":")[6]
            numRows = self.tableWidget.rowCount()
            self.tableWidget.insertRow(numRows)
            self.tableWidget.setItem(numRows, 0, QTableWidgetItem(type))
            self.tableWidget.setItem(numRows, 1, QTableWidgetItem(email))
            self.tableWidget.setItem(numRows, 2, QTableWidgetItem(name))
            self.tableWidget.setItem(numRows, 3, QTableWidgetItem(password))
            self.tableWidget.setItem(numRows, 4, QTableWidgetItem(date_create))
            self.tableWidget.setItem(numRows, 5, QTableWidgetItem(date_expire))
            self.tableWidget.setItem(numRows, 6, QTableWidgetItem(note))
    def edit(self):
        fi = open("data.txt", "a")
        index = self.tableWidget.currentIndex()
        NewIndex = self.tableWidget.model().index(index.row(), 0)
        NewIndex1 = self.tableWidget.model().index(index.row(), 1)
        NewIndex2 = self.tableWidget.model().index(index.row(), 2)
        NewIndex3 = self.tableWidget.model().index(index.row(), 3)
        NewIndex4 = self.tableWidget.model().index(index.row(), 4)
        NewIndex5 = self.tableWidget.model().index(index.row(), 5)
        NewIndex6 = self.tableWidget.model().index(index.row(), 6)
        Name = self.tableWidget.model().data(NewIndex)
        Name1 = self.tableWidget.model().data(NewIndex1)
        Name2 = self.tableWidget.model().data(NewIndex2)
        Name3 = self.tableWidget.model().data(NewIndex3)
        Name4 = self.tableWidget.model().data(NewIndex4)
        Name5 = self.tableWidget.model().data(NewIndex5)
        Name6 = self.tableWidget.model().data(NewIndex6)
        rem = f"{Name}:{Name1}:{Name2}:{Name3}:{Name4}:{Name5}:{Name6}"
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)
        self.tableWidget.setItem(numRows, 0, QTableWidgetItem(Name))
        self.tableWidget.setItem(numRows, 1, QTableWidgetItem(Name1))
        self.tableWidget.setItem(numRows, 2, QTableWidgetItem(Name2))
        self.tableWidget.setItem(numRows, 3, QTableWidgetItem(Name3))
        self.tableWidget.setItem(numRows, 4, QTableWidgetItem(Name4))
        self.tableWidget.setItem(numRows, 5, QTableWidgetItem(Name5))
        self.tableWidget.setItem(numRows, 6, QTableWidgetItem(Name6))
        fi.write(f"{Name}:{Name1}:{Name2}:{Name3}:{Name4}:{Name5}:{Name6}\n")
        indices = self.tableWidget.selectionModel().selectedRows()
        for each_row in reversed(sorted(indices)):
            self.tableWidget.removeRow(each_row.row())
        x23 = self.tableWidget.currentRow()
        a_file = open("data.txt", "r")
        lines = a_file.readlines()
        a_file.close()
        del lines[x23]
        new_file = open("data.txt", "w+")
        for line in lines:
            new_file.write(line)
        new_file.close()

    def removeRow(self):
        index = self.tableWidget.currentIndex()
        NewIndex = self.tableWidget.model().index(index.row(), 0)
        NewIndex1 = self.tableWidget.model().index(index.row(), 1)
        NewIndex2= self.tableWidget.model().index(index.row(), 2)
        NewIndex3 = self.tableWidget.model().index(index.row(), 3)
        NewIndex4 = self.tableWidget.model().index(index.row(), 4)
        NewIndex5 = self.tableWidget.model().index(index.row(), 5)
        NewIndex6 = self.tableWidget.model().index(index.row(), 6)
        Name = self.tableWidget.model().data(NewIndex)
        Name1 = self.tableWidget.model().data(NewIndex1)
        Name2 = self.tableWidget.model().data(NewIndex2)
        Name3 = self.tableWidget.model().data(NewIndex3)
        Name4 = self.tableWidget.model().data(NewIndex4)
        Name5 = self.tableWidget.model().data(NewIndex5)
        Name6 = self.tableWidget.model().data(NewIndex6)
        rem=f"{Name}:{Name1}:{Name2}:{Name3}:{Name4}:{Name5}:{Name6}"
        a_file = open("data.txt", "r")
        lines = a_file.readlines()
        a_file.close()
        new_file = open("data.txt", "w")
        for line in lines:
            if line.strip("\n") != rem:
                new_file.write(line)
        new_file.close()
        indices = self.tableWidget.selectionModel().selectedRows()
        for each_row in reversed(sorted(indices)):
            self.tableWidget.removeRow(each_row.row())
    def th4(self):
        th4=threading.Thread(target=self.removeRow)
        th4.start()
    def th3(self):
        th3 = threading.Thread(target=self.load)
        th3.start()
    def th12(self):
        th12=threading.Thread(target=self.edit)
        th12.start()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
