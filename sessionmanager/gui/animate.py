# Program: SessionManager
# File: gui/animate.py
# Desc: Animations for GUI components
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets


class Animate(QtCore.QObject):
    def __init__(self, parent):
        super(Animate, self).__init__(parent)

    # Properties
    def get_color(self):
        return self.palette().text().color()

    def set_color(self, color):
        palette = self.palette()
        palette.setColor(self.foregroundRole(), color)
        self.setPalette(palette)

    def get_mirror(self):
        return self.palette()

    def set_mirror(self, color):
        palette = self.palette()
        palette.setColor(self.backgroundRole(), color)
        self.setPalette(palette)

    color = QtCore.pyqtProperty(QtGui.QColor, get_color, set_color)
    mirror = QtCore.pyqtProperty(QtGui.QColor, get_mirror, set_mirror)

    # Animations
    def color_fade(self, obj, start, end):
        colorize = QtWidgets.QGraphicsColorizeEffect(self)
        obj.setGraphicsEffect(colorize)
        self.animate = QtCore.QPropertyAnimation(colorize, b"color")
        self.animate.setStartValue(QtGui.QColor(start))
        self.animate.setEndValue(QtGui.QColor(end))
        self.animate.setDuration(250)
        self.animate.start()

    def color_mirror(self, obj, start, end):
        colorize = QtWidgets.QGraphicsColorizeEffect(self)
        obj.setGraphicsEffect(colorize)
        self.animate = QtCore.QPropertyAnimation(colorize, b"color")
        self.animate.setStartValue(QtGui.QColor(start))
        self.animate.setEndValue(QtGui.QColor(end))
        self.animate.setDuration(400)
        self.animate.start()