# Program: Session Manager
# File: gui/widgets/event_filter.py
# Desc: Event Filter Manager
# Author: Braden Mars

from PyQt5 import QtCore, QtGui, QtWidgets
from gui import animate


class EventFilter(QtCore.QObject):
    logo_added = QtCore.pyqtSignal(object)

    def __init__(self, parent):
        super(EventFilter, self).__init__(parent)
        self.animate = animate.Animate(self)
        self.parent = parent

        # Functions
    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.ChildRemoved:
            print('DRAG EVENT RECEIVED')
            self.logo_added.emit(object)

        action = str(object.property("action"))
        if action == "color_fade":
            if event.type() == QtCore.QEvent.HoverEnter:
                self.animate.color_fade(object, "#736F6E", "#f2f2f2")
                return True
            if event.type() == QtCore.QEvent.HoverLeave:
                self.animate.color_fade(object, "#f2f2f2", "#736F6E")
                return True

        elif action == "color_mirror":
            if event.type() == QtCore.QEvent.HoverEnter:
                #self.animate.color_mirror(object, "rgba(0,0,0,0)", "#D3D3D3")
                return True
            if event.type() == QtCore.QEvent.HoverLeave:
                #self.animate.color_mirror(object, "#D3D3D3", "rgba(0,0,0,0)")
                return True

        elif action == "item_text":
            if event.type() == QtCore.QEvent.HoverEnter:
                object.setStyleSheet("color:red;")
                return True

        elif action == "context":
            if event.type() == QtCore.QEvent.ContextMenu:
                menu = QtWidgets.QMenu(self.parent)
                menu.addAction(self.parent.delete_icon, "Delete")

                if menu.exec_(event.globalPos()):
                    self.parent.delete_session()
                return True

        elif action == "proof_context":
            if event.type() == QtCore.QEvent.ContextMenu:
                menu = QtWidgets.QMenu(self.parent)
                if bool(object.property("loose")):
                    open = menu.addAction(self.parent.preview_icon, "Open Preview")
                else:
                    open = menu.addAction(self.parent.preview_icon, "Open Preview")
                    delete = menu.addAction(self.parent.delete_icon, "Delete")
                    logo = menu.addAction(self.parent.logo_icon, "Add Logo")
                action = menu.exec_(event.globalPos())
                if action is not None :
                    if action == open:
                        self.parent.view()
                    elif action == delete:
                        self.parent.delete_proof()
                    elif action == logo:
                        self.parent.edit_proof()
                return True

            elif action == "mime":
                if event.type() == QtCore.QEvent.MouseMove:
                    mimeData = QtCore.QMimeData()
                    mimeData.setText('%d,%d' % (event.x(), event.y()))
                    pix = QtWidgets.QWidget.grab(object)
                    drag = QtGui.QDrag(object)
                    drag.setMimeData(mimeData)
                    drag.setPixmap(pix)
                    drag.setHotSpot(event.pos())
                    if drag.exec_(QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction:
                        print("moved")
                return True

        return False
