# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStatusBar, QTabWidget, QTableView, QTextEdit,
    QTreeView, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 793)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBarWidget = QWidget(self.centralwidget)
        self.toolBarWidget.setObjectName(u"toolBarWidget")
        self.toolBarWidget.setMinimumSize(QSize(0, 40))
        self.toolBarWidget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.toolBarWidget)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.newButton = QPushButton(self.toolBarWidget)
        self.newButton.setObjectName(u"newButton")

        self.horizontalLayout.addWidget(self.newButton)

        self.openButton = QPushButton(self.toolBarWidget)
        self.openButton.setObjectName(u"openButton")

        self.horizontalLayout.addWidget(self.openButton)

        self.saveButton = QPushButton(self.toolBarWidget)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.runButton = QPushButton(self.toolBarWidget)
        self.runButton.setObjectName(u"runButton")

        self.horizontalLayout.addWidget(self.runButton)

        self.stopButton = QPushButton(self.toolBarWidget)
        self.stopButton.setObjectName(u"stopButton")

        self.horizontalLayout.addWidget(self.stopButton)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.offlineButton = QPushButton(self.toolBarWidget)
        self.offlineButton.setObjectName(u"offlineButton")

        self.horizontalLayout.addWidget(self.offlineButton)

        self.onlineButton = QPushButton(self.toolBarWidget)
        self.onlineButton.setObjectName(u"onlineButton")

        self.horizontalLayout.addWidget(self.onlineButton)

        self.displayButton = QPushButton(self.toolBarWidget)
        self.displayButton.setObjectName(u"displayButton")

        self.horizontalLayout.addWidget(self.displayButton)

        self.packetToolButton = QPushButton(self.toolBarWidget)
        self.packetToolButton.setObjectName(u"packetToolButton")
        self.packetToolButton.setVisible(False)

        self.horizontalLayout.addWidget(self.packetToolButton)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.envLabel = QLabel(self.toolBarWidget)
        self.envLabel.setObjectName(u"envLabel")

        self.horizontalLayout.addWidget(self.envLabel)

        self.envComboBox = QComboBox(self.toolBarWidget)
        self.envComboBox.addItem("")
        self.envComboBox.addItem("")
        self.envComboBox.addItem("")
        self.envComboBox.setObjectName(u"envComboBox")

        self.horizontalLayout.addWidget(self.envComboBox)


        self.verticalLayout.addWidget(self.toolBarWidget)

        self.mainSplitter = QSplitter(self.centralwidget)
        self.mainSplitter.setObjectName(u"mainSplitter")
        self.mainSplitter.setOrientation(Qt.Horizontal)
        self.fileExplorerWidget = QWidget(self.mainSplitter)
        self.fileExplorerWidget.setObjectName(u"fileExplorerWidget")
        self.fileExplorerWidget.setMinimumSize(QSize(250, 0))
        self.fileExplorerWidget.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.fileExplorerWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fileExplorerLabel = QLabel(self.fileExplorerWidget)
        self.fileExplorerLabel.setObjectName(u"fileExplorerLabel")

        self.verticalLayout_2.addWidget(self.fileExplorerLabel)

        self.fileExplorerTreeView = QTreeView(self.fileExplorerWidget)
        self.fileExplorerTreeView.setObjectName(u"fileExplorerTreeView")

        self.verticalLayout_2.addWidget(self.fileExplorerTreeView)

        self.deviceListWidget = QWidget(self.fileExplorerWidget)
        self.deviceListWidget.setObjectName(u"deviceListWidget")
        self.deviceListWidget.setMinimumSize(QSize(0, 200))
        self.verticalLayout_8 = QVBoxLayout(self.deviceListWidget)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 4, 0, 0)
        self.deviceListLabel = QLabel(self.deviceListWidget)
        self.deviceListLabel.setObjectName(u"deviceListLabel")

        self.verticalLayout_8.addWidget(self.deviceListLabel)

        self.deviceListView = QListWidget(self.deviceListWidget)
        QListWidgetItem(self.deviceListView)
        QListWidgetItem(self.deviceListView)
        QListWidgetItem(self.deviceListView)
        self.deviceListView.setObjectName(u"deviceListView")
        self.deviceListView.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_8.addWidget(self.deviceListView)

        self.deviceToolsWidget = QWidget(self.deviceListWidget)
        self.deviceToolsWidget.setObjectName(u"deviceToolsWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.deviceToolsWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.selectedDeviceLabel = QLabel(self.deviceToolsWidget)
        self.selectedDeviceLabel.setObjectName(u"selectedDeviceLabel")

        self.horizontalLayout_3.addWidget(self.selectedDeviceLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.refreshButton = QPushButton(self.deviceToolsWidget)
        self.refreshButton.setObjectName(u"refreshButton")

        self.horizontalLayout_3.addWidget(self.refreshButton)

        self.sendPacketButton = QPushButton(self.deviceToolsWidget)
        self.sendPacketButton.setObjectName(u"sendPacketButton")

        self.horizontalLayout_3.addWidget(self.sendPacketButton)


        self.verticalLayout_8.addWidget(self.deviceToolsWidget)


        self.verticalLayout_2.addWidget(self.deviceListWidget)

        self.mainSplitter.addWidget(self.fileExplorerWidget)
        self.editorSplitter = QSplitter(self.mainSplitter)
        self.editorSplitter.setObjectName(u"editorSplitter")
        self.editorSplitter.setOrientation(Qt.Vertical)
        self.editorTabWidget = QTabWidget(self.editorSplitter)
        self.editorTabWidget.setObjectName(u"editorTabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.codeEditor = QTextEdit(self.tab)
        self.codeEditor.setObjectName(u"codeEditor")

        self.verticalLayout_3.addWidget(self.codeEditor)

        self.editorTabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.editorTabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.editorTabWidget.addTab(self.tab_3, "")
        self.registerEditorTab = QWidget()
        self.registerEditorTab.setObjectName(u"registerEditorTab")
        self.editorTabWidget.addTab(self.registerEditorTab, "")
        self.editorSplitter.addWidget(self.editorTabWidget)
        self.logSplitter = QSplitter(self.editorSplitter)
        self.logSplitter.setObjectName(u"logSplitter")
        self.logSplitter.setOrientation(Qt.Horizontal)
        self.dataBrowserWidget = QWidget(self.logSplitter)
        self.dataBrowserWidget.setObjectName(u"dataBrowserWidget")
        self.verticalLayout_4 = QVBoxLayout(self.dataBrowserWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.dataBrowserLabel = QLabel(self.dataBrowserWidget)
        self.dataBrowserLabel.setObjectName(u"dataBrowserLabel")

        self.verticalLayout_4.addWidget(self.dataBrowserLabel)

        self.packetCaptureTableView = QTableView(self.dataBrowserWidget)
        self.packetCaptureTableView.setObjectName(u"packetCaptureTableView")

        self.verticalLayout_4.addWidget(self.packetCaptureTableView)

        self.logSplitter.addWidget(self.dataBrowserWidget)
        self.logWidget = QWidget(self.logSplitter)
        self.logWidget.setObjectName(u"logWidget")
        self.verticalLayout_5 = QVBoxLayout(self.logWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.logLabel = QLabel(self.logWidget)
        self.logLabel.setObjectName(u"logLabel")

        self.verticalLayout_5.addWidget(self.logLabel)

        self.logTableView = QTableView(self.logWidget)
        self.logTableView.setObjectName(u"logTableView")

        self.verticalLayout_5.addWidget(self.logTableView)

        self.logSplitter.addWidget(self.logWidget)
        self.editorSplitter.addWidget(self.logSplitter)
        self.mainSplitter.addWidget(self.editorSplitter)
        self.diagnosticsWidget = QWidget(self.mainSplitter)
        self.diagnosticsWidget.setObjectName(u"diagnosticsWidget")
        self.diagnosticsWidget.setMinimumSize(QSize(250, 0))
        self.diagnosticsWidget.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.diagnosticsWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.diagnosticsLabel = QLabel(self.diagnosticsWidget)
        self.diagnosticsLabel.setObjectName(u"diagnosticsLabel")
        self.diagnosticsLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.diagnosticsLabel)

        self.codeLabel = QLabel(self.diagnosticsWidget)
        self.codeLabel.setObjectName(u"codeLabel")

        self.verticalLayout_6.addWidget(self.codeLabel)

        self.diagCodeLabel = QLabel(self.diagnosticsWidget)
        self.diagCodeLabel.setObjectName(u"diagCodeLabel")

        self.verticalLayout_6.addWidget(self.diagCodeLabel)

        self.actionLabel = QLabel(self.diagnosticsWidget)
        self.actionLabel.setObjectName(u"actionLabel")

        self.verticalLayout_6.addWidget(self.actionLabel)

        self.diagActionLabel = QLabel(self.diagnosticsWidget)
        self.diagActionLabel.setObjectName(u"diagActionLabel")

        self.verticalLayout_6.addWidget(self.diagActionLabel)

        self.contentLabel = QLabel(self.diagnosticsWidget)
        self.contentLabel.setObjectName(u"contentLabel")

        self.verticalLayout_6.addWidget(self.contentLabel)

        self.tableLabel = QLabel(self.diagnosticsWidget)
        self.tableLabel.setObjectName(u"tableLabel")

        self.verticalLayout_6.addWidget(self.tableLabel)

        self.tableNameLabel = QLabel(self.diagnosticsWidget)
        self.tableNameLabel.setObjectName(u"tableNameLabel")

        self.verticalLayout_6.addWidget(self.tableNameLabel)

        self.tableDescLabel = QLabel(self.diagnosticsWidget)
        self.tableDescLabel.setObjectName(u"tableDescLabel")

        self.verticalLayout_6.addWidget(self.tableDescLabel)

        self.tableDescContentLabel = QLabel(self.diagnosticsWidget)
        self.tableDescContentLabel.setObjectName(u"tableDescContentLabel")

        self.verticalLayout_6.addWidget(self.tableDescContentLabel)

        self.fieldLabel = QLabel(self.diagnosticsWidget)
        self.fieldLabel.setObjectName(u"fieldLabel")

        self.verticalLayout_6.addWidget(self.fieldLabel)

        self.fieldTreeWidget = QTreeWidget(self.diagnosticsWidget)
        QTreeWidgetItem(self.fieldTreeWidget)
        QTreeWidgetItem(self.fieldTreeWidget)
        QTreeWidgetItem(self.fieldTreeWidget)
        self.fieldTreeWidget.setObjectName(u"fieldTreeWidget")
        self.fieldTreeWidget.setColumnCount(3)

        self.verticalLayout_6.addWidget(self.fieldTreeWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.mainSplitter.addWidget(self.diagnosticsWidget)

        self.verticalLayout.addWidget(self.mainSplitter)

        self.consoleWidget = QWidget(self.centralwidget)
        self.consoleWidget.setObjectName(u"consoleWidget")
        self.consoleWidget.setMinimumSize(QSize(0, 100))
        self.consoleWidget.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_7 = QVBoxLayout(self.consoleWidget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.consoleButton = QPushButton(self.consoleWidget)
        self.consoleButton.setObjectName(u"consoleButton")

        self.horizontalLayout_2.addWidget(self.consoleButton)

        self.terminalButton = QPushButton(self.consoleWidget)
        self.terminalButton.setObjectName(u"terminalButton")

        self.horizontalLayout_2.addWidget(self.terminalButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.consoleTextEdit = QTextEdit(self.consoleWidget)
        self.consoleTextEdit.setObjectName(u"consoleTextEdit")
        self.consoleTextEdit.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.consoleTextEdit)


        self.verticalLayout.addWidget(self.consoleWidget)

        self.statusBar = QStatusBar(self.centralwidget)
        self.statusBar.setObjectName(u"statusBar")

        self.verticalLayout.addWidget(self.statusBar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.editorTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pkjviz", None))
        self.newButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.runButton.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.offlineButton.setText(QCoreApplication.translate("MainWindow", u"\u79bb\u7ebf", None))
        self.onlineButton.setText(QCoreApplication.translate("MainWindow", u"\u5728\u7ebf", None))
        self.displayButton.setText(QCoreApplication.translate("MainWindow", u"\u6f14\u793a", None))
        self.packetToolButton.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u5305\u5de5\u5177", None))
        self.envLabel.setText(QCoreApplication.translate("MainWindow", u"\u73af\u5883:", None))
        self.envComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"LT", None))
        self.envComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"NB-Cosim", None))
        self.envComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"NB-SDK", None))

        self.fileExplorerLabel.setText(QCoreApplication.translate("MainWindow", u"\u8d44\u6e90\u7ba1\u7406\u5668", None))
        self.deviceListLabel.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u7528\u8bbe\u5907\u5217\u8868", None))

        __sortingEnabled = self.deviceListView.isSortingEnabled()
        self.deviceListView.setSortingEnabled(False)
        ___qlistwidgetitem = self.deviceListView.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u59071 (192.168.1.1)", None));
        ___qlistwidgetitem1 = self.deviceListView.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u59072 (192.168.1.2)", None));
        ___qlistwidgetitem2 = self.deviceListView.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u59073 (192.168.1.3)", None));
        self.deviceListView.setSortingEnabled(__sortingEnabled)

        self.selectedDeviceLabel.setText("")
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.sendPacketButton.setText(QCoreApplication.translate("MainWindow", u"\u65ad\u5f00", None))
        self.editorTabWidget.setTabText(self.editorTabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"untitled-1.py", None))
        self.editorTabWidget.setTabText(self.editorTabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6587\u4ef61.py", None))
        self.editorTabWidget.setTabText(self.editorTabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u6587\u4ef62.py", None))
        self.editorTabWidget.setTabText(self.editorTabWidget.indexOf(self.registerEditorTab), QCoreApplication.translate("MainWindow", u"\u5bc4\u5b58\u5668\u7f16\u8f91\u5668", None))
        self.dataBrowserLabel.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5305\u6355\u83b7", None))
        self.logLabel.setText(QCoreApplication.translate("MainWindow", u"Log\u7f16\u8f91\u5668", None))
        self.diagnosticsLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bca\u65ad\u7ed3\u679c", None))
        self.codeLabel.setText(QCoreApplication.translate("MainWindow", u"Code:", None))
        self.diagCodeLabel.setText(QCoreApplication.translate("MainWindow", u"DIAG-001", None))
        self.actionLabel.setText(QCoreApplication.translate("MainWindow", u"Action:", None))
        self.diagActionLabel.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u7aef\u53e3\u914d\u7f6e\u5e76\u91cd\u542f\u670d\u52a1", None))
        self.contentLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u5185\u5b58\u8be6\u60c5</p></body></html>", None))
        self.tableLabel.setText(QCoreApplication.translate("MainWindow", u"\u8868\u540d:", None))
        self.tableNameLabel.setText(QCoreApplication.translate("MainWindow", u"ACL_TABLE", None))
        self.tableDescLabel.setText(QCoreApplication.translate("MainWindow", u"\u8868\u63cf\u8ff0:", None))
        self.tableDescContentLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bbf\u95ee\u63a7\u5236\u5217\u8868\u8868\uff0c\u7528\u4e8e\u5b58\u50a8ACL\u89c4\u5219", None))
        self.fieldLabel.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u6bb5\u5217\u8868:", None))
        ___qtreewidgetitem = self.fieldTreeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"\u503c", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u63cf\u8ff0", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));

        __sortingEnabled1 = self.fieldTreeWidget.isSortingEnabled()
        self.fieldTreeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.fieldTreeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"1001", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"ACL\u552f\u4e00\u6807\u8bc6\u7b26", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"acl_id", None));
        ___qtreewidgetitem2 = self.fieldTreeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"100", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"\u89c4\u5219\u4f18\u5148\u7ea7", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"priority", None));
        ___qtreewidgetitem3 = self.fieldTreeWidget.topLevelItem(2)
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"PERMIT", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"\u6267\u884c\u52a8\u4f5c", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"action", None));
        self.fieldTreeWidget.setSortingEnabled(__sortingEnabled1)

        self.consoleButton.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa", None))
        self.terminalButton.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u7aef", None))
        self.consoleTextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">[10:45:32] \u7a0b\u5e8f\u5df2\u542f\u52a8</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">[10:45:33] \u52a0\u8f7d\u6a21\u5757: core.module</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">[10:45:34] \u521d\u59cb\u5316\u5b8c"
                        "\u6210</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">[10:45:36] \u8b66\u544a: \u8bbe\u5907\u672a\u8fde\u63a5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun'; font-size:9pt;\">[10:45:40] \u4fe1\u606f: \u7b49\u5f85\u7528\u6237\u64cd\u4f5c</span></p></body></html>", None))
    # retranslateUi

