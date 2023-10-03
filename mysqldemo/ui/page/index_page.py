from PySide6.QtWidgets import QWidget
from .index_page_ui import Ui_IndexPage

class IndexPage(QWidget):
    
    def __init__(self, parent: QWidget=None) -> None:
        super().__init__(parent)
        self.ui = Ui_IndexPage()
        self.ui.setupUi(self)
        