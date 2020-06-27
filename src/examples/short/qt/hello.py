#!/usr/bin/env python

import sys

import PyQt5.QtCore
import PyQt5.QtWidgets

print('version is', PyQt5.QtCore.QT_VERSION_STR)
a = PyQt5.QtWidgets.QApplication(sys.argv)
w = PyQt5.QtWidgets.QPushButton('Hello World', None)

# Here the differences to the trivial one above may be seen, using QT's
# signal and slot features:

# We connect the clicked() signal to the button's 'close' slot (method).
# Whenever you click on the button, it emits the signal. Then every slot that is
# connected to that signal gets called. In this case, only w.close
w.clicked.connect(w.close)

# We make w the main widget of the application. That means that when w is closed
# The application exits. If we didn't do this, we would have to call a.quit()
# to make it end.
# a.setMainWidget(w)
w.show()
sys.exit(a.exec_())
