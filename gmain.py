import sys
import os
import main
from PyQt5 import QtCore, QtGui, QtWidgets
from gui_main import Ui_MainFrame
from gui_deleteWarn import Ui_DeletePopup
from gui_create import Ui_createWindow
# SM Files
import sessions
import plist


# Create Session thread:
class CreateSession(QtCore.QThread):
    working = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()
    def __init__(self, PATH, NAME, DESC, RAW):
        QtCore.QThread.__init__(self)
        self.path = PATH
        self.name = NAME
        self.desc = DESC
        self.raw = RAW

    def __del__(self):
        self.wait()

    def run(self):
        self.working.emit()
        main.create(self.path, self.name, self.desc, self.raw)
        return self.finished.emit()


class DeletePopup(QtWidgets.QDialog):
    def __init__(self):
        super(DeletePopup, self).__init__()
        self.ui = Ui_DeletePopup()
        self.ui.setupUi(self)

class createWindow(QtWidgets.QDialog):
    def __init__(self):
        super(createWindow, self).__init__()
        self.ui = Ui_createWindow()
        self.ui.setupUi(self)

        # Path
        self.ui.openPath.clicked.connect(self.updateList)
        self.ui.pathText.textChanged.connect(self.updateImage)

        # Buttons
        self.ui.cancelButton.clicked.connect(self.reject)
        self.ui.createButton.clicked.connect(self.create)
        self.ui.createButton.setDisabled(True)

        global gif
        gif = QtGui.QMovie("icons/loading.gif")
        self.ui.loadingGif.setMovie(gif)

        self.ui.loadingGif.hide()
        self.ui.loadingText.hide()
        self.ui.errorInfo.hide()


    def updateList(self):
        global dialog
        dialog = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.pathText.setText(dialog)

    def updateImage(self):
        if os.path.isdir(dialog):
            self.ui.createButton.setDisabled(False)
            images = []
            for file in os.listdir(dialog):
                if file.endswith(".CR2"):
                    images.append(file)

            for x in images:
                item = QtWidgets.QListWidgetItem()
                icon = "%s/icons/cr2.png" % (os.getcwd())
                print(icon)
                item.setIcon(QtGui.QIcon(icon))
                item.setText(x)
                self.ui.imageList.addItem(item)
        else:
            self.ui.errorInfo.show()
            self.ui.errorInfo.setText("Invalid Path, please select another.")

    def create(self):
        def done():
            gif.stop()
            self.ui.loadingGif.clear()
            self.ui.loadingGif.setText("")
            self.ui.loadingText.setText("Finished!")
            QtCore.QTimer().singleShot(3500, lambda: self.close())
        def working():
            gif.start()
            self.ui.loadingGif.show()
            self.ui.loadingText.show()

        self.ui.errorInfo.hide()
        path = self.ui.pathText.text()
        name = self.ui.createName.text()
        desc = self.ui.createDesc.text()
        raw = self.ui.keepRaw.checkState()
        if len(name) and len(desc) > 1:
            if plist.validateKey(name):
                self.ui.errorInfo.show()
                self.ui.errorInfo.setText("A session with the name '%s' already exist!" % name)
            else:
                self.get_thread = CreateSession(path, name, desc, raw)
                self.get_thread.finished.connect(done)
                self.get_thread.working.connect(working)
                self.get_thread.start()
        else:
            self.ui.errorInfo.show()
            self.ui.errorInfo.setText("Name and Description field must contain more than 1 character.")



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainFrame()
        self.ui.setupUi(self)

        # Startup
        global g
        g = self.ui
        global model
        model = QtGui.QStandardItemModel()

        # MainFrame click
        global defName
        defName = g.sesName.text()
        g.centralwidget.mouseReleaseEvent=self.resetInfo
        g.sesDelete.hide()

        # Delete Button
        g.sesDelete.clicked.connect(self.deleteSession)

        # Filter
        completer = QtWidgets.QCompleter()
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setModel(model)
        g.sesFilter.setCompleter(completer)
        g.sesFilter.show()


        # Session List
        g.sessionList.clicked.connect(self.updateInfo)
        g.sesFilter.textChanged.connect(self.searchList)

        # Create Button
        g.createSesButton.clicked.connect(self.createSession)

        # List Sessions
    def updateList(self):
        model.clear()
        sesList = sessions.iterateSessions()
        for x in sesList:
            item = QtGui.QStandardItem("%s" % x)
            model.appendRow(item)
        g.sessionList.setModel(model)


    def resetInfo(self, event):
        g.sesName.setText(defName)
        g.date_text.clear()
        g.desc_Box.clear()
        g.sesDelete.hide()
        g.sesFilter.clear()

    def updateInfo(self):
        sesKeyObj = g.sessionList.selectedIndexes()[0]
        sesKey = sesKeyObj.data()
        sDate = plist.retrieveData(KEY=sesKey, CONTENT="CreationDate")
        sDesc = plist.retrieveData(KEY=sesKey, CONTENT="Description")
        g.sesName.setText(sesKey)
        g.date_text.setText(sDate)
        g.desc_Box.setText(sDesc)
        g.sesDelete.show()

    def deleteSession(self):
        sesKeyObj = g.sessionList.selectedIndexes()[0]
        sesKey = sesKeyObj.data()
        pop = DeletePopup()
        pop.ui.deleteInfo.setText("Are you sure you want to delete '%s' ?" % sesKey)
        check = pop.exec_()
        if check is 1:
            main.delete(sesKey)
            g.sesFilter.clear()
            self.updateList()
            self.resetInfo(event=None)

    def searchList(self):
        filter_txt = str(g.sesFilter.text()).lower()
        for row in range(model.rowCount()):
            if filter_txt in str(model.item(row).text()).lower():
                g.sessionList.setRowHidden(row, False)
            else:
                g.sessionList.setRowHidden(row, True)



    def createSession(self):
        cwindow = createWindow()
        cwindow.exec_()
        self.updateList()



def start():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.updateList()
    sys.exit(app.exec_())

