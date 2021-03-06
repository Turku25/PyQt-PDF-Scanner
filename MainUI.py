# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from QDisplayFrame import QDisplayFrame


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 710)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(866, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ToolsWidget = QtWidgets.QWidget(self.centralwidget)
        self.ToolsWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolsWidget.sizePolicy().hasHeightForWidth())
        self.ToolsWidget.setSizePolicy(sizePolicy)
        self.ToolsWidget.setMinimumSize(QtCore.QSize(300, 200))
        self.ToolsWidget.setMaximumSize(QtCore.QSize(1000, 200))
        self.ToolsWidget.setBaseSize(QtCore.QSize(500, 200))
        self.ToolsWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ToolsWidget.setObjectName("ToolsWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ToolsWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DeviceSelectLayout = QtWidgets.QVBoxLayout()
        self.DeviceSelectLayout.setObjectName("DeviceSelectLayout")
        self.label = QtWidgets.QLabel(self.ToolsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.DeviceSelectLayout.addWidget(self.label)
        self.DeviceComboBox = QtWidgets.QComboBox(self.ToolsWidget)
        self.DeviceComboBox.setMinimumSize(QtCore.QSize(300, 0))
        self.DeviceComboBox.setObjectName("DeviceComboBox")
        self.DeviceComboBox.addItem("")
        self.DeviceSelectLayout.addWidget(self.DeviceComboBox)
        self.line_3 = QtWidgets.QFrame(self.ToolsWidget)
        self.line_3.setMinimumSize(QtCore.QSize(0, 10))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.DeviceSelectLayout.addWidget(self.line_3)
        self.SearchButton = QtWidgets.QPushButton(self.ToolsWidget)
        self.SearchButton.setObjectName("SearchButton")
        self.DeviceSelectLayout.addWidget(self.SearchButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.DeviceSelectLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.DeviceSelectLayout)
        self.line_4 = QtWidgets.QFrame(self.ToolsWidget)
        self.line_4.setMinimumSize(QtCore.QSize(10, 0))
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 300))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.ScanSizeLayout = QtWidgets.QVBoxLayout()
        self.ScanSizeLayout.setSpacing(6)
        self.ScanSizeLayout.setObjectName("ScanSizeLayout")
        self.ScanSizeLabel = QtWidgets.QLabel(self.ToolsWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.ScanSizeLabel.setFont(font)
        self.ScanSizeLabel.setObjectName("ScanSizeLabel")
        self.ScanSizeLayout.addWidget(self.ScanSizeLabel)
        self.ScanSizeCombo = QtWidgets.QComboBox(self.ToolsWidget)
        self.ScanSizeCombo.setMinimumSize(QtCore.QSize(165, 0))
        self.ScanSizeCombo.setObjectName("ScanSizeCombo")
        self.ScanSizeCombo.addItem("")
        self.ScanSizeCombo.addItem("")
        self.ScanSizeCombo.addItem("")
        self.ScanSizeCombo.addItem("")
        self.ScanSizeCombo.addItem("")
        self.ScanSizeCombo.addItem("")
        self.ScanSizeCombo.addItem("")
        self.ScanSizeLayout.addWidget(self.ScanSizeCombo)
        self.line = QtWidgets.QFrame(self.ToolsWidget)
        self.line.setMinimumSize(QtCore.QSize(0, 10))
        self.line.setBaseSize(QtCore.QSize(0, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.ScanSizeLayout.addWidget(self.line)
        self.UnitLayout = QtWidgets.QHBoxLayout()
        self.UnitLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.UnitLayout.setContentsMargins(0, -1, -1, -1)
        self.UnitLayout.setObjectName("UnitLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.UnitLayout.addItem(spacerItem1)
        self.CustomUnitLabel = QtWidgets.QLabel(self.ToolsWidget)
        self.CustomUnitLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CustomUnitLabel.sizePolicy().hasHeightForWidth())
        self.CustomUnitLabel.setSizePolicy(sizePolicy)
        self.CustomUnitLabel.setObjectName("CustomUnitLabel")
        self.UnitLayout.addWidget(self.CustomUnitLabel)
        self.CustomUnitComboBox = QtWidgets.QComboBox(self.ToolsWidget)
        self.CustomUnitComboBox.setEnabled(False)
        self.CustomUnitComboBox.setMinimumSize(QtCore.QSize(110, 0))
        self.CustomUnitComboBox.setObjectName("CustomUnitComboBox")
        self.CustomUnitComboBox.addItem("")
        self.CustomUnitComboBox.addItem("")
        self.UnitLayout.addWidget(self.CustomUnitComboBox)
        self.ScanSizeLayout.addLayout(self.UnitLayout)
        self.WidthLayout = QtWidgets.QHBoxLayout()
        self.WidthLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.WidthLayout.setObjectName("WidthLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.WidthLayout.addItem(spacerItem2)
        self.CustomWidthLabel = QtWidgets.QLabel(self.ToolsWidget)
        self.CustomWidthLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CustomWidthLabel.sizePolicy().hasHeightForWidth())
        self.CustomWidthLabel.setSizePolicy(sizePolicy)
        self.CustomWidthLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.CustomWidthLabel.setMaximumSize(QtCore.QSize(55, 16777215))
        self.CustomWidthLabel.setObjectName("CustomWidthLabel")
        self.WidthLayout.addWidget(self.CustomWidthLabel)
        self.CustomWidthSpinBox = QtWidgets.QDoubleSpinBox(self.ToolsWidget)
        self.CustomWidthSpinBox.setEnabled(False)
        self.CustomWidthSpinBox.setDecimals(1)
        self.CustomWidthSpinBox.setMaximum(300.0)
        self.CustomWidthSpinBox.setObjectName("CustomWidthSpinBox")
        self.WidthLayout.addWidget(self.CustomWidthSpinBox)
        self.ScanSizeLayout.addLayout(self.WidthLayout)
        self.CustomHeightLayout = QtWidgets.QHBoxLayout()
        self.CustomHeightLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.CustomHeightLayout.setObjectName("CustomHeightLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.CustomHeightLayout.addItem(spacerItem3)
        self.CustomHeightLabel = QtWidgets.QLabel(self.ToolsWidget)
        self.CustomHeightLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CustomHeightLabel.sizePolicy().hasHeightForWidth())
        self.CustomHeightLabel.setSizePolicy(sizePolicy)
        self.CustomHeightLabel.setMaximumSize(QtCore.QSize(55, 16777215))
        self.CustomHeightLabel.setObjectName("CustomHeightLabel")
        self.CustomHeightLayout.addWidget(self.CustomHeightLabel)
        self.CustomHeightSpinBox = QtWidgets.QDoubleSpinBox(self.ToolsWidget)
        self.CustomHeightSpinBox.setEnabled(False)
        self.CustomHeightSpinBox.setDecimals(1)
        self.CustomHeightSpinBox.setMaximum(300.0)
        self.CustomHeightSpinBox.setObjectName("CustomHeightSpinBox")
        self.CustomHeightLayout.addWidget(self.CustomHeightSpinBox)
        self.ScanSizeLayout.addLayout(self.CustomHeightLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ScanSizeLayout.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.ScanSizeLayout)
        self.line_2 = QtWidgets.QFrame(self.ToolsWidget)
        self.line_2.setMinimumSize(QtCore.QSize(10, 0))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.ResolutionLayout = QtWidgets.QVBoxLayout()
        self.ResolutionLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.ResolutionLayout.setObjectName("ResolutionLayout")
        self.ScanQualityLabel = QtWidgets.QLabel(self.ToolsWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ScanQualityLabel.setFont(font)
        self.ScanQualityLabel.setObjectName("ScanQualityLabel")
        self.ResolutionLayout.addWidget(self.ScanQualityLabel)
        self.QualityComboBox = QtWidgets.QComboBox(self.ToolsWidget)
        self.QualityComboBox.setMinimumSize(QtCore.QSize(165, 0))
        self.QualityComboBox.setMaximumSize(QtCore.QSize(165, 16777215))
        self.QualityComboBox.setObjectName("QualityComboBox")
        self.QualityComboBox.addItem("")
        self.QualityComboBox.addItem("")
        self.QualityComboBox.addItem("")
        self.QualityComboBox.addItem("")
        self.QualityComboBox.addItem("")
        self.QualityComboBox.addItem("")
        self.ResolutionLayout.addWidget(self.QualityComboBox)
        self.line_5 = QtWidgets.QFrame(self.ToolsWidget)
        self.line_5.setMinimumSize(QtCore.QSize(0, 10))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.ResolutionLayout.addWidget(self.line_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.ToolsWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ColorRadio = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ColorRadio.setFont(font)
        self.ColorRadio.setChecked(True)
        self.ColorRadio.setObjectName("ColorRadio")
        self.verticalLayout_4.addWidget(self.ColorRadio)
        self.GrayRadio = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GrayRadio.setFont(font)
        self.GrayRadio.setObjectName("GrayRadio")
        self.verticalLayout_4.addWidget(self.GrayRadio)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.ToolsWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PortraitRadio = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PortraitRadio.setFont(font)
        self.PortraitRadio.setChecked(True)
        self.PortraitRadio.setObjectName("PortraitRadio")
        self.verticalLayout.addWidget(self.PortraitRadio)
        self.LandscapeRadio = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LandscapeRadio.setFont(font)
        self.LandscapeRadio.setObjectName("LandscapeRadio")
        self.verticalLayout.addWidget(self.LandscapeRadio)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.ResolutionLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.ResolutionLayout)
        self.line_9 = QtWidgets.QFrame(self.ToolsWidget)
        self.line_9.setMinimumSize(QtCore.QSize(10, 0))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout.addWidget(self.line_9)
        self.verticalLayout_2.addWidget(self.ToolsWidget)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_2.addWidget(self.line_6)
        self.ScanButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ScanButton.setFont(font)
        self.ScanButton.setObjectName("ScanButton")
        self.verticalLayout_2.addWidget(self.ScanButton)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_2.addWidget(self.line_7)
        self.DisplayFrame = QDisplayFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DisplayFrame.sizePolicy().hasHeightForWidth())
        self.DisplayFrame.setSizePolicy(sizePolicy)
        self.DisplayFrame.setObjectName("DisplayFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.DisplayFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2.addWidget(self.DisplayFrame)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_2.addWidget(self.line_8)
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.SaveButton.setFont(font)
        self.SaveButton.setObjectName("SaveButton")
        self.verticalLayout_2.addWidget(self.SaveButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.QualityComboBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Scan Device: "))
        self.DeviceComboBox.setItemText(0, _translate("MainWindow", "No Devices Found"))
        self.SearchButton.setText(_translate("MainWindow", "Scan For Devices"))
        self.ScanSizeLabel.setText(_translate("MainWindow", "Scan Size:"))
        self.ScanSizeCombo.setItemText(0, _translate("MainWindow", "Letter  (8.5 x 11 in)"))
        self.ScanSizeCombo.setItemText(1, _translate("MainWindow", "Legal (8.5 x 14 in)"))
        self.ScanSizeCombo.setItemText(2, _translate("MainWindow", "A3 (297 x 420 mm)"))
        self.ScanSizeCombo.setItemText(3, _translate("MainWindow", "A4 (210 x 297 mm)"))
        self.ScanSizeCombo.setItemText(4, _translate("MainWindow", "A5 (148 x 210 mm)"))
        self.ScanSizeCombo.setItemText(5, _translate("MainWindow", "A6 (105 x 148 mm)"))
        self.ScanSizeCombo.setItemText(6, _translate("MainWindow", "Custom"))
        self.CustomUnitLabel.setText(_translate("MainWindow", "Unit: "))
        self.CustomUnitComboBox.setItemText(0, _translate("MainWindow", "Inches"))
        self.CustomUnitComboBox.setItemText(1, _translate("MainWindow", "MIllimeters"))
        self.CustomWidthLabel.setText(_translate("MainWindow", "Width: "))
        self.CustomHeightLabel.setText(_translate("MainWindow", "Height: "))
        self.ScanQualityLabel.setText(_translate("MainWindow", "Scan Details:"))
        self.QualityComboBox.setItemText(0, _translate("MainWindow", "75 dpi (Draft)"))
        self.QualityComboBox.setItemText(1, _translate("MainWindow", "150 dpi"))
        self.QualityComboBox.setItemText(2, _translate("MainWindow", "300 dpi (Default)"))
        self.QualityComboBox.setItemText(3, _translate("MainWindow", "600 dpi"))
        self.QualityComboBox.setItemText(4, _translate("MainWindow", "1200 dpi (High Res)"))
        self.QualityComboBox.setItemText(5, _translate("MainWindow", "2400 dpi"))
        self.groupBox.setTitle(_translate("MainWindow", "Color:"))
        self.ColorRadio.setText(_translate("MainWindow", "Color"))
        self.GrayRadio.setText(_translate("MainWindow", "Grayscale"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Orientation: "))
        self.PortraitRadio.setText(_translate("MainWindow", "Portrait"))
        self.LandscapeRadio.setText(_translate("MainWindow", "Landscape"))
        self.ScanButton.setText(_translate("MainWindow", "Scan"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
