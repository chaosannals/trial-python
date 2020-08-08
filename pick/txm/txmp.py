import txmp_rc
import sys
from PyQt5 import QtWidgets as qtw
from ui.mainwindow import MainWindow

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
