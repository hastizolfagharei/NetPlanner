# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TP1H_R.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(112, 521)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(20, 230, 55, 16))
        self.label_12.setObjectName("label_12")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 230, 31, 16))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../MP1H/button.png"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 210, 31, 16))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../MP1H/button.png"))
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(20, 210, 55, 16))
        self.label_11.setObjectName("label_11")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 380, 31, 16))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../MP1H/button.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 360, 31, 16))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../MP1H/button.png"))
        self.label_4.setObjectName("label_4")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(20, 360, 55, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(20, 380, 55, 16))
        self.label_14.setObjectName("label_14")
        self.label_29 = QtWidgets.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(30, 70, 55, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(20, 80, 31, 16))
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("../MP1H/button.png"))
        self.label_30.setObjectName("label_30")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(30, 60, 55, 16))
        self.label_27.setObjectName("label_27")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(20, 70, 31, 16))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("../MP1H/button.png"))
        self.label_26.setObjectName("label_26")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.label_31.setObjectName("label_31")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(20, 60, 31, 16))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("../MP1H/button.png"))
        self.label_28.setObjectName("label_28")
        self.label_61 = QtWidgets.QLabel(Form)
        self.label_61.setGeometry(QtCore.QRect(30, 330, 55, 16))
        self.label_61.setText("")
        self.label_61.setPixmap(QtGui.QPixmap("../../NetPlanner/MP2X_panel/CH.png"))
        self.label_61.setObjectName("label_61")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(10, 330, 55, 16))
        self.label_25.setObjectName("label_25")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:6pt;\">SF</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:6pt;\">SF</span></p></body></html>"))
        self.label_29.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:6pt;\">FAIL</span></p></body></html>"))
        self.label_27.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:6pt;\">ACT</span></p></body></html>"))
        self.label_31.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:6pt;\">W/P</span></p></body></html>"))
        self.label_25.setText(_translate("Form", "CH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
