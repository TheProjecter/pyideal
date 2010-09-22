from PyQt4.QtGui import QAction
from PyQt4.QtGui import QIcon
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QObject

import resources

class MenuEdit(object):

    def __init__(self, menu, tool, main):
        self._main = main

        undoAction = menu.addAction(QIcon(resources.images['undo']), 'Undo')
        redoAction = menu.addAction(QIcon(resources.images['redo']), 'Redo')
        cutAction = menu.addAction(QIcon(resources.images['cut']), '&Cut (Ctrl+X)')
        copyAction = menu.addAction(QIcon(resources.images['copy']), '&Copy (Ctrl+C)')
        pasteAction = menu.addAction(QIcon(resources.images['paste']), '&Paste (Ctrl+V)')
        prefAction = menu.addAction(QIcon(resources.images['pref']), 'Preference&s')

        tool.addAction(cutAction)
        tool.addAction(copyAction)
        tool.addAction(pasteAction)

        QObject.connect(cutAction, SIGNAL("triggered()"), lambda: self._main.obtain_editor().cut())
        QObject.connect(copyAction, SIGNAL("triggered()"), lambda: self._main.obtain_editor().copy())
        QObject.connect(pasteAction, SIGNAL("triggered()"), lambda: self._main.obtain_editor().paste())
        QObject.connect(redoAction, SIGNAL("triggered()"), lambda: self._main.obtain_editor().redo())
        QObject.connect(undoAction, SIGNAL("triggered()"), lambda: self._main.obtain_editor().undo())
