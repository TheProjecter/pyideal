import sys, time

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from main_window import MainWindow
from menu_file import MenuFile
from menu_edit import MenuEdit

import resources

class IDE(QMainWindow):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('pyIDEal')
        self.setWindowState(Qt.WindowMaximized)

        #Main Widgets
        self.main = MainWindow(self)
        self.setCentralWidget(self.main)

        #Menu
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        edit = menubar.addMenu('&Edit')

        self._toolbar = self.addToolBar("toolbar")
        self._toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self._menuFile = MenuFile(file, self._toolbar, self.main)
        self._menuEdit = MenuEdit(edit, self._toolbar, self.main)

        self.main.obtain_editor().setFocus()

def start():
    app = QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QPixmap(resources.images['splash'])
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    time.sleep(2)
    ide = IDE()
    ide.show()
    splash.finish(ide)
    sys.exit(app.exec_())
