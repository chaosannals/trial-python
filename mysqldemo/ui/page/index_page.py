from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import QWidget
from loguru import logger
from .index_page_ui import Ui_IndexPage
from ..route import router

class IndexPage(QWidget):
    
    def __init__(self, parent: QWidget=None) -> None:
        super().__init__(parent)
        self.ui = Ui_IndexPage()
        self.ui.setupUi(self)
        logger.info('init index page')
        self.connect(self.ui.userGrantButton, SIGNAL('clicked()'), self.routeTo('userGrantPage'))

    def routeTo(self, name):
        def action():
            logger.info('route to {}', name)
            router.on_next(name)
        return action
        