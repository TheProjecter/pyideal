#partially based on: http://john.nachtimwald.com/2009/08/15/qtextedit-with-line-numbers/ (MIT license)

from PyQt4.QtGui import QWidget
from PyQt4.QtGui import QPlainTextEdit
from PyQt4.QtGui import QTextEdit
from PyQt4.QtGui import QFontMetrics
from PyQt4.QtGui import QTextFormat
from PyQt4.QtGui import QColor
from PyQt4.QtGui import QBrush
from PyQt4.QtGui import QPainter
from PyQt4.QtCore import Qt

from highlighter import PythonHighlighter

class Editor(QPlainTextEdit):

    def __init__(self):
        QPlainTextEdit.__init__(self)
        self.lineNumberArea = self.LineNumberArea(self)
        self.viewport().installEventFilter(self)
        
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

        self.highlight_current_line()
        
    def highlight_current_line(self):
        extraSelections = []

        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            lineColor = QColor(Qt.darkCyan)
            lineColor.setAlpha(20)

            selection.format.setBackground(lineColor)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)

    def resizeEvent(self,e):
        self.lineNumberArea.setFixedHeight(self.height())
        QPlainTextEdit.resizeEvent(self,e)

    def eventFilter(self, object, event):
        if object is self.viewport():
            self.lineNumberArea.update()
            return False
        return QPlainTextEdit.eventFilter(object, event)


    class LineNumberArea(QWidget):

        def __init__(self, editor):
            QWidget.__init__(self, editor)
            self.edit = editor
            self.highest_line = 0
            css = '''
            QWidget {
              font-family: monospace;
              font-size: 10;
              color: black;
            }'''
            self.setStyleSheet(css)
 
        def update(self, *args):
            width = QFontMetrics(self.edit.document().defaultFont()).width(str(self.highest_line)) + 10
            if self.width() != width:
                self.setFixedWidth(width)
                self.edit.setViewportMargins(width,0,0,0)
            QWidget.update(self, *args)
 
        def paintEvent(self, event):
            contents_y = 0
            page_bottom = self.edit.viewport().height()
            font_metrics = QFontMetrics(self.edit.document().defaultFont())
            current_block = self.edit.document().findBlock(self.edit.textCursor().position())
 
            painter = QPainter(self)
            painter.fillRect(self.rect(), Qt.lightGray)
            
            block = self.edit.firstVisibleBlock()
            viewport_offset = self.edit.contentOffset()
            line_count = block.blockNumber()
            painter.setFont(self.edit.document().defaultFont())
            while block.isValid():
                line_count += 1
                # The top left position of the block in the document
                position = self.edit.blockBoundingGeometry(block).topLeft() + viewport_offset
                # Check if the position of the block is out side of the visible area
                if position.y() > page_bottom:
                    break
 
                # We want the line number for the selected line to be bold.
                bold = False
                if block == current_block:
                    bold = True
                    font = painter.font()
                    font.setBold(True)
                    painter.setFont(font)
 
                # Draw the line number right justified at the y position of the
                # line. 3 is a magic padding number. drawText(x, y, text).
                painter.drawText(self.width() - font_metrics.width(str(line_count)) - 3,
                    round(position.y()) + font_metrics.ascent()+font_metrics.descent()-1,
                    str(line_count))
 
                # Remove the bold style if it was set previously.
                if bold:
                    font = painter.font()
                    font.setBold(False)
                    painter.setFont(font)
 
                block = block.next()
 
            self.highest_line = line_count
            painter.end()
 
            QWidget.paintEvent(self, event)
