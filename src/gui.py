from MainWindowUI import *
from MainDialog import *
from threads.communication import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QGridLayout
from PyQt5.QtCore import QThread, pyqtSignal
from threads.graph import MyGraphThread
from threads.db import MyDBThread


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.port.setText("None")
        self.ui.baudrate.setText("None")
        self.ui.parity.setText("None")
        self.ui.stopbit.setText("None")
        self.ui.databits.setText("None")
        self.current_data = None

        self.ui.startButton.clicked.connect(self.open_com)
        self.ui.stopButton.clicked.connect(self.close_com)

        self.ui.stopButton.setEnabled(False)

        self.ui.actionUART.triggered.connect(self.uart)

    def uart(self):
        self.settings = MainDialog()
        response = self.settings.exec_()

        if response:
            self.current_data = self.settings.get_data()

            self.ui.port.setText(self.current_data.get("com_port"))
            self.ui.baudrate.setText(str(self.current_data.get("baud_rate")))
            self.ui.parity.setText(str(self.current_data.get("parity")))
            self.ui.databits.setText(str(self.current_data.get("data_bits")))
            self.ui.stopbit.setText(str(self.current_data.get("stop_bit")))

            self.ui.startButton.setEnabled(True)
            self.ui.stopButton.setEnabled(False)
        else:
            self.current_data = None

    def open_com(self):
        if self.ui.unitBox.currentText() == "None":
            self.error()
            return

        self.com_thread = ComThread(self.current_data)
        self.graph_thread = MyGraphThread(tabPlot=self.ui.tab_2)
        self.db_thread = MyDBThread()

        self.com_thread.change_value.connect(self.get_data)
        self.com_thread.error.connect(self.error)
        self.graph_thread.data.connect(self.get_data)
        self.db_thread.db.connect(self.get_data)
        self.ui.startButton.setEnabled(False)
        self.ui.stopButton.setEnabled(True)

        self.com_thread.start()
        self.db_thread.start()
        self.graph_thread.start()

    def error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error!")
        msg.setWindowTitle("Serial Error")
        msg.exec_()

    def get_data(self, data):
        self.ui.terminal.append(data)
        next = self.ui.terminal.toPlainText().split("\n")
        self.graph_thread.up_graph(next[len(next) - 1], self.ui.unitBox.currentText())
        self.db_thread.update_db(data, self.ui.unitBox.currentText())

    def close_com(self):
        self.com_thread.exit()
        self.graph_thread.exit()
        self.db_thread.exit()

        self.ui.terminal.clear()
        self.com_thread.deleteLater()
        self.graph_thread.deleteLater()
        self.db_thread.deleteLater()

        self.ui.startButton.setEnabled(True)
        self.ui.stopButton.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
