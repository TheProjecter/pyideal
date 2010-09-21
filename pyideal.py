import sys

import gui
import resources

dictGui = {'qt':gui.setupQt, 'gtk':gui.setupGtk}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        function = dictGui.get(sys.argv[1], dictGui['qt'])
        function()
    else:
        gui.setupQt()
