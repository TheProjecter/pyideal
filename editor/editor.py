from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QPlainTextEdit

from highlighter import PythonHighlighter

class Editor(QPlainTextEdit):

    def __init__(self):
        QPlainTextEdit.__init__(self)
        self.highlighter = PythonHighlighter(self.document())
        self.newDocument = True
        self.path = ''
