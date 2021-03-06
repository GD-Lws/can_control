# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 0, 213, 545))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 3, 0, 1, 2)
        self.button_mc_close = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_mc_close.setMaximumSize(QtCore.QSize(16770000, 16777215))
        self.button_mc_close.setDefault(False)
        self.button_mc_close.setObjectName("button_mc_close")
        self.gridLayout_2.addWidget(self.button_mc_close, 5, 1, 1, 1)
        self.button_pid_set = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_pid_set.setMaximumSize(QtCore.QSize(16770000, 16777215))
        self.button_pid_set.setDefault(False)
        self.button_pid_set.setObjectName("button_pid_set")
        self.gridLayout_2.addWidget(self.button_pid_set, 15, 1, 1, 1)
        self.button_pid_control = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_pid_control.setMaximumSize(QtCore.QSize(16770000, 16777215))
        self.button_pid_control.setDefault(False)
        self.button_pid_control.setObjectName("button_pid_control")
        self.gridLayout_2.addWidget(self.button_pid_control, 15, 0, 1, 1)
        self.label_kd = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_kd.setObjectName("label_kd")
        self.gridLayout_2.addWidget(self.label_kd, 14, 0, 1, 1)
        self.button_enable = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_enable.setDefault(False)
        self.button_enable.setObjectName("button_enable")
        self.gridLayout_2.addWidget(self.button_enable, 4, 0, 1, 1)
        self.edit_kp = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edit_kp.setObjectName("edit_kp")
        self.gridLayout_2.addWidget(self.edit_kp, 12, 1, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_2.addWidget(self.line_9, 0, 0, 1, 2)
        self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 10, 0, 1, 2)
        self.button_speed_single = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_speed_single.setMaximumSize(QtCore.QSize(16770000, 16777215))
        self.button_speed_single.setDefault(False)
        self.button_speed_single.setObjectName("button_speed_single")
        self.gridLayout_2.addWidget(self.button_speed_single, 8, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 6, 0, 1, 2)
        self.label_single_encode = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_single_encode.setObjectName("label_single_encode")
        self.gridLayout_2.addWidget(self.label_single_encode, 17, 0, 1, 1)
        self.button_disable = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_disable.setDefault(False)
        self.button_disable.setObjectName("button_disable")
        self.gridLayout_2.addWidget(self.button_disable, 4, 1, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 18, 0, 1, 2)
        self.edit_speed_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edit_speed_input.setObjectName("edit_speed_input")
        self.gridLayout_2.addWidget(self.edit_speed_input, 7, 1, 1, 1)
        self.edit_kd = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edit_kd.setObjectName("edit_kd")
        self.gridLayout_2.addWidget(self.edit_kd, 14, 1, 1, 1)
        self.button_mc_open = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_mc_open.setMaximumSize(QtCore.QSize(16770000, 16777215))
        self.button_mc_open.setDefault(False)
        self.button_mc_open.setObjectName("button_mc_open")
        self.gridLayout_2.addWidget(self.button_mc_open, 5, 0, 1, 1)
        self.label_speed = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_speed.setObjectName("label_speed")
        self.gridLayout_2.addWidget(self.label_speed, 7, 0, 1, 1)
        self.button_derive_close = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_derive_close.setDefault(False)
        self.button_derive_close.setObjectName("button_derive_close")
        self.gridLayout_2.addWidget(self.button_derive_close, 2, 1, 1, 1)
        self.edit_ki = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edit_ki.setObjectName("edit_ki")
        self.gridLayout_2.addWidget(self.edit_ki, 13, 1, 1, 1)
        self.label_kp = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_kp.setObjectName("label_kp")
        self.gridLayout_2.addWidget(self.label_kp, 12, 0, 1, 1)
        self.button_derive_open = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_derive_open.setDefault(False)
        self.button_derive_open.setObjectName("button_derive_open")
        self.gridLayout_2.addWidget(self.button_derive_open, 2, 0, 1, 1)
        self.label_encode_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_encode_2.setObjectName("label_encode_2")
        self.gridLayout_2.addWidget(self.label_encode_2, 19, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 16, 0, 1, 2)
        self.edit_encode_single = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edit_encode_single.setObjectName("edit_encode_single")
        self.gridLayout_2.addWidget(self.edit_encode_single, 17, 1, 1, 1)
        self.button_speed_continue_start = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_speed_continue_start.setMaximumSize(QtCore.QSize(16770000, 16777215))
        self.button_speed_continue_start.setDefault(False)
        self.button_speed_continue_start.setObjectName("button_speed_continue_start")
        self.gridLayout_2.addWidget(self.button_speed_continue_start, 8, 0, 1, 1)
        self.textbrowser_log = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textbrowser_log.setObjectName("textbrowser_log")
        self.gridLayout_2.addWidget(self.textbrowser_log, 20, 0, 1, 2)
        self.label_ki = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_ki.setObjectName("label_ki")
        self.gridLayout_2.addWidget(self.label_ki, 13, 0, 1, 1)
        self.edit_encode_multi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edit_encode_multi.setObjectName("edit_encode_multi")
        self.gridLayout_2.addWidget(self.edit_encode_multi, 19, 1, 1, 1)
        self.button_speed_continue_close = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_speed_continue_close.setMaximumSize(QtCore.QSize(16770000, 16777215))
        self.button_speed_continue_close.setDefault(False)
        self.button_speed_continue_close.setObjectName("button_speed_continue_close")
        self.gridLayout_2.addWidget(self.button_speed_continue_close, 9, 0, 1, 1)
        self.graphicsViewl = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsViewl.setGeometry(QtCore.QRect(250, 0, 531, 541))
        self.graphicsViewl.setObjectName("graphicsViewl")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(570, 540, 193, 3))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CanDerive"))
        self.button_mc_close.setText(_translate("MainWindow", "??????????????????"))
        self.button_pid_set.setText(_translate("MainWindow", "??????"))
        self.button_pid_control.setText(_translate("MainWindow", "pid??????"))
        self.label_kd.setText(_translate("MainWindow", "KD"))
        self.button_enable.setText(_translate("MainWindow", "????????????"))
        self.button_speed_single.setText(_translate("MainWindow", "????????????"))
        self.label_single_encode.setText(_translate("MainWindow", "?????????????????????"))
        self.button_disable.setText(_translate("MainWindow", "????????????"))
        self.button_mc_open.setText(_translate("MainWindow", "??????????????????"))
        self.label_speed.setText(_translate("MainWindow", "????????????"))
        self.button_derive_close.setText(_translate("MainWindow", "CAN??????"))
        self.label_kp.setText(_translate("MainWindow", "KP"))
        self.button_derive_open.setText(_translate("MainWindow", "CAN??????"))
        self.label_encode_2.setText(_translate("MainWindow", "?????????????????????"))
        self.button_speed_continue_start.setText(_translate("MainWindow", "??????????????????"))
        self.label_ki.setText(_translate("MainWindow", "KI"))
        self.button_speed_continue_close.setText(_translate("MainWindow", "??????????????????"))
