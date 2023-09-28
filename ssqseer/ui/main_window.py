from typing import Optional
from PySide6.QtCore import Qt, SIGNAL, QStringListModel
from PySide6.QtWidgets import QMainWindow, QCompleter
from .main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.completeSet = set()
        self.completeModel = QStringListModel(list(self.completeSet),self)
        self.completer = QCompleter(self)
        self.completer.setCompletionMode(QCompleter.CompletionMode.UnfilteredPopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setModel(self.completeModel)
        self.ui.searchEdit.setCompleter(self.completer)
        self.connect(self.ui.searchEdit, SIGNAL('editingFinished()'), self.onEditComplete)
    
    def onEditComplete(self):
        text = self.ui.searchEdit.text()
        if len(text) != 0:
            if text not in self.completeSet:
                self.completeSet.add(text)
                self.completeModel.setStringList(list(self.completeSet))
        else:
            self.completer.popup().show()
