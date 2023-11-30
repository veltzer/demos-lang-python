"""
A simple hello world application in pyqt
"""
# pylint: disable=c-extension-no-member

import sys
import PyQt5.QtWidgets

app = PyQt5.QtWidgets.QApplication(sys.argv)
button = PyQt5.QtWidgets.QPushButton("Button")

# We connect the clicked() signal to the buttons "close" slot (method).
# Whenever you click on the button, it emits the signal. Then every slot that is
# connected to that signal gets called. In this case, only w.close
button.clicked.connect(button.close)

# Show the window. Without this we would still have an application but the window
# would not be shown.
button.show()
# Make sure that when the last window is closed, the application would quit.
# This is the default behaviour is True so strictly speaking it is not needed.
app.setQuitOnLastWindowClosed(True)

# Go into the application main loop
# app.exec returns an integer which is the return code of the application.
sys.exit(app.exec())
