from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *
from PySide2 import QtCore, QtGui, QtWidgets


class MP2X_R_Demand(QWidget):
    def __init__(self,Panel_ID, nodename):
        super(MP2X_R_Demand, self).__init__()

        self.id = Panel_ID
        self.nodename = nodename
        #self.setObjectName("self")
        #self.resize(112, 521)
        self.setFixedSize(112, 521)
        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(30, 100, 21, 31))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("button.png"))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(50, 100, 21, 31))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("button.png"))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(30, 120, 21, 31))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("button.png"))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(50, 120, 21, 31))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("button.png"))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self)
        self.label_14.setGeometry(QtCore.QRect(50, 160, 21, 31))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("button.png"))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self)
        self.label_15.setGeometry(QtCore.QRect(50, 140, 21, 31))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("button.png"))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self)
        self.label_16.setGeometry(QtCore.QRect(30, 160, 21, 31))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("button.png"))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self)
        self.label_17.setGeometry(QtCore.QRect(30, 140, 21, 31))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("button.png"))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self)
        self.label_18.setGeometry(QtCore.QRect(50, 200, 21, 31))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("button.png"))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self)
        self.label_19.setGeometry(QtCore.QRect(50, 180, 21, 31))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("button.png"))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self)
        self.label_20.setGeometry(QtCore.QRect(30, 200, 21, 31))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("button.png"))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self)
        self.label_21.setGeometry(QtCore.QRect(30, 180, 21, 31))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("button.png"))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self)
        self.label_22.setGeometry(QtCore.QRect(50, 240, 21, 31))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("button.png"))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self)
        self.label_23.setGeometry(QtCore.QRect(50, 220, 21, 31))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("button.png"))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self)
        self.label_24.setGeometry(QtCore.QRect(30, 240, 21, 31))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("button.png"))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self)
        self.label_25.setGeometry(QtCore.QRect(30, 220, 21, 31))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("button.png"))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self)
        self.label_26.setGeometry(QtCore.QRect(50, 280, 21, 31))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("button.png"))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self)
        self.label_27.setGeometry(QtCore.QRect(50, 260, 21, 31))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("button.png"))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self)
        self.label_28.setGeometry(QtCore.QRect(30, 280, 21, 31))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("button.png"))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self)
        self.label_29.setGeometry(QtCore.QRect(30, 260, 21, 31))
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("button.png"))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self)
        self.label_30.setGeometry(QtCore.QRect(50, 320, 21, 31))
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("button.png"))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self)
        self.label_31.setGeometry(QtCore.QRect(50, 300, 21, 31))
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap("button.png"))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self)
        self.label_32.setGeometry(QtCore.QRect(30, 320, 21, 31))
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap("button.png"))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self)
        self.label_33.setGeometry(QtCore.QRect(30, 300, 21, 31))
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("button.png"))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self)
        self.label_34.setGeometry(QtCore.QRect(50, 360, 21, 31))
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap("button.png"))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self)
        self.label_35.setGeometry(QtCore.QRect(50, 340, 21, 31))
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("button.png"))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self)
        self.label_36.setGeometry(QtCore.QRect(30, 360, 21, 31))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap("button.png"))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self)
        self.label_37.setGeometry(QtCore.QRect(30, 340, 21, 31))
        self.label_37.setText("")
        self.label_37.setPixmap(QtGui.QPixmap("button.png"))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self)
        self.label_38.setGeometry(QtCore.QRect(50, 400, 21, 31))
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap("button.png"))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self)
        self.label_39.setGeometry(QtCore.QRect(50, 380, 21, 31))
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap("button.png"))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self)
        self.label_40.setGeometry(QtCore.QRect(30, 400, 21, 31))
        self.label_40.setText("")
        self.label_40.setPixmap(QtGui.QPixmap("button.png"))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self)
        self.label_41.setGeometry(QtCore.QRect(30, 380, 21, 31))
        self.label_41.setText("")
        self.label_41.setPixmap(QtGui.QPixmap("button.png"))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self)
        self.label_42.setGeometry(QtCore.QRect(50, 440, 21, 31))
        self.label_42.setText("")
        self.label_42.setPixmap(QtGui.QPixmap("button.png"))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self)
        self.label_43.setGeometry(QtCore.QRect(50, 420, 21, 31))
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap("button.png"))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self)
        self.label_44.setGeometry(QtCore.QRect(30, 440, 21, 31))
        self.label_44.setText("")
        self.label_44.setPixmap(QtGui.QPixmap("button.png"))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self)
        self.label_45.setGeometry(QtCore.QRect(30, 420, 21, 31))
        self.label_45.setText("")
        self.label_45.setPixmap(QtGui.QPixmap("button.png"))
        self.label_45.setObjectName("label_45")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 110, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(70, 130, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(70, 150, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(70, 190, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(70, 210, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(70, 230, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(70, 250, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(70, 270, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_46 = QtWidgets.QLabel(self)
        self.label_46.setGeometry(QtCore.QRect(70, 290, 55, 16))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self)
        self.label_47.setGeometry(QtCore.QRect(70, 310, 55, 16))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self)
        self.label_48.setGeometry(QtCore.QRect(70, 330, 55, 16))
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self)
        self.label_49.setGeometry(QtCore.QRect(70, 350, 55, 16))
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self)
        self.label_50.setGeometry(QtCore.QRect(70, 370, 55, 16))
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self)
        self.label_51.setGeometry(QtCore.QRect(70, 390, 55, 16))
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self)
        self.label_52.setGeometry(QtCore.QRect(70, 410, 55, 16))
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self)
        self.label_53.setGeometry(QtCore.QRect(70, 430, 55, 16))
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self)
        self.label_54.setGeometry(QtCore.QRect(70, 450, 55, 16))
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self)
        self.label_55.setGeometry(QtCore.QRect(30, 40, 21, 31))
        self.label_55.setText("")
        self.label_55.setPixmap(QtGui.QPixmap("button.png"))
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self)
        self.label_56.setGeometry(QtCore.QRect(30, 20, 21, 31))
        self.label_56.setText("")
        self.label_56.setPixmap(QtGui.QPixmap("button.png"))
        self.label_56.setObjectName("label_56")
        self.label_58 = QtWidgets.QLabel(self)
        self.label_58.setGeometry(QtCore.QRect(50, 30, 55, 16))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self)
        self.label_59.setGeometry(QtCore.QRect(10, 40, 21, 31))
        self.label_59.setText("")
        self.label_59.setPixmap(QtGui.QPixmap("button.png"))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self)
        self.label_60.setGeometry(QtCore.QRect(50, 50, 55, 16))
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self)
        self.label_61.setGeometry(QtCore.QRect(10, 20, 21, 31))
        self.label_61.setText("")
        self.label_61.setPixmap(QtGui.QPixmap("button.png"))
        self.label_61.setObjectName("label_61")
        self.label_57 = QtWidgets.QLabel(self)
        self.label_57.setGeometry(QtCore.QRect(40, 470, 55, 16))
        self.label_57.setText("")
        self.label_57.setPixmap(QtGui.QPixmap("CH.png"))
        self.label_57.setObjectName("label_57")
        self.label_62 = QtWidgets.QLabel(self)
        self.label_62.setGeometry(QtCore.QRect(40, 490, 55, 16))
        self.label_62.setText("")
        self.label_62.setPixmap(QtGui.QPixmap("CH.png"))
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self)
        self.label_63.setGeometry(QtCore.QRect(0, 470, 55, 16))
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self)
        self.label_64.setGeometry(QtCore.QRect(0, 490, 55, 16))
        self.label_64.setObjectName("label_64")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setAcceptDrops(True)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label.setText(_translate("self", "ACT"))
        self.label_2.setText(_translate("self", "FAIL"))
        self.label_3.setText(_translate("self", "ACT"))
        self.label_4.setText(_translate("self", "FAIL"))
        self.label_5.setText(_translate("self", "ACT"))
        self.label_6.setText(_translate("self", "FAIL"))
        self.label_7.setText(_translate("self", "ACT"))
        self.label_8.setText(_translate("self", "FAIL"))
        self.label_9.setText(_translate("self", "ACT"))
        self.label_46.setText(_translate("self", "FAIL"))
        self.label_47.setText(_translate("self", "ACT"))
        self.label_48.setText(_translate("self", "FAIL"))
        self.label_49.setText(_translate("self", "ACT"))
        self.label_50.setText(_translate("self", "FAIL"))
        self.label_51.setText(_translate("self", "ACT"))
        self.label_52.setText(_translate("self", "FAIL"))
        self.label_53.setText(_translate("self", "ACT"))
        self.label_54.setText(_translate("self", "FAIL"))
        self.label_58.setText(_translate("self", "ACT"))
        self.label_60.setText(_translate("self", "FAIL"))
        self.label_63.setText(_translate("self", "CH1"))
        self.label_64.setText(_translate("self", "CH2"))

