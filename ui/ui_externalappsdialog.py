# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'externalappsdialog.ui'
#
# Created: Mon Oct 01 11:16:29 2012
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ExternalAppsDialog(object):
    def setupUi(self, ExternalAppsDialog):
        ExternalAppsDialog.setObjectName(_fromUtf8("ExternalAppsDialog"))
        ExternalAppsDialog.resize(595, 151)
        self.verticalLayout = QtGui.QVBoxLayout(ExternalAppsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.comboBoxCategory = QtGui.QComboBox(ExternalAppsDialog)
        self.comboBoxCategory.setObjectName(_fromUtf8("comboBoxCategory"))
        self.gridLayout.addWidget(self.comboBoxCategory, 0, 1, 1, 1)
        self.buttonNewCategory = QtGui.QPushButton(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonNewCategory.sizePolicy().hasHeightForWidth())
        self.buttonNewCategory.setSizePolicy(sizePolicy)
        self.buttonNewCategory.setObjectName(_fromUtf8("buttonNewCategory"))
        self.gridLayout.addWidget(self.buttonNewCategory, 0, 2, 1, 1)
        self.buttonDeleteCategory = QtGui.QPushButton(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDeleteCategory.sizePolicy().hasHeightForWidth())
        self.buttonDeleteCategory.setSizePolicy(sizePolicy)
        self.buttonDeleteCategory.setObjectName(_fromUtf8("buttonDeleteCategory"))
        self.gridLayout.addWidget(self.buttonDeleteCategory, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditAppCmdPattern = QtGui.QLineEdit(ExternalAppsDialog)
        self.lineEditAppCmdPattern.setReadOnly(False)
        self.lineEditAppCmdPattern.setObjectName(_fromUtf8("lineEditAppCmdPattern"))
        self.gridLayout.addWidget(self.lineEditAppCmdPattern, 1, 1, 1, 2)
        self.buttonSelectApp = QtGui.QPushButton(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSelectApp.sizePolicy().hasHeightForWidth())
        self.buttonSelectApp.setSizePolicy(sizePolicy)
        self.buttonSelectApp.setObjectName(_fromUtf8("buttonSelectApp"))
        self.gridLayout.addWidget(self.buttonSelectApp, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(ExternalAppsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditFileExtensions = QtGui.QLineEdit(ExternalAppsDialog)
        self.lineEditFileExtensions.setObjectName(_fromUtf8("lineEditFileExtensions"))
        self.gridLayout.addWidget(self.lineEditFileExtensions, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(ExternalAppsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ExternalAppsDialog)
        QtCore.QMetaObject.connectSlotsByName(ExternalAppsDialog)

    def retranslateUi(self, ExternalAppsDialog):
        ExternalAppsDialog.setWindowTitle(QtGui.QApplication.translate("ExternalAppsDialog", "Preferred External Applications", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ExternalAppsDialog", "Category of files:", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonNewCategory.setText(QtGui.QApplication.translate("ExternalAppsDialog", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDeleteCategory.setText(QtGui.QApplication.translate("ExternalAppsDialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ExternalAppsDialog", "Executable:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditAppCmdPattern.setToolTip(QtGui.QApplication.translate("ExternalAppsDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Syntax: </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;path to executable&gt; &lt;replacement fields&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Replacement fields could be:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">%f - will be replaced with file name;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">%d - will be replaced with containing directory of the file.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSelectApp.setText(QtGui.QApplication.translate("ExternalAppsDialog", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ExternalAppsDialog", "File extensions:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditFileExtensions.setToolTip(QtGui.QApplication.translate("ExternalAppsDialog", "File extentions, separated with spaces, e.g. \".txt .doc .csv\"", None, QtGui.QApplication.UnicodeUTF8))
