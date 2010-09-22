from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QPlainTextEdit
from PyQt4.QtGui import QFont
from PyQt4.QtGui import QTextCharFormat

from highlighter import PythonHighlighter

class Editor(QPlainTextEdit):

    def __init__(self):
        QPlainTextEdit.__init__(self)
        font = QFont("monospace", 10)
        charFormat = QTextCharFormat()
        charFormat.setFont(font)
        self.setCurrentCharFormat(charFormat)
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
