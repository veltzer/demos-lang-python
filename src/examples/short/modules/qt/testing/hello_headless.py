"""
This is an example of how to run a PyQt application headless.

References:
- https://stackoverflow.com/questions/13215120/how-do-i-make-python-qt-and-webkit-work-on-a-headless-server
"""
# pylint: disable=c-extension-no-member

import sys
import PyQt5.QtWidgets

sys.argv.extend(["-platform", "minimal"])
app = PyQt5.QtWidgets.QApplication(sys.argv)
button = PyQt5.QtWidgets.QPushButton("Button")
button.clicked.connect(button.close)
button.show()
sys.exit(app.exec())
