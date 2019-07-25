# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UltimateSerial_UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

class SerialController(QWidget):
    BAUDRATES = (
        QSerialPort.Baud1200,
        QSerialPort.Baud2400,
        QSerialPort.Baud4800,
        QSerialPort.Baud9600,
        QSerialPort.Baud19200,
        QSerialPort.Baud38400,
        QSerialPort.Baud57600,
        QSerialPort.Baud115200,
    )

    def __init__(self):
        QWidget.__init__(self)



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1079, 618)
        self.PortList_Fir = QtWidgets.QListWidget(Form)
        self.PortList_Fir.setGeometry(QtCore.QRect(10, 30, 131, 71))
        self.PortList_Fir.setObjectName("PortList_Fir")
        self.PortOpenBtn_Fir = QtWidgets.QPushButton(Form)
        self.PortOpenBtn_Fir.setGeometry(QtCore.QRect(150, 60, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PortOpenBtn_Fir.setFont(font)
        self.PortOpenBtn_Fir.setObjectName("PortOpenBtn_Fir")
        self.RX_TextView_Fir = QtWidgets.QTextBrowser(Form)
        self.RX_TextView_Fir.setGeometry(QtCore.QRect(10, 120, 521, 441))
        self.RX_TextView_Fir.setObjectName("RX_TextView_Fir")
        self.Tx_TextEdit_Fir = QtWidgets.QTextEdit(Form)
        self.Tx_TextEdit_Fir.setGeometry(QtCore.QRect(10, 580, 431, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tx_TextEdit_Fir.sizePolicy().hasHeightForWidth())
        self.Tx_TextEdit_Fir.setSizePolicy(sizePolicy)
        self.Tx_TextEdit_Fir.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Tx_TextEdit_Fir.setFont(font)
        self.Tx_TextEdit_Fir.setObjectName("Tx_TextEdit_Fir")
        self.SendBtn_Fir = QtWidgets.QPushButton(Form)
        self.SendBtn_Fir.setGeometry(QtCore.QRect(450, 580, 81, 27))
        self.SendBtn_Fir.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SendBtn_Fir.setFont(font)
        self.SendBtn_Fir.setObjectName("SendBtn_Fir")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 560, 81, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.PortOpenBtn_Sec = QtWidgets.QPushButton(Form)
        self.PortOpenBtn_Sec.setGeometry(QtCore.QRect(680, 60, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PortOpenBtn_Sec.setFont(font)
        self.PortOpenBtn_Sec.setObjectName("PortOpenBtn_Sec")
        self.TX_TextEdit_Sec = QtWidgets.QTextEdit(Form)
        self.TX_TextEdit_Sec.setGeometry(QtCore.QRect(550, 580, 431, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TX_TextEdit_Sec.sizePolicy().hasHeightForWidth())
        self.TX_TextEdit_Sec.setSizePolicy(sizePolicy)
        self.TX_TextEdit_Sec.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TX_TextEdit_Sec.setFont(font)
        self.TX_TextEdit_Sec.setObjectName("TX_TextEdit_Sec")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(560, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.PortList_Sec = QtWidgets.QListWidget(Form)
        self.PortList_Sec.setGeometry(QtCore.QRect(550, 30, 121, 71))
        self.PortList_Sec.setObjectName("PortList_Sec")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(560, 560, 81, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.SendBtn_Sec = QtWidgets.QPushButton(Form)
        self.SendBtn_Sec.setGeometry(QtCore.QRect(990, 580, 81, 27))
        self.SendBtn_Sec.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SendBtn_Sec.setFont(font)
        self.SendBtn_Sec.setObjectName("SendBtn_Sec")
        self.RX_TextView_Sec = QtWidgets.QTextBrowser(Form)
        self.RX_TextView_Sec.setGeometry(QtCore.QRect(550, 120, 521, 441))
        self.RX_TextView_Sec.setObjectName("RX_TextView_Sec")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(560, 100, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.BaudrateCombo_Fir = QtWidgets.QComboBox(Form)
        self.BaudrateCombo_Fir.setGeometry(QtCore.QRect(150, 30, 121, 22))
        self.BaudrateCombo_Fir.setObjectName("BaudrateCombo_Fir")
        self.BaudrateCombo_Sec = QtWidgets.QComboBox(Form)
        self.BaudrateCombo_Sec.setGeometry(QtCore.QRect(680, 30, 121, 22))
        self.BaudrateCombo_Sec.setObjectName("BaudrateCombo_Sec")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(160, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(690, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ultimate Serial by JY"))
        self.PortOpenBtn_Fir.setText(_translate("Form", "OPEN"))
        self.SendBtn_Fir.setText(_translate("Form", "SEND"))
        self.label.setText(_translate("Form", "TX Data"))
        self.label_2.setText(_translate("Form", "RX Data"))
        self.label_3.setText(_translate("Form", "PORT"))
        self.PortOpenBtn_Sec.setText(_translate("Form", "OPEN"))
        self.label_4.setText(_translate("Form", "PORT"))
        self.label_5.setText(_translate("Form", "TX Data"))
        self.SendBtn_Sec.setText(_translate("Form", "SEND"))
        self.label_6.setText(_translate("Form", "RX Data"))
        self.label_7.setText(_translate("Form", "Baudrate"))
        self.label_8.setText(_translate("Form", "Baudrate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

