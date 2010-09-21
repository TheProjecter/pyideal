import sys

from PyQt4 import QtGui, QtCore
import os
from editor import Editor
import resources

class MainWindow(QtGui.QWidget):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self._parent = parent

        self._vbox = QtGui.QVBoxLayout(self)
        #Central Widgets
        self.splitter = QtGui.QSplitter()
        #Project Explorer
        self._tree = QtGui.QTreeWidget()
        #Editor
        self._tabs = QtGui.QTabWidget()
        self._tabs.setTabsClosable(True)
        editor = Editor()
        self._tabs.addTab(editor, 'New Document')
        
        self.splitter.addWidget(self._tree)
        self.splitter.addWidget(self._tabs)
        self._vbox.addWidget(self.splitter)
        
        shortCloseTab = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_W), self)
        shortNew = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_N), self)
        shortOpen = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_O), self)
        shortSave = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_S), self)
        shortChangeTab = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Tab), self)
        
        self.connect(shortCloseTab, QtCore.SIGNAL("activated()"), self.close_actual_tab)
        self.connect(shortNew, QtCore.SIGNAL("activated()"), self.new_editor)
        self.connect(shortOpen, QtCore.SIGNAL("activated()"), self.open_file)
        self.connect(shortSave, QtCore.SIGNAL("activated()"), self.save)
        self.connect(shortChangeTab, QtCore.SIGNAL("activated()"), self._change_tab)

    def obtain_editor(self):
        return self._tabs.widget(0)

    def new_editor(self):
        editor = Editor()
        self._tabs.addTab(editor, 'New Document')
        self._tabs.setCurrentIndex(self._tabs.count()-1)
        editor.setFocus()

    def open_file(self):
        fileName = str(QtGui.QFileDialog.getOpenFileName(self, 'Open File', filter='*'))
        if fileName == '':
            return
        editor = Editor()
        try:
            f = open(fileName)
            content = f.readlines()
            content = ''.join(content)
            editor.setPlainText(content)
            self._tabs.addTab(editor, fileName)
            self._tabs.setTabText(self._tabs.count()-1, os.path.basename(f.name))
            self._tabs.setCurrentIndex(self._tabs.count()-1)
            editor.setFocus()
        except:
            QtGui.QMessageBox.information(self, 'Incorrect File', 'The file does not exist!')

    def open_project(self):
        folderName = str(QtGui.QFileDialog.getExistingDirectory(self, 'Open Project Directory'))
        if folderName == '':
            return
        editor = Editor()
        try:
            f = open(fileName)
            content = f.readlines()
            content = ''.join(content)
            editor.setPlainText(content)
            self._tabs.addTab(editor, 'New Document')
            self._tabs.setCurrentIndex(self._tabs.count()-1)
            editor.setFocus()
        except:
            QtGui.QMessageBox.information(self, 'Incorrect File', 'The file does not exist!')

    def close_actual_tab(self):
        self._tabs.removeTab(self._tabs.currentIndex())

    def save(self):
        editor = self.obtain_editor()
        try:
            if editor.newDocument:
                fileName = str(QtGui.QFileDialog.getSaveFileName(self, 'Save File', filter='*.py'))
                if fileName == '':
                    raise Exception()
                if not fileName.endswith('.py'):
                    fileName += '.py'
                self._tabs.setTabText(self._tabs.currentIndex(), os.path.basename(fileName))
                editor.newDocument = False
                editor.path = fileName
            else:
                fileName = editor.path
            f = open(fileName, 'w')
            f.write(editor.toPlainText())
            f.close()
        except:
            editor.newDocument = True
            editor.path = ''
            self._tabs.setTabText(self._tabs.currentIndex(), 'New Document')

    def save_as(self):
        editor = self.obtain_editor()
        try:
            fileName = str(QtGui.QFileDialog.getSaveFileName(self, 'Save File', filter='*.py'))
            if fileName == '':
                raise Exception()
            if not fileName.endswith('.py'):
                fileName += '.py'
            self._tabs.setTabText(self._tabs.currentIndex(), os.path.basename(fileName))
            editor.newDocument = False
            editor.path = fileName
            f = open(fileName, 'w')
            f.write(editor.toPlainText())
            f.close()
        except:
            editor.newDocument = True
            editor.path = ''
            self._tabs.setTabText(self._tabs.currentIndex(), 'New Document')

    def _change_tab(self):
        if self._tabs.currentIndex() < (self._tabs.count()-1):
            self._tabs.setCurrentIndex(self._tabs.currentIndex() + 1)
        else:
            self._tabs.setCurrentIndex(0)
