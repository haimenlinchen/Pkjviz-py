# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'packet_sender.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QTextEdit, QTreeView, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_PacketSenderDialog(object):
    def setupUi(self, PacketSenderDialog):
        if not PacketSenderDialog.objectName():
            PacketSenderDialog.setObjectName(u"PacketSenderDialog")
        PacketSenderDialog.resize(800, 600)
        self.verticalLayout = QVBoxLayout(PacketSenderDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setObjectName(u"toolbarLayout")
        self.addProtocolButton = QPushButton(PacketSenderDialog)
        self.addProtocolButton.setObjectName(u"addProtocolButton")

        self.toolbarLayout.addWidget(self.addProtocolButton)

        self.openButton = QPushButton(PacketSenderDialog)
        self.openButton.setObjectName(u"openButton")

        self.toolbarLayout.addWidget(self.openButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.toolbarLayout.addItem(self.horizontalSpacer)

        self.collapseButton = QPushButton(PacketSenderDialog)
        self.collapseButton.setObjectName(u"collapseButton")

        self.toolbarLayout.addWidget(self.collapseButton)

        self.expandButton = QPushButton(PacketSenderDialog)
        self.expandButton.setObjectName(u"expandButton")

        self.toolbarLayout.addWidget(self.expandButton)


        self.verticalLayout.addLayout(self.toolbarLayout)

        self.mainSplitter = QSplitter(PacketSenderDialog)
        self.mainSplitter.setObjectName(u"mainSplitter")
        self.mainSplitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.mainSplitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.dataPacketLayout = QVBoxLayout(self.layoutWidget)
        self.dataPacketLayout.setObjectName(u"dataPacketLayout")
        self.dataPacketLayout.setContentsMargins(0, 0, 0, 0)
        self.dataPacketLabel = QLabel(self.layoutWidget)
        self.dataPacketLabel.setObjectName(u"dataPacketLabel")

        self.dataPacketLayout.addWidget(self.dataPacketLabel)

        self.dataPacketTreeView = QTreeView(self.layoutWidget)
        self.dataPacketTreeView.setObjectName(u"dataPacketTreeView")

        self.dataPacketLayout.addWidget(self.dataPacketTreeView)

        self.mainSplitter.addWidget(self.layoutWidget)
        self.contentSplitter = QSplitter(self.mainSplitter)
        self.contentSplitter.setObjectName(u"contentSplitter")
        self.contentSplitter.setOrientation(Qt.Vertical)
        self.layoutWidget1 = QWidget(self.contentSplitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.detailLayout = QVBoxLayout(self.layoutWidget1)
        self.detailLayout.setObjectName(u"detailLayout")
        self.detailLayout.setContentsMargins(0, 0, 0, 0)
        self.detailLabel = QLabel(self.layoutWidget1)
        self.detailLabel.setObjectName(u"detailLabel")

        self.detailLayout.addWidget(self.detailLabel)

        self.detailTreeWidget = QTreeWidget(self.layoutWidget1)
        __qtreewidgetitem = QTreeWidgetItem(self.detailTreeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem)
        self.detailTreeWidget.setObjectName(u"detailTreeWidget")

        self.detailLayout.addWidget(self.detailTreeWidget)

        self.contentSplitter.addWidget(self.layoutWidget1)
        self.layoutWidget2 = QWidget(self.contentSplitter)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.hexViewLayout = QVBoxLayout(self.layoutWidget2)
        self.hexViewLayout.setObjectName(u"hexViewLayout")
        self.hexViewLayout.setContentsMargins(0, 0, 0, 0)
        self.hexViewLabel = QLabel(self.layoutWidget2)
        self.hexViewLabel.setObjectName(u"hexViewLabel")

        self.hexViewLayout.addWidget(self.hexViewLabel)

        self.hexViewTextEdit = QTextEdit(self.layoutWidget2)
        self.hexViewTextEdit.setObjectName(u"hexViewTextEdit")
        font = QFont()
        font.setFamilies([u"monospace"])
        self.hexViewTextEdit.setFont(font)

        self.hexViewLayout.addWidget(self.hexViewTextEdit)

        self.contentSplitter.addWidget(self.layoutWidget2)
        self.mainSplitter.addWidget(self.contentSplitter)

        self.verticalLayout.addWidget(self.mainSplitter)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer_2)

        self.cancelButton = QPushButton(PacketSenderDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonLayout.addWidget(self.cancelButton)

        self.sendButton = QPushButton(PacketSenderDialog)
        self.sendButton.setObjectName(u"sendButton")

        self.buttonLayout.addWidget(self.sendButton)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(PacketSenderDialog)

        QMetaObject.connectSlotsByName(PacketSenderDialog)
    # setupUi

    def retranslateUi(self, PacketSenderDialog):
        PacketSenderDialog.setWindowTitle(QCoreApplication.translate("PacketSenderDialog", u"\u53d1\u5305\u5de5\u5177", None))
        self.addProtocolButton.setText(QCoreApplication.translate("PacketSenderDialog", u"\u6dfb\u52a0\u534f\u8bae", None))
        self.openButton.setText(QCoreApplication.translate("PacketSenderDialog", u"\u6253\u5f00", None))
        self.collapseButton.setText(QCoreApplication.translate("PacketSenderDialog", u"\u6298\u53e0", None))
        self.expandButton.setText(QCoreApplication.translate("PacketSenderDialog", u"\u5c55\u5f00", None))
        self.dataPacketLabel.setText(QCoreApplication.translate("PacketSenderDialog", u"\u6570\u636e\u5305", None))
        self.detailLabel.setText(QCoreApplication.translate("PacketSenderDialog", u"\u8be6\u60c5", None))
        ___qtreewidgetitem = self.detailTreeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("PacketSenderDialog", u"\u503c", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("PacketSenderDialog", u"\u5c5e\u6027", None));

        __sortingEnabled = self.detailTreeWidget.isSortingEnabled()
        self.detailTreeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.detailTreeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("PacketSenderDialog", u"Ethernet", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("PacketSenderDialog", u"\u503c0", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("PacketSenderDialog", u"\u6e90MAC\u5730\u5740", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("PacketSenderDialog", u"\u503c1", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("PacketSenderDialog", u"\u5b57\u6bb51", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("PacketSenderDialog", u"\u503c2", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("PacketSenderDialog", u"\u5b57\u6bb52", None));
        self.detailTreeWidget.setSortingEnabled(__sortingEnabled)

        self.hexViewLabel.setText(QCoreApplication.translate("PacketSenderDialog", u"Hex\u89c6\u56fe", None))
        self.hexViewTextEdit.setHtml(QCoreApplication.translate("PacketSenderDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'monospace'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00 11 22 33 44 55 FF FF FF FF FF FF 08</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00 28 00 01 00 00 40 11 7C CD 7F 00 00</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00 01 04 00 04 00 00 14 00 00 00 00 00</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00 00 00 00 00 00 00 00 00 00 00 00 00</p></body></html>", None))
        self.cancelButton.setText(QCoreApplication.translate("PacketSenderDialog", u"\u53d6\u6d88", None))
        self.sendButton.setText(QCoreApplication.translate("PacketSenderDialog", u"\u53d1\u9001", None))
    # retranslateUi

