from PyQt5.QtWidgets import QDialog
from MainDialogUI import *
from serial.tools import list_ports
from serial import *


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog = Ui_MainDialogUI()
        self.dialog.setupUi(self)
        self.dialog.databitsBox.setCurrentIndex(3)
        self.dialog.parityBox.setCurrentIndex(2)

        self.comDict = {}
        coms = list_ports.comports()

        for com in coms:
            self.dialog.portBox.addItem(str(com.device))

    def get_data(self):
        self.comDict["com_port"] = self.dialog.portBox.currentText()
        self.comDict["baud_rate"] = int(self.dialog.baudrateBox.currentText())
        tmp = self.dialog.databitsBox.currentText()
        if tmp == "5":
            self.comDict["data_bits"] = FIVEBITS
        if tmp == "6":
            self.comDict["data_bits"] = SIXBITS
        if tmp == "7":
            self.comDict["data_bits"] = SEVENBITS
        if tmp == "8":
            self.comDict["data_bits"] = EIGHTBITS

        tmp = self.dialog.parityBox.currentText()
        if tmp == "None":
            self.comDict["parity"] = PARITY_NONE
        if tmp == "Even":
            self.comDict["parity"] = PARITY_EVEN
        if tmp == "Mark":
            self.comDict["parity"] = PARITY_MARK
        if tmp == "Space":
            self.comDict["parity"] = PARITY_SPACE
        if tmp == "Odd":
            self.comDict["parity"] = PARITY_ODD

        tmp = self.dialog.stopbitBox.currentText()
        if tmp == "1":
            self.comDict["stop_bit"] = STOPBITS_ONE
        if tmp == "1.5":
            self.comDict["stop_bit"] = STOPBITS_ONE_POINT_FIVE
        if tmp == "2":
            self.comDict["stop_bit"] = STOPBITS_TWO

        return self.comDict

