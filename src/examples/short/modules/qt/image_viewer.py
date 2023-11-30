"""
This is an image viewer application
"""


import sys
import signal
# pylint: disable=no-name-in-module
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget


signal.signal(signal.SIGINT, signal.SIG_DFL)


class ImageWidget(QWidget):

    def __init__(self, image_path, parent):
        super().__init__(parent)
        self.picture = QPixmap(image_path)

    def paintEvent(self, _event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.picture)


class TableWidget(QTableWidget):

    def setImage(self, row, col, image_path):
        image = ImageWidget(image_path, self)
        self.setCellWidget(row, col, image)


def main():
    app = QApplication([])
    table_widget = TableWidget(10, 2)
    table_widget.setImage(0, 1, "data/jpg/image0000.jpg")
    table_widget.show()
    sys.exit(app.exec())


main()
