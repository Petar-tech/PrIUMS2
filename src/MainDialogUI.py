# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainDialogUI(object):
    def setupUi(self, MainDialogUI):
        MainDialogUI.setObjectName("MainDialogUI")
        MainDialogUI.resize(175, 222)
        MainDialogUI.setMinimumSize(QtCore.QSize(175, 222))
        MainDialogUI.setMaximumSize(QtCore.QSize(175, 222))
        self.gridLayout = QtWidgets.QGridLayout(MainDialogUI)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.portBox = QtWidgets.QComboBox(MainDialogUI)
        self.portBox.setObjectName("portBox")
        self.verticalLayout.addWidget(self.portBox)
        self.baudrateBox = QtWidgets.QComboBox(MainDialogUI)
        self.baudrateBox.setObjectName("baudrateBox")
        self.baudrateBox.addItem("")
        self.baudrateBox.addItem("")
        self.baudrateBox.addItem("")
        self.baudrateBox.addItem("")
        self.verticalLayout.addWidget(self.baudrateBox)
        self.parityBox = QtWidgets.QComboBox(MainDialogUI)
        self.parityBox.setObjectName("parityBox")
        self.parityBox.addItem("")
        self.parityBox.addItem("")
        self.parityBox.addItem("")
        self.parityBox.addItem("")
        self.parityBox.addItem("")
        self.verticalLayout.addWidget(self.parityBox)
        self.databitsBox = QtWidgets.QComboBox(MainDialogUI)
        self.databitsBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.databitsBox.setObjectName("databitsBox")
        self.databitsBox.addItem("")
        self.databitsBox.addItem("")
        self.databitsBox.addItem("")
        self.databitsBox.addItem("")
        self.verticalLayout.addWidget(self.databitsBox)
        self.stopbitBox = QtWidgets.QComboBox(MainDialogUI)
        self.stopbitBox.setObjectName("stopbitBox")
        self.stopbitBox.addItem("")
        self.stopbitBox.addItem("")
        self.stopbitBox.addItem("")
        self.verticalLayout.addWidget(self.stopbitBox)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.portLabel = QtWidgets.QLabel(MainDialogUI)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.portLabel.setFont(font)
        self.portLabel.setAutoFillBackground(False)
        self.portLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.portLabel.setObjectName("portLabel")
        self.verticalLayout_2.addWidget(self.portLabel)
        self.baudrateLabel = QtWidgets.QLabel(MainDialogUI)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.baudrateLabel.setFont(font)
        self.baudrateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.baudrateLabel.setObjectName("baudrateLabel")
        self.verticalLayout_2.addWidget(self.baudrateLabel)
        self.parityLabel = QtWidgets.QLabel(MainDialogUI)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.parityLabel.setFont(font)
        self.parityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.parityLabel.setObjectName("parityLabel")
        self.verticalLayout_2.addWidget(self.parityLabel)
        self.databitsLabel = QtWidgets.QLabel(MainDialogUI)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.databitsLabel.setFont(font)
        self.databitsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.databitsLabel.setObjectName("databitsLabel")
        self.verticalLayout_2.addWidget(self.databitsLabel)
        self.stopbitLabel = QtWidgets.QLabel(MainDialogUI)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.stopbitLabel.setFont(font)
        self.stopbitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stopbitLabel.setObjectName("stopbitLabel")
        self.verticalLayout_2.addWidget(self.stopbitLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(MainDialogUI)
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.gridLayout.addWidget(self.dialogButtonBox, 1, 0, 1, 2)

        self.retranslateUi(MainDialogUI)
        self.dialogButtonBox.accepted.connect(MainDialogUI.accept)
        self.dialogButtonBox.rejected.connect(MainDialogUI.reject)
        QtCore.QMetaObject.connectSlotsByName(MainDialogUI)

    def retranslateUi(self, MainDialogUI):
        _translate = QtCore.QCoreApplication.translate
        MainDialogUI.setWindowTitle(_translate("MainDialogUI", "Dialog"))
        self.baudrateBox.setItemText(0, _translate("MainDialogUI", "9600"))
        self.baudrateBox.setItemText(1, _translate("MainDialogUI", "19200"))
        self.baudrateBox.setItemText(2, _translate("MainDialogUI", "57600"))
        self.baudrateBox.setItemText(3, _translate("MainDialogUI", "115200"))
        self.parityBox.setItemText(0, _translate("MainDialogUI", "None"))
        self.parityBox.setItemText(1, _translate("MainDialogUI", "Odd"))
        self.parityBox.setItemText(2, _translate("MainDialogUI", "Even"))
        self.parityBox.setItemText(3, _translate("MainDialogUI", "Mark"))
        self.parityBox.setItemText(4, _translate("MainDialogUI", "Space"))
        self.databitsBox.setCurrentText(_translate("MainDialogUI", "8"))
        self.databitsBox.setItemText(0, _translate("MainDialogUI", "5"))
        self.databitsBox.setItemText(1, _translate("MainDialogUI", "6"))
        self.databitsBox.setItemText(2, _translate("MainDialogUI", "7"))
        self.databitsBox.setItemText(3, _translate("MainDialogUI", "8"))
        self.stopbitBox.setItemText(0, _translate("MainDialogUI", "1"))
        self.stopbitBox.setItemText(1, _translate("MainDialogUI", "1.5"))
        self.stopbitBox.setItemText(2, _translate("MainDialogUI", "2"))
        self.portLabel.setText(_translate("MainDialogUI", "Port:"))
        self.baudrateLabel.setText(_translate("MainDialogUI", "Baud rate:"))
        self.parityLabel.setText(_translate("MainDialogUI", "Parity:"))
        self.databitsLabel.setText(_translate("MainDialogUI", "Data bits:"))
        self.stopbitLabel.setText(_translate("MainDialogUI", "Stop bit:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainDialogUI = QtWidgets.QDialog()
    ui = Ui_MainDialogUI()
    ui.setupUi(MainDialogUI)
    MainDialogUI.show()
    sys.exit(app.exec_())
