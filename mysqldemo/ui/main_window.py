from PySide6.QtWidgets import QWidget, QMainWindow
from .main_window_ui import Ui_MainWindow
from .route import router

class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget=None) -> None:
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        def on_route_next(name):
            page = getattr(self.ui, name)
            self.ui.routeWidget.setCurrentWidget(page)
        router.subscribe(
            on_next=on_route_next
        )
        