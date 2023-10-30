
# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any emanual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Prog2_Prak_PythonPlotter import plotter

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 209)
        self.buOk = QtWidgets.QPushButton(Dialog)
        self.buOk.setGeometry(QtCore.QRect(310, 100, 83, 25))
        self.buOk.setObjectName("buOk")
        self.buReset = QtWidgets.QPushButton(Dialog)
        self.buReset.setGeometry(QtCore.QRect(10, 100, 83, 25))
        self.buReset.setObjectName("buReset")
        self.txtEingabe = QtWidgets.QPlainTextEdit(Dialog)
        self.txtEingabe.setGeometry(QtCore.QRect(10, 20, 381, 70))
        self.txtEingabe.setObjectName("txtEingabe")
        self.txtAusgabe = QtWidgets.QPlainTextEdit(Dialog)
        self.txtAusgabe.setGeometry(QtCore.QRect(10, 130, 381, 70))
        self.txtAusgabe.setObjectName("txtAusgabe")

        self.retranslateUi(Dialog)
        self.buOk.clicked.connect(self.buOk_Click) 
        self.buReset.clicked.connect(self.bbuReset_Click) 
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.buOk.setText(_translate("Dialog", "Ok"))
        self.buReset.setText(_translate("Dialog", "Reset"))

    def buOk_Click(self):
        a = plotter.plot_function(self.txtEingabe, -10, 10, 40, 31) #TODO: zwei weitere Textboxen oder so zum �ndern des anzeigeradiuses :)
        self.txtAusgabe.setPlainText(a)

    def buReset_Click(self):
        self.txtAusgabe.clear
        self.txtEingabe.clear

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())




