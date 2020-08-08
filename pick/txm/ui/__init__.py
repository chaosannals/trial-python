from PyQt5 import QtCore as core
from PyQt5 import uic


def load_ui(widget, url):
    f = core.QFile(url)
    f.open(core.QIODevice.ReadOnly)
    ui = uic.loadUi(f, widget)
    f.close()
    return ui


def load_rc(url):
    f = core.QFile(url)
    f.open(core.QIODevice.ReadOnly)
    r = f.readAll()
    f.close()
    return str(r, encoding='utf-8')
