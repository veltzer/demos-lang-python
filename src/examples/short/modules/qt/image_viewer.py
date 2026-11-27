"""
This is an image viewer application
"""


import signal
import sys
import typing

from PyQt5.QtGui import QPainter, QPaintEvent, QPixmap
from PyQt5.QtWidgets import QApplication, QTableWidget, QWidget

signal.signal(signal.SIGINT, signal.SIG_DFL)


class ImageWidget(QWidget):

    def __init__(self, image_path: str, parent: QWidget) -> None:
        super().__init__(parent)
        self.picture = QPixmap(image_path)

    @typing.override
    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.picture)


class TableWidget(QTableWidget):

    def set_image(self, row: int, col: int, image_path: str) -> None:
        image = ImageWidget(image_path, self)
        self.setCellWidget(row, col, image)


def main():
    app = QApplication([])
    table_widget = TableWidget(10, 2)
    table_widget.set_image(0, 1, "data/jpg/image0000.jpg")
    table_widget.show()
    sys.exit(app.exec())


main()
