from PySide6.QtWidgets import QWidget, QMainWindow
from .main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        