from PySide6.QtWidgets import QWidget
from .user_grant_page_ui import Ui_UserGrantPage

class UserGrantPage(QWidget):

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.ui = Ui_UserGrantPage()
        self.ui.setupUi(self)

        
