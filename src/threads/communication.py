from PyQt5.QtCore import QThread, pyqtSignal
from serial import Serial


class ComThread(QThread):
    change_value = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, current_data):
        super().__init__()
        self.com_port = current_data["com_port"]
        self.baud = current_data["baud_rate"]
        self.data_bits = current_data["data_bits"]
        self.parity = current_data["parity"]
        self.stop_bit = current_data["stop_bit"]

    def run(self):
        try:
            self.s = Serial(
                self.com_port, self.baud, self.data_bits, self.parity, self.stop_bit
            )
        except:
            self.error.emit("Error Occured!")
            return None

        while True:
            data = self.s.readline().decode().rstrip()
            self.change_value.emit(data)

    def exit(self):
        self.terminate()
        if self.s.is_open:
            self.s.close()
