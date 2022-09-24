from PyQt6 import QtCore, QtGui, QtWidgets
import sys, math
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox
from ui import Ui_MainWindow

class Otio(QtWidgets.QMainWindow):
    def __init__(self):
        super(Otio,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    def init_UI(self):
        self.setWindowTitle("Otio")
        #self.setWindowIcon(QIcon())

        self.ui.V.setPlaceholderText("Volt(V/U)")
        self.ui.I.setPlaceholderText("Amps(I)")
        self.ui.R.setPlaceholderText("Ohm(R)")
        self.ui.P.setPlaceholderText("Power(P)")

        self.ui.go.clicked.connect(self.OkayLetsGo)

    def OkayLetsGo(self):
        #U/V
        if self.ui.vkpr.isChecked() == True:
            p = self.ui.P.text()
            r = self.ui.R.text()
            pr = math.sqrt(int(r) * int(p))
            dialog = QMessageBox()
            dialog.setText(str(pr))
            dialog.exec()
        elif self.ui.vir.isChecked() == True:
            i = self.ui.I.text()
            r = self.ui.R.text()
            ir = int(i) * int(r)
            dialog = QMessageBox()
            dialog.setText(str(ir))
            dialog.exec()
        elif self.ui.vpi.isChecked() == True:
            p = self.ui.P.text()
            i = self.ui.I.text()
            pi = int(p) / int(i)
            dialog = QMessageBox()
            dialog.setText(str(pi))
            dialog.exec()
        #I
        elif self.ui.iur.isChecked() == True:
            u = self.ui.V.text()
            r = self.ui.R.text()
            ur = int(u) / int(r)
            dialog = QMessageBox()
            dialog.setText(str(ur))
            dialog.exec()
        elif self.ui.ipu.isChecked() == True:
            p = self.ui.P.text()
            u = self.ui.V.text()
            pu = int(p) / int(u)
            dialog = QMessageBox()
            dialog.setText(str(pu))
            dialog.exec()
        elif self.ui.ikpr.isChecked() == True:
            p = self.ui.P.text()
            r = self.ui.R.text()
            pr = math.sqrt(int(p) / int(r))
            dialog = QMessageBox()
            dialog.setText(str(pr))
            dialog.exec()
        #R
        elif self.ui.ru2p.isChecked() == True:
            u = self.ui.V.text()
            p = self.ui.P.text()
            u2p = (int(u) * int(u)) / int(p)
            dialog = QMessageBox()
            dialog.setText(str(u2p))
            dialog.exec()
        elif self.ui.rui.isChecked() == True:
            u = self.ui.V.text()
            i = self.ui.I.text()
            udeli = int(u) / int(i)
            dialog = QMessageBox()
            dialog.setText(str(udeli))
            dialog.exec()
        elif self.ui.rpi2.isChecked() == True:
            p = self.ui.P.text() 
            i = self.ui.I.text()
            pi2 = int(p) / (int(i) * int(i))
            dialog = QMessageBox()
            dialog.setText(str(pi2))
            dialog.exec()
        #P
        elif self.ui.pui.isChecked() == True:
            u = self.ui.V.text()
            i = self.ui.I.text()
            uumi = int(u) * int(i)
            dialog = QMessageBox()
            dialog.setText(str(uumi))
            dialog.exec()
        elif self.ui.pi2r.isChecked() == True:
            i = self.ui.I.text()
            r = self.ui.R.text()
            i2umr = (int(i) * int(i)) * int(r)
            dialog = QMessageBox()
            dialog.setText(str(i2umr))
            dialog.exec()
        elif self.ui.pu2r.isChecked() == True:
            u = self.ui.V.text()
            r = self.ui.R.text()
            u2umr = (int(u) * int(u)) / int(r)
            dialog = QMessageBox()
            dialog.setText(str(u2umr))
            dialog.exec()
    

app = QtWidgets.QApplication([])
application = Otio()
application.show()
sys.exit(app.exec())