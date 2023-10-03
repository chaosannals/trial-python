import sys
from loguru import logger
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

@logger.catch
def main():
    logger.add(
        'log/app.log',
        level='TRACE',
        # rotation='00:00',
        rotation='2000 KB',
        retention='7 days',
        encoding='utf8'
    )

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()

if '__main__' == __name__:
    main()