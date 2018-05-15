# Program: Session Manager
# File: gui/widgets/photo_viewer.py
# Desc: View and Edit Images
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets


class EditScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent):
        super(EditScene, self).__init__(parent)
        self.parent = parent
        self.item = False

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        print('got a drop')
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()
        #x = event.pos()
        pos = QtGui.QCursor.pos()
        print(pos)
        # pix = QtWidgets.QWidget.grab(active)
        # drag = QtGui.QDrag(self)
        # drag.setMimeData(self.mime)
        # drag.setPixmap(pix)
        # drag.setHotSpot(pos)

        print('drag enter')

    def dragLeaveEvent(self, event):
        event.accept()
        print("drag leave")


class QPhotoView(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(QPhotoView, self).__init__(parent)
        # Vars
        self._zoom = 0
        #self._scene = QtWidgets.QGraphicsScene(self)
        self._scene = EditScene(self)
        print(self._scene)
        self._photo = QtWidgets.QGraphicsPixmapItem()
        self._logo = QtWidgets.QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.setScene(self._scene)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)

    def fitInView(self, scale=True):
        rect = QtCore.QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
            self.scale(1 / unity.width(), 1 / unity.height())
            viewrect = self.viewport().rect()
            scenerect = self.transform().mapRect(rect)
            factor = min(viewrect.width() / scenerect.width(),
                         viewrect.height() / scenerect.height())
            self.scale(factor, factor)
            self._zoom = 0

    def set_photo(self, pixmap=None):
        self._zoom = 0
        if pixmap and not pixmap.isNull():
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self._photo.setPixmap(pixmap)
        else:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self._photo.setPixmap(QtGui.QPixmap())
        #self.fitInView()

    def insert_logo(self, pixmap=None):
        self._logo.setPixmap(pixmap)
        self._logo.setFlags(QtWidgets.QGraphicsPixmapItem.ItemIsSelectable | QtWidgets.QGraphicsPixmapItem.ItemIsMovable)
        self._scene.addItem(self._logo)
        self._logo.setPos(QtGui.QCursor.pos())

        print('logo added')

    def toggle_drag(self):
        if self.dragMode() == QtWidgets.QGraphicsView.ScrollHandDrag:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        elif not self._photo.pixmap().isNull():
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            factor = 1.25
            self._zoom += 1
        else:
            factor = 0.8
            self._zoom -= 1
        if self._zoom > 0:
            self.scale(factor, factor)
        elif self._zoom == 0:
            self.fitInView()
        else:
            self._zoom = 0

    def mousePressEvent(self, event):
        if self._photo.isUnderMouse() and self._photo.isObscured() is False:
            print('image clicked')
            return False
        return False
            #self.photoClicked.emit(QtCore.QPoint(event.pos()))
        #super(PhotoViewer, self).mousePressEvent(event)