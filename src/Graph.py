from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):
    axes = None

    def __init__(self, width=5, height=4, dpi=100, args=111):
        self.figure = Figure(figsize=(width, height), dpi=dpi, tight_layout=3.0)

        super().__init__(self.figure)
