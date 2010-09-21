import sys, time

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import resources

from ui import MainWindow
from ui import FileMenu
from ui import EditMenu

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

        self._fileMenu = FileMenu(file, self._toolbar, self.main)
        self._editMenu = EditMenu(edit, self._toolbar, self.main)

        self.main.obtain_editor().setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and display the splash screen
    splash_pix = QPixmap(resources.images['splash'])
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # Simulate something that takes time
    time.sleep(2)

    ide = IDE()
    ide.show()
    splash.finish(ide)
    sys.exit(app.exec_())
