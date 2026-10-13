import sys
import dbconect

# импорт ui
from UI.MainWindow import Ui_MainWindow as MainWindow
from UI.AddPlayer import Ui_Dialog as AddPlayer
from UI.AddPlayer_2 import Ui_Dialog as AddPlayer_2
from UI.AddPlayer_3 import Ui_Dialog as AddPlayer_3

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox

# для отображения картинок
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from pathlib import Path

players = []

# добавление 1 игрока
def add_player():
    playername = login_ui.lineEdit_playername.text()

    if not playername:
        QMessageBox.warning(window, "ошибка", "Введите имя игрока")
        return

    players.append(playername)

    window.close()
    open_player_2()

# открытие диалога для добавления 2 игрока
def open_player_2():
    global window_2, login_ui_2

    window_2 = QDialog()
    login_ui_2 = AddPlayer_2()
    login_ui_2.setupUi(window_2)

    login_ui_2.pushButton_addplayer.clicked.connect(add_player_2)

    window_2.show()

# добавление 2 игрока
def add_player_2():
    playername = login_ui_2.lineEdit_playername.text()

    if not playername:
        QMessageBox.warning(window, "ошибка", "Введите имя игрока")
        return

    players.append(playername)

    window_2.close()
    open_player_3()

# открытие диалога для добавления 3 игрока
def open_player_3():
    global window_3, login_ui_3

    window_3 = QDialog()
    login_ui_3 = AddPlayer_3()
    login_ui_3.setupUi(window_3)

    login_ui_3.pushButton_addplayer.clicked.connect(add_player_3)

    window_3.show()

# добавление 3 игрока
def add_player_3():
    playername = login_ui_3.lineEdit_playername.text()

    if not playername:
        QMessageBox.warning(window, "ошибка", "Введите имя игрока")
        return

    players.append(playername)

    window_3.close()
    open_main_wiwndow()

# открытие главного окна игры
def open_main_wiwndow():
    global main_window, main_window_ui
    main_window = QMainWindow()
    main_window_ui = MainWindow()
    main_window_ui.setupUi(main_window)

    main_window_ui.label_playername.setText("".join(players[0]))
    main_window_ui.label_playername2.setText("".join(players[1]))
    main_window_ui.label_playername3.setText("".join(players[2]))

    window.close()

    main_window.show()
    show_img()

BASE_DIR = Path(__file__).resolve().parent

def show_img():
    card = dbconect.get_random_img()

    if card is None:
        print("Ошибка отображения карточки")
        return

    card_id, correct_answer, card_url = card

    img_path = BASE_DIR / card_url

    pixmap = QPixmap(str(img_path))

    if pixmap.isNull():
        print(f"Не удалось загрузить изображение: {img_path}")
        return

    main_window_ui.label_image.setPixmap(
        pixmap.scaled(
            main_window_ui.label_image.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
    )

# запуск диалога
if __name__ == "__main__":
    app = QApplication(sys.argv)

    global window

    window = QDialog()
    login_ui = AddPlayer()
    login_ui.setupUi(window)

    login_ui.pushButton_addplayer.clicked.connect(add_player)

    window.show()
    sys.exit(app.exec())

