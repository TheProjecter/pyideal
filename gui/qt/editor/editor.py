from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QPlainTextEdit
from PyQt4.QtGui import QFont
from PyQt4.QtGui import QTextCharFormat
from PyQt4.QtCore import QSize

from highlighter import PythonHighlighter

class Editor(QPlainTextEdit):

    def __init__(self):
        QPlainTextEdit.__init__(self)
        self.lineNumber = LineNumbersArea(self)
        self.highlighter = PythonHighlighter(self.document())
        self.newDocument = True
        self.path = ''
        css = '''
        QPlainTextEdit {
          font-family: monospace;
          font-size: 10;
          color: black;
          background-color: white;
          selection-color: white;
          selection-background-color: #437DCD;
        }'''
        self.setStyleSheet(css)


class LineNumbersArea(QWidget):

    def __init__(self, editor):
        QWidget.__init__(editor)
        self.codeEditor = editor

    def sizeHint(self):
        return QSize(self.codeEditor.line_number_area(), 0)
