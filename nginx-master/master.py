# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'master.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setFixedSize(519, 520)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.submit = QtGui.QPushButton(Dialog)
        self.submit.setGeometry(QtCore.QRect(270, 170, 121, 27))
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.domainName = QtGui.QLineEdit(Dialog)
        self.domainName.setGeometry(QtCore.QRect(210, 30, 281, 31))
        self.domainName.setObjectName(_fromUtf8("domainName"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 10, 141, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 70, 141, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.projectPath = QtGui.QLineEdit(Dialog)
        self.projectPath.setGeometry(QtCore.QRect(210, 90, 281, 31))
        self.projectPath.setObjectName(_fromUtf8("projectPath"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(170, -20, 20, 241))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.updateHosts = QtGui.QCheckBox(Dialog)
        self.updateHosts.setGeometry(QtCore.QRect(270, 130, 151, 22))
        self.updateHosts.setObjectName(_fromUtf8("updateHosts"))
        self.updateHosts.setChecked(True)
        self.statusBox = QtGui.QTextBrowser(Dialog)
        self.statusBox.setEnabled(False)
        self.statusBox.setGeometry(QtCore.QRect(-1, 220, 521, 301))
        self.statusBox.setObjectName(_fromUtf8("statusBox"))
        self.restartNginx = QtGui.QPushButton(Dialog)
        self.restartNginx.setGeometry(QtCore.QRect(10, 90, 151, 27))
        self.restartNginx.setObjectName(_fromUtf8("restartNginx"))
        self.stopNginx = QtGui.QPushButton(Dialog)
        self.stopNginx.setGeometry(QtCore.QRect(10, 50, 151, 27))
        self.stopNginx.setObjectName(_fromUtf8("stopNginx"))
        self.startNginx = QtGui.QPushButton(Dialog)
        self.startNginx.setGeometry(QtCore.QRect(10, 10, 151, 27))
        self.startNginx.setObjectName(_fromUtf8("startNginx"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 210, 521, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setEnabled(True)
        self.line_3.setGeometry(QtCore.QRect(510, 0, 20, 221))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        ##################################################################################
        # self.statusBox.setText(os.popen4("service nginx status")[1].read())
        self.submit.clicked.connect(self.submitClicked)
        self.startNginx.clicked.connect(self.startClicked)
        self.stopNginx.clicked.connect(self.stopClicked)
        self.restartNginx.clicked.connect(self.restartClicked)
        ##################################################################################
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    ##########################My Functions ################################################
    def startClicked(self):
        status = 'Please open with sudo privilege.'
        try:
            os.system('service nginx start')
            status = 'NGINX Started'
            self.statusBox.setText(status)
        except Exception as e:
            print(str(e))
        self.statusBox.setText(status)

    def stopClicked(self):
        status = 'Please open with sudo privilege.'
        try:
            os.system('service nginx stop')
            status = 'NGINX Stopped'
            self.statusBox.setText(status)
        except Exception as e:
            print(str(e))
        self.statusBox.setText(status)

    def restartClicked(self):
        status = 'Please open with sudo privilege.'
        try:
            os.system('service nginx restart')
            status = 'NGINX Restarted'
            self.statusBox.setText(status)
        except Exception as e:
            print(str(e))
        self.statusBox.setText(status)

    def submitClicked(self):
        print('Created By: Rafik Farhad\nmailto:<rafikfarhad@gmail.com>\n')
        domain = str(self.domainName.text())
        project = str(self.projectPath.text())
        status = 'Domain name:     '
        status += domain
        status += "\nProject Path:       "
        status += project
        status += "\n"
        fileString = open(os.path.dirname(os.path.abspath(__file__)) + '/conf.txt', 'r').read()
        fileString = fileString.replace('###', project)
        fileString = fileString.replace('***', domain)
        fileNamePath = '/etc/nginx/sites-enabled/' + domain
        tempFileNamePath = '/tmp/' + domain
        try:
            # os.system('touch ' + fileNamePath)
            file = open(tempFileNamePath, 'w')
            file.write(fileString + '\n')
            file.close()
            os.system('cp ' + tempFileNamePath + ' ' + fileNamePath)
        except Exception as e:
            print(e)
            self.statusBox.setText('Please open with sudo privilege.\n' + str(e))
            return
        if self.updateHosts.isChecked():
            file = open('/etc/hosts', 'a')
            file.write('127.0.0.1  ' + domain)
            file.close()
            status += '\n\n/etc/hosts updated...'
        status += '\n\nTesting conf file integrity...\n\n'
        status += str(os.popen4("nginx -t")[1].read())
        status += '\n\nRestarting NGINX...\n\n'
        os.system('service nginx reload')
        status += 'Restart Completed.\n\nThank You.'
        self.statusBox.setText(status)

    #######################################################################################
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "NGINX - Master v1.0", None))
        self.submit.setText(_translate("Dialog", "Create Config", None))
        self.domainName.setText(_translate("Dialog", "hello.farhad.me", None))
        self.label.setText(_translate("Dialog", "Domain Name", None))
        self.label_2.setText(_translate("Dialog", "Project Path", None))
        self.projectPath.setText(_translate("Dialog", "/home/farhad/html/laravel/public", None))
        self.updateHosts.setText(_translate("Dialog", "Update /etc/hosts", None))
        self.restartNginx.setText(_translate("Dialog", "Restart NGINX", None))
        self.stopNginx.setText(_translate("Dialog", "Stop NGINX", None))
        self.startNginx.setText(_translate("Dialog", "Start NGINX", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

