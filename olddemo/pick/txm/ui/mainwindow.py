from PyQt5 import QtWidgets as qtw
from .pick import Picker
from . import load_ui, load_rc


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.move(500, 300)
        self.setWindowTitle('腾讯地图行政区划')
        self.ui = load_ui(self, ':/ui/mainwindow.ui')
        self.ui.setStyleSheet(load_rc(':/ui/mainwindow.qss'))
        self.ui.pickButton.clicked.connect(self.pick)

    def pick(self):
        key = self.ui.keyLineEdit.text()
        secret = self.ui.secretLineEdit.text()
        picker = Picker(key, secret)
        picker.pick_district_as_tree_save_json('area.json')
