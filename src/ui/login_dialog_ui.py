# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    Qt,
)
from PySide6.QtGui import (
    QFont,
)
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog: QWidget) -> None:
        if not LoginDialog.objectName():
            LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(400, 200)
        self.verticalLayout = QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QLabel(LoginDialog)
        self.titleLabel.setObjectName("titleLabel")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.deviceLabel = QLabel(LoginDialog)
        self.deviceLabel.setObjectName("deviceLabel")

        self.verticalLayout.addWidget(self.deviceLabel)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.usernameLabel = QLabel(LoginDialog)
        self.usernameLabel.setObjectName("usernameLabel")

        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.usernameEdit = QLineEdit(LoginDialog)
        self.usernameEdit.setObjectName("usernameEdit")

        self.gridLayout.addWidget(self.usernameEdit, 0, 1, 1, 1)

        self.passwordLabel = QLabel(LoginDialog)
        self.passwordLabel.setObjectName("passwordLabel")

        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1)

        self.passwordEdit = QLineEdit(LoginDialog)
        self.passwordEdit.setObjectName("passwordEdit")
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.passwordEdit, 1, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(LoginDialog)
        self.cancelButton.setObjectName("cancelButton")

        self.buttonLayout.addWidget(self.cancelButton)

        self.loginButton = QPushButton(LoginDialog)
        self.loginButton.setObjectName("loginButton")

        self.buttonLayout.addWidget(self.loginButton)

        self.verticalLayout.addLayout(self.buttonLayout)

        self.retranslateUi(LoginDialog)

        self.loginButton.setDefault(True)

        QMetaObject.connectSlotsByName(LoginDialog)

    # setupUi

    def retranslateUi(self, LoginDialog: QWidget) -> None:
        LoginDialog.setWindowTitle(
            QCoreApplication.translate("LoginDialog", "\u767b\u5f55", None)
        )
        self.titleLabel.setText(
            QCoreApplication.translate("LoginDialog", "\u8bbe\u5907\u767b\u5f55", None)
        )
        self.deviceLabel.setText(
            QCoreApplication.translate("LoginDialog", "\u8bbe\u5907\uff1a", None)
        )
        self.usernameLabel.setText(
            QCoreApplication.translate("LoginDialog", "\u7528\u6237\u540d\uff1a", None)
        )
        self.passwordLabel.setText(
            QCoreApplication.translate("LoginDialog", "\u5bc6\u7801\uff1a", None)
        )
        self.cancelButton.setText(
            QCoreApplication.translate("LoginDialog", "\u53d6\u6d88", None)
        )
        self.loginButton.setText(
            QCoreApplication.translate("LoginDialog", "\u767b\u5f55", None)
        )

    # retranslateUi
