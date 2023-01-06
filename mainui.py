from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMessageBox
import sys, math
from ui import Ui_MainWindow

class otioWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(otioWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def CreateMGB(self, symv):
        dialog = QMessageBox()
        dialog.setWindowTitle("Message Dialog")
        dialog.setText(symv)
        ret = dialog.exec()

    def init_UI(self):
        self.ui.uText.setPlaceholderText("U")
        self.ui.iText.setPlaceholderText("I")
        self.ui.rText.setPlaceholderText("R")
        self.ui.pText.setPlaceholderText("P")
        self.ui.pushButton.clicked.connect(self.qwerty)

    def qwerty(self):
        uText = self.ui.uText.text()
        iText = self.ui.iText.text()
        rText = self.ui.rText.text()
        pText = self.ui.pText.text()
        #U
        if self.ui.ukpur.isChecked() == True:
            num11 = math.sqrt(float(pText))
            num21 = math.sqrt(float(rText))
            num31 = num11 * num21
            self.CreateMGB(str(num31))
        if self.ui.uiur.isChecked() == True:
            uiur = float(iText) * float(rText)
            self.CreateMGB(str(uiur))
        if self.ui.updi.isChecked() == True:
            updi = float(pText) / float(iText)
            self.CreateMGB(str(updi))
        #I
        if self.ui.iudr.isChecked() == True:
            iudr = float(uText) / float(rText)
            self.CreateMGB(str(iudr))
        if self.ui.ipdu.isChecked() == True:
            ipdu = float(pText) / float(uText)
            self.CreateMGB(str(ipdu))
        if self.ui.ikpdr.isChecked() == True:
            num12 = math.sqrt(float(pText))
            num22 = math.sqrt(float(rText))
            num32 = num12 / num22
            self.CreateMGB(str(num32))
        #P
        if self.ui.puui.isChecked() == True:
            puui = float(uText) * float(iText)
            self.CreateMGB(str(puui))
        if self.ui.pi2ur.isChecked() == True:
            pi2ur = (float(iText) * float(iText)) * float(rText)
            self.CreateMGB(str(pi2ur))
        if self.ui.pu2dr.isChecked() == True:
            pu2dr = (float(uText) * float(uText)) / float(rText)
            self.CreateMGB(str(pu2dr))
        #R
        if self.ui.rpdi2.isChecked() == True:
            rpdi2 = float(pText) / (float(iText) * float(iText))
            self.CreateMGB(str(rpdi2))
        if self.ui.rudi.isChecked() == True:
            rudi = float(uText) / float(iText)
            self.CreateMGB(str(rudi))
        if self.ui.ru2dp.isChecked() == True:
            ru2dp = (float(uText) * float(uText)) / float(pText)
            self.CreateMGB(str(ru2dp))

app = QtWidgets.QApplication([])
application = otioWindow()
application.show()

sys.exit(app.exec())
