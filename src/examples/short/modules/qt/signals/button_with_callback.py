"""
This is an example of an app with a button with a callback

References:
- https://stackoverflow.com/questions/15080731/calling-a-function-upon-button-press
"""
# pylint: disable=c-extension-no-member

import sys
import PyQt5.QtWidgets

app = PyQt5.QtWidgets.QApplication(sys.argv)
button = PyQt5.QtWidgets.QPushButton("Button")
button.clicked.connect(button.close)
button.show()
sys.exit(app.exec())
