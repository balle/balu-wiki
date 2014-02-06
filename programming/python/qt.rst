####
PyQt
####

Simple hello world example with button and signal / slot
========================================================

.. code-block:: python

  #!/usr/bin/python2

  import sys
  from PyQt4 import QtCore, QtGui

  class MainWindow(QtGui.QMainWindow):
     def __init__(self, *argv):
        QtGui.QMainWindow.__init__(self, *argv)
        self.createMenu()
        self.createComponents()
        self.createLayout()
        self.createConnects()

     def createMenu(self):
        self.actionFileOpen = QtGui.QAction(self.tr("Open file..."), self)
        self.actionFileSave = QtGui.QAction(self.tr("Save"), self)
        self.actionExit = QtGui.QAction(self.tr("Exit"), self)
        self.actionExit.setMenuRole(QtGui.QAction.QuitRole)

        menuFile = self.menuBar().addMenu(self.tr("File"))
        menuFile.addAction(self.actionFileOpen)
        menuFile.addAction(self.actionFileSave)
        menuFile.addSeparator()
        menuFile.addAction(self.actionExit)

     def createComponents(self):
        self.labelHelloWorld = QtGui.QLabel(self.tr("Hello world!"))
        self.buttonUpdate = QtGui.QPushButton(self.tr("Update"))
        self.editText = QtGui.QLineEdit()
        self.setWindowTitle(self.tr("Hello world"))

     def createLayout(self):
        widgetCentral = QtGui.QWidget()

        layoutCentral = QtGui.QVBoxLayout()
        layoutCentral.addWidget(self.labelHelloWorld)
        layoutCentral.addWidget(self.editText)
        layoutCentral.addWidget(self.buttonUpdate)

        widgetCentral.setLayout(layoutCentral)
        self.setCentralWidget(widgetCentral)

     def createConnects(self):
        self.buttonUpdate.clicked.connect(self.updateText)


     @QtCore.pyqtSlot()
     def updateText(self):
        self.labelHelloWorld.setText(self.editText.text())


  def main(argv):
    app = QtGui.QApplication(argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

  if __name__ == "__main__":
    main(sys.argv)


Django-like Framework
=====================

* http://www.python-camelot.com
