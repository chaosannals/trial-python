from PySide6.QtCore import Qt, SIGNAL
from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from loguru import logger
from .user_grant_page_ui import Ui_UserGrantPage

class RowBuilder:
    def __init__(self, table: QTableWidget) -> None:
        self.columnIndex = 0
        self.table = table

    
    def addColumn(self, index, item):
        self.table.setItem(index, self.columnIndex, item)
        self.columnIndex += 1

    def addItem(self, index, row: dict, **config):
        item = QTableWidgetItem()
        if config.get('isCheckBox', False):
            item.setCheckState(Qt.Unchecked)
            item.setData(Qt.UserRole, row)
        else:
            item.setText(row.get(config.get('field', None), None))
        item.setTextAlignment(Qt.AlignCenter)
        self.addColumn(index, item)



class UserGrantPage(QWidget):

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.ui = Ui_UserGrantPage()
        self.ui.setupUi(self)
        self.users = []
        self.dbs = []
        self.ips = []

        self.connect(self.ui.userAddButton, SIGNAL('clicked()'), self.addUserRow)

    
    def addUserRow(self):
        '''
        '''

        user = self.ui.userInputEdit.text()
        row = {
            'name': user,
        }
        index = len(self.users)

        logger.info('add user {} {}', index, row)
        builder = RowBuilder(self.ui.userTable)
        builder.addItem(index, row, isCheckBox=True)
        builder.addItem(index, row, filed='name')
        self.users.append(row)
        self.ui.userTable.setRowCount(len(self.users))


    def insertDbRow(self):
        '''
        '''

        builder = RowBuilder(self.ui.dbTable)

    def insertIpRow(self):
        '''
        '''

        builder = RowBuilder(self.ui.ipTable)