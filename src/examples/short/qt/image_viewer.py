import sys

from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)


class ImageWidget(QWidget):

    def __init__(self, image_path, parent):
        super(ImageWidget, self).__init__(parent)
        self.picture = QPixmap(image_path)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.picture)


class TableWidget(QTableWidget):

    def setImage(self, row, col, image_path):
        image = ImageWidget(image_path, self)
        self.setCellWidget(row, col, image)


def main():
    app = QApplication([])
    table_widget = TableWidget(10, 2)
    table_widget.setImage(0, 1, "data_samples/images/image0000.jpg")
    table_widget.show()
    sys.exit(app.exec_())


main()
