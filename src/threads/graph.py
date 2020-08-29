from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QGridLayout
from Graph import MplCanvas
from time import gmtime, strftime


class MyGraphThread(QThread):
    data = pyqtSignal(str)

    def __init__(self, tabPlot):
        super().__init__()
        self.canvas = MplCanvas()
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.mpl = QGridLayout()
        self.tabPlot = tabPlot

        self.mpl.addWidget(self.canvas)

        self.ydata = [None] * 10
        self.xdata = list(range(10))

    def run(self):
        pass

    def up_graph(self, data, selection):
        self.tabPlot.setLayout(self.mpl)
        try:
            self.selection = selection
            self.ydata = self.ydata[1:]
            self.xdata = self.xdata[1:]
            self.ydata.append(float(data))
            self.xdata.append(strftime("%H:%M:%S", gmtime()))
        except:
            self.ydata.append(None)
            print("Error", data)

        if self.selection == "Pressure":
            self.canvas.axes.cla()
            self.canvas.axes.plot(self.xdata, self.ydata, "r")
            self.canvas.axes.set_title("Pressure")
            self.canvas.axes.set_ylabel("mBar", fontsize=16)
            self.canvas.axes.set_xlabel("Time", fontsize=16)
            self.canvas.draw()

        if self.selection == "Temperature":
            self.canvas.axes.cla()
            self.canvas.axes.plot(self.xdata, self.ydata, "g")
            self.canvas.axes.set_title("Temperature")
            self.canvas.axes.set_ylabel("°C", fontsize=16)
            self.canvas.axes.set_xlabel("Time", fontsize=16)
            self.canvas.draw()

        if self.selection == "Irradiance":
            self.canvas.axes.cla()
            self.canvas.axes.plot(self.xdata, self.ydata, "b")
            self.canvas.axes.set_title("Irradiance")
            self.canvas.axes.set_ylabel("uW/cm2", fontsize=16)
            self.canvas.axes.set_xlabel("Time", fontsize=16)
            self.canvas.draw()

    def exit(self):
        self.mpl.deleteLater()
        self.terminate()
