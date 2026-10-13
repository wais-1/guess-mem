import sys
import dbconect

from UI.MainWindow import Ui_MainWindow as MainWindow
from UI.AddPlayer import Ui_Dialog as AddPlayer

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem

if __name__ == "__main__":
    app = QApplication(sys.argv)

    global window

    window = QMainWindow()
    ui = MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec())

