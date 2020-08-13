"""
A simple hello world application in pyqt
"""

import sys

import PyQt5.QtWidgets

app = PyQt5.QtWidgets.QApplication(sys.argv)
window = PyQt5.QtWidgets.QPushButton('Hello World', None)

"""
We connect the clicked() signal to the button's 'close' slot (method).
Whenever you click on the button, it emits the signal. Then every slot that is
connected to that signal gets called. In this case, only w.close
"""
# window.clicked.connect(window.close)

"""
Show the window. Without this we would still have an application but the window
would not be shown.
"""
window.show()
"""
Make sure that when the last window is closed, the application would quit.
This is the default behaviour so strictly speaking it is not needed.
"""
# app.setQuitOnLastWindowClosed(True)

"""
Go into the appication main loop
"""
sys.exit(app.exec_())
