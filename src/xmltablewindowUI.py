# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XMLTableWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TableWidgetThing(object):
    def setupUi(self, TableWidgetThing):
        TableWidgetThing.setObjectName("TableWidgetThing")
        TableWidgetThing.resize(1181, 586)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TableWidgetThing)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xmltable = QtWidgets.QTableWidget(TableWidgetThing)
        self.xmltable.setObjectName("xmltable")
        self.xmltable.setColumnCount(0)
        self.xmltable.setRowCount(0)
        self.horizontalLayout.addWidget(self.xmltable)
        self.frame = QtWidgets.QFrame(TableWidgetThing)
        self.frame.setMinimumSize(QtCore.QSize(800, 0))
        self.frame.setMaximumSize(QtCore.QSize(800, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.framex_label = QtWidgets.QLabel(self.frame_2)
        self.framex_label.setObjectName("framex_label")
        self.horizontalLayout_2.addWidget(self.framex_label)
        self.framex_spinbox = QtWidgets.QSpinBox(self.frame_2)
        self.framex_spinbox.setMinimum(-10000)
        self.framex_spinbox.setMaximum(10000)
        self.framex_spinbox.setObjectName("framex_spinbox")
        self.horizontalLayout_2.addWidget(self.framex_spinbox)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.framey_label = QtWidgets.QLabel(self.frame_2)
        self.framey_label.setObjectName("framey_label")
        self.horizontalLayout_3.addWidget(self.framey_label)
        self.framey_spinbox = QtWidgets.QSpinBox(self.frame_2)
        self.framey_spinbox.setMinimum(-10000)
        self.framey_spinbox.setMaximum(10000)
        self.framey_spinbox.setObjectName("framey_spinbox")
        self.horizontalLayout_3.addWidget(self.framey_spinbox)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.framewidth_label = QtWidgets.QLabel(self.frame_2)
        self.framewidth_label.setObjectName("framewidth_label")
        self.horizontalLayout_4.addWidget(self.framewidth_label)
        self.framewidth_spinbox = QtWidgets.QSpinBox(self.frame_2)
        self.framewidth_spinbox.setMinimum(1)
        self.framewidth_spinbox.setMaximum(10000)
        self.framewidth_spinbox.setObjectName("framewidth_spinbox")
        self.horizontalLayout_4.addWidget(self.framewidth_spinbox)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frameheight_label = QtWidgets.QLabel(self.frame_2)
        self.frameheight_label.setObjectName("frameheight_label")
        self.horizontalLayout_5.addWidget(self.frameheight_label)
        self.frameheight_spinbox = QtWidgets.QSpinBox(self.frame_2)
        self.frameheight_spinbox.setMinimum(1)
        self.frameheight_spinbox.setMaximum(10000)
        self.frameheight_spinbox.setObjectName("frameheight_spinbox")
        self.horizontalLayout_5.addWidget(self.frameheight_spinbox)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.frame_2)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 774, 456))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_preview_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_preview_label.sizePolicy().hasHeightForWidth())
        self.frame_preview_label.setSizePolicy(sizePolicy)
        self.frame_preview_label.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_preview_label.setAlignment(QtCore.Qt.AlignCenter)
        self.frame_preview_label.setObjectName("frame_preview_label")
        self.gridLayout.addWidget(self.frame_preview_label, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.frame_info_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame_info_label.setFont(font)
        self.frame_info_label.setObjectName("frame_info_label")
        self.verticalLayout.addWidget(self.frame_info_label)
        self.horizontalLayout.addWidget(self.frame)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(TableWidgetThing)
        QtCore.QMetaObject.connectSlotsByName(TableWidgetThing)

    def retranslateUi(self, TableWidgetThing):
        _translate = QtCore.QCoreApplication.translate
        TableWidgetThing.setWindowTitle(_translate("TableWidgetThing", "XML Table View"))
        self.framex_label.setText(_translate("TableWidgetThing", "FrameX"))
        self.framey_label.setText(_translate("TableWidgetThing", "FrameY"))
        self.framewidth_label.setText(_translate("TableWidgetThing", "FrameWidth"))
        self.frameheight_label.setText(_translate("TableWidgetThing", "FrameHeight"))
        self.frame_preview_label.setText(_translate("TableWidgetThing", "Frame preview goes here"))
        self.frame_info_label.setText(_translate("TableWidgetThing", "Info about the frame"))
