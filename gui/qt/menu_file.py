import sys

from PyQt4.QtGui import QAction
from PyQt4.QtGui import QKeySequence
from PyQt4.QtGui import QShortcut
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QStyle
from PyQt4.QtGui import QIcon
from PyQt4.QtCore import QObject
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QCoreApplication

import resources

class MenuFile(object):

    def __init__(self, menu, tool, main):
        self._main = main

        newAction = menu.addAction(QIcon(resources.images['new']), '&New (Ctrl+N)')
        saveAction = menu.addAction(QIcon(resources.images['save']), '&Save (Ctrl+S)')
        saveAsAction = menu.addAction(QIcon(resources.images['saveAs']), 'Save &As')
        openAction = menu.addAction(QIcon(resources.images['open']), '&Open (Ctrl+O)')
        openProjectAction = menu.addAction(QIcon(resources.images['openProj']), '&Open Project')
        closeAction = menu.addAction(self._main.style().standardIcon(QStyle.SP_DialogCloseButton), '&Close')
        menu.addSeparator()
        exitAction = menu.addAction(self._main.style().standardIcon(QStyle.SP_DialogCloseButton), '&Exit')

        tool.addAction(newAction)
        tool.addAction(openAction)
        tool.addAction(saveAction)

        QObject.connect(newAction, SIGNAL("triggered()"), main.new_editor)
        QObject.connect(openAction, SIGNAL("triggered()"), main.open_file)
        QObject.connect(saveAction, SIGNAL("triggered()"), main.save)
        QObject.connect(saveAsAction, SIGNAL("triggered()"), main.save_as)
        QObject.connect(openProjectAction, SIGNAL("triggered()"), main.open_project)
        QObject.connect(closeAction, SIGNAL("triggered()"), main.close_actual_tab)
        QObject.connect(exitAction, SIGNAL("triggered()"), QCoreApplication.quit)
