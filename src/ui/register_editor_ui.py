# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_editor.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_RegisterEditorForm(object):
    def setupUi(self, RegisterEditorForm):
        if not RegisterEditorForm.objectName():
            RegisterEditorForm.setObjectName(u"RegisterEditorForm")
        RegisterEditorForm.resize(800, 600)
        self.verticalLayout = QVBoxLayout(RegisterEditorForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolbarLayout = QHBoxLayout()
        self.toolbarLayout.setObjectName(u"toolbarLayout")
        self.newButton = QPushButton(RegisterEditorForm)
        self.newButton.setObjectName(u"newButton")
        icon = QIcon()
        icon.addFile(u"icons/new.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.newButton.setIcon(icon)

        self.toolbarLayout.addWidget(self.newButton)

        self.openButton = QPushButton(RegisterEditorForm)
        self.openButton.setObjectName(u"openButton")
        icon1 = QIcon()
        icon1.addFile(u"icons/open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.openButton.setIcon(icon1)

        self.toolbarLayout.addWidget(self.openButton)

        self.saveButton = QPushButton(RegisterEditorForm)
        self.saveButton.setObjectName(u"saveButton")
        icon2 = QIcon()
        icon2.addFile(u"icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveButton.setIcon(icon2)

        self.toolbarLayout.addWidget(self.saveButton)

        self.line = QFrame(RegisterEditorForm)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.toolbarLayout.addWidget(self.line)

        self.importButton = QPushButton(RegisterEditorForm)
        self.importButton.setObjectName(u"importButton")

        self.toolbarLayout.addWidget(self.importButton)

        self.exportButton = QPushButton(RegisterEditorForm)
        self.exportButton.setObjectName(u"exportButton")

        self.toolbarLayout.addWidget(self.exportButton)

        self.line_2 = QFrame(RegisterEditorForm)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.toolbarLayout.addWidget(self.line_2)

        self.addButton = QPushButton(RegisterEditorForm)
        self.addButton.setObjectName(u"addButton")

        self.toolbarLayout.addWidget(self.addButton)

        self.deleteButton = QPushButton(RegisterEditorForm)
        self.deleteButton.setObjectName(u"deleteButton")

        self.toolbarLayout.addWidget(self.deleteButton)

        self.resetButton = QPushButton(RegisterEditorForm)
        self.resetButton.setObjectName(u"resetButton")

        self.toolbarLayout.addWidget(self.resetButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.toolbarLayout.addItem(self.horizontalSpacer)

        self.deviceComboBox = QComboBox(RegisterEditorForm)
        self.deviceComboBox.setObjectName(u"deviceComboBox")
        self.deviceComboBox.setMinimumSize(QSize(150, 0))

        self.toolbarLayout.addWidget(self.deviceComboBox)

        self.registerGroupComboBox = QComboBox(RegisterEditorForm)
        self.registerGroupComboBox.setObjectName(u"registerGroupComboBox")
        self.registerGroupComboBox.setMinimumSize(QSize(120, 0))

        self.toolbarLayout.addWidget(self.registerGroupComboBox)


        self.verticalLayout.addLayout(self.toolbarLayout)

        self.filterGroupBox = QGroupBox(RegisterEditorForm)
        self.filterGroupBox.setObjectName(u"filterGroupBox")
        self.horizontalLayout = QHBoxLayout(self.filterGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.filterGroupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.addressFilterEdit = QLineEdit(self.filterGroupBox)
        self.addressFilterEdit.setObjectName(u"addressFilterEdit")

        self.horizontalLayout.addWidget(self.addressFilterEdit)

        self.label_2 = QLabel(self.filterGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.nameFilterEdit = QLineEdit(self.filterGroupBox)
        self.nameFilterEdit.setObjectName(u"nameFilterEdit")

        self.horizontalLayout.addWidget(self.nameFilterEdit)

        self.label_3 = QLabel(self.filterGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.descFilterEdit = QLineEdit(self.filterGroupBox)
        self.descFilterEdit.setObjectName(u"descFilterEdit")

        self.horizontalLayout.addWidget(self.descFilterEdit)

        self.showModifiedCheckBox = QCheckBox(self.filterGroupBox)
        self.showModifiedCheckBox.setObjectName(u"showModifiedCheckBox")

        self.horizontalLayout.addWidget(self.showModifiedCheckBox)


        self.verticalLayout.addWidget(self.filterGroupBox)

        self.registerTableView = QTableView(RegisterEditorForm)
        self.registerTableView.setObjectName(u"registerTableView")
        self.registerTableView.setAlternatingRowColors(True)
        self.registerTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.registerTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.registerTableView.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.registerTableView)

        self.detailsGroupBox = QGroupBox(RegisterEditorForm)
        self.detailsGroupBox.setObjectName(u"detailsGroupBox")
        self.formLayout = QFormLayout(self.detailsGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.addressLabel = QLabel(self.detailsGroupBox)
        self.addressLabel.setObjectName(u"addressLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.addressLabel)

        self.addressEdit = QLineEdit(self.detailsGroupBox)
        self.addressEdit.setObjectName(u"addressEdit")
        self.addressEdit.setReadOnly(False)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.addressEdit)

        self.nameLabel = QLabel(self.detailsGroupBox)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.nameLabel)

        self.nameEdit = QLineEdit(self.detailsGroupBox)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setReadOnly(False)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nameEdit)

        self.valueLabel = QLabel(self.detailsGroupBox)
        self.valueLabel.setObjectName(u"valueLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.valueLabel)

        self.valueLayout = QHBoxLayout()
        self.valueLayout.setObjectName(u"valueLayout")
        self.valueEdit = QLineEdit(self.detailsGroupBox)
        self.valueEdit.setObjectName(u"valueEdit")

        self.valueLayout.addWidget(self.valueEdit)

        self.decValueLabel = QLabel(self.detailsGroupBox)
        self.decValueLabel.setObjectName(u"decValueLabel")

        self.valueLayout.addWidget(self.decValueLabel)

        self.decValue = QLabel(self.detailsGroupBox)
        self.decValue.setObjectName(u"decValue")

        self.valueLayout.addWidget(self.decValue)

        self.binaryValueLabel = QLabel(self.detailsGroupBox)
        self.binaryValueLabel.setObjectName(u"binaryValueLabel")

        self.valueLayout.addWidget(self.binaryValueLabel)

        self.binaryValue = QLabel(self.detailsGroupBox)
        self.binaryValue.setObjectName(u"binaryValue")

        self.valueLayout.addWidget(self.binaryValue)


        self.formLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.valueLayout)

        self.descriptionLabel = QLabel(self.detailsGroupBox)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.descriptionLabel)

        self.descriptionEdit = QLineEdit(self.detailsGroupBox)
        self.descriptionEdit.setObjectName(u"descriptionEdit")
        self.descriptionEdit.setReadOnly(False)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.descriptionEdit)

        self.writableLabel = QLabel(self.detailsGroupBox)
        self.writableLabel.setObjectName(u"writableLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.writableLabel)

        self.writableCheckBox = QCheckBox(self.detailsGroupBox)
        self.writableCheckBox.setObjectName(u"writableCheckBox")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.writableCheckBox)

        self.detailsButtonLayout = QHBoxLayout()
        self.detailsButtonLayout.setObjectName(u"detailsButtonLayout")
        self.applyButton = QPushButton(self.detailsGroupBox)
        self.applyButton.setObjectName(u"applyButton")

        self.detailsButtonLayout.addWidget(self.applyButton)

        self.cancelButton = QPushButton(self.detailsGroupBox)
        self.cancelButton.setObjectName(u"cancelButton")

        self.detailsButtonLayout.addWidget(self.cancelButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.detailsButtonLayout.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(5, QFormLayout.ItemRole.FieldRole, self.detailsButtonLayout)


        self.verticalLayout.addWidget(self.detailsGroupBox)

        self.statusLabel = QLabel(RegisterEditorForm)
        self.statusLabel.setObjectName(u"statusLabel")

        self.verticalLayout.addWidget(self.statusLabel)


        self.retranslateUi(RegisterEditorForm)

        QMetaObject.connectSlotsByName(RegisterEditorForm)
    # setupUi

    def retranslateUi(self, RegisterEditorForm):
        RegisterEditorForm.setWindowTitle(QCoreApplication.translate("RegisterEditorForm", u"\u5bc4\u5b58\u5668\u6570\u636e\u7f16\u8f91\u5668", None))
        self.newButton.setText(QCoreApplication.translate("RegisterEditorForm", u"\u65b0\u5efa", None))
        self.openButton.setText(QCoreApplication.translate("RegisterEditorForm", u"\u6253\u5f00", None))
        self.saveButton.setText(QCoreApplication.translate("RegisterEditorForm", u"\u4fdd\u5b58", None))
        self.importButton.setText(QCoreApplication.translate("RegisterEditorForm", u"\u5bfc\u5165\u8bbe\u5907", None))
        self.exportButton.setText(QCoreApplication.translate("RegisterEditorForm", u"\u5bfc\u51fa\u8bbe\u5907", None))
        self.addButton.setText(QCoreApplication.translate("RegisterEditorForm", u"\u6dfb\u52a0", None))
        self.deleteButton.setText(QCoreApplication.translate("RegisterEditorForm", u"\u5220\u9664", None))
        self.resetButton.setText(QCoreApplication.translate("RegisterEditorForm", u"\u91cd\u7f6e", None))
        self.filterGroupBox.setTitle(QCoreApplication.translate("RegisterEditorForm", u"\u8fc7\u6ee4\u5668", None))
        self.label.setText(QCoreApplication.translate("RegisterEditorForm", u"\u5730\u5740\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("RegisterEditorForm", u"\u540d\u79f0\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("RegisterEditorForm", u"\u63cf\u8ff0\uff1a", None))
        self.showModifiedCheckBox.setText(QCoreApplication.translate("RegisterEditorForm", u"\u4ec5\u663e\u793a\u5df2\u4fee\u6539", None))
        self.detailsGroupBox.setTitle(QCoreApplication.translate("RegisterEditorForm", u"\u8be6\u7ec6\u4fe1\u606f", None))
        self.addressLabel.setText(QCoreApplication.translate("RegisterEditorForm", u"\u5730\u5740\uff1a", None))
        self.nameLabel.setText(QCoreApplication.translate("RegisterEditorForm", u"\u540d\u79f0\uff1a", None))
        self.valueLabel.setText(QCoreApplication.translate("RegisterEditorForm", u"\u503c\uff1a", None))
        self.decValueLabel.setText(QCoreApplication.translate("RegisterEditorForm", u"\u5341\u8fdb\u5236: ", None))
        self.decValue.setText(QCoreApplication.translate("RegisterEditorForm", u"0", None))
        self.binaryValueLabel.setText(QCoreApplication.translate("RegisterEditorForm", u"\u4e8c\u8fdb\u5236: ", None))
        self.binaryValue.setText(QCoreApplication.translate("RegisterEditorForm", u"00000000", None))
        self.descriptionLabel.setText(QCoreApplication.translate("RegisterEditorForm", u"\u63cf\u8ff0\uff1a", None))
        self.writableLabel.setText(QCoreApplication.translate("RegisterEditorForm", u"\u53ef\u5199\uff1a", None))
        self.writableCheckBox.setText("")
        self.applyButton.setText(QCoreApplication.translate("RegisterEditorForm", u"\u5e94\u7528", None))
        self.cancelButton.setText(QCoreApplication.translate("RegisterEditorForm", u"\u53d6\u6d88", None))
        self.statusLabel.setText(QCoreApplication.translate("RegisterEditorForm", u"\u5c31\u7eea", None))
    # retranslateUi

