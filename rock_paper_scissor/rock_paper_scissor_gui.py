import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock, Paper, and scissor")

        label = QLabel("Hello", self)

        #window size.
        self.setGeometry(400, 200, 500, 500)

        #icon.
        self.setWindowIcon(QIcon("icon.png"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()