# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        if not LoginDialog.objectName():
            LoginDialog.setObjectName(u"LoginDialog")
        LoginDialog.resize(400, 200)
        self.verticalLayout = QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(LoginDialog)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.deviceLabel = QLabel(LoginDialog)
        self.deviceLabel.setObjectName(u"deviceLabel")

        self.verticalLayout.addWidget(self.deviceLabel)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.usernameLabel = QLabel(LoginDialog)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.usernameEdit = QLineEdit(LoginDialog)
        self.usernameEdit.setObjectName(u"usernameEdit")

        self.gridLayout.addWidget(self.usernameEdit, 0, 1, 1, 1)

        self.passwordLabel = QLabel(LoginDialog)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1)

        self.passwordEdit = QLineEdit(LoginDialog)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.passwordEdit, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(LoginDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonLayout.addWidget(self.cancelButton)

        self.loginButton = QPushButton(LoginDialog)
        self.loginButton.setObjectName(u"loginButton")

        self.buttonLayout.addWidget(self.loginButton)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(LoginDialog)

        self.loginButton.setDefault(True)


        QMetaObject.connectSlotsByName(LoginDialog)
    # setupUi

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QCoreApplication.translate("LoginDialog", u"\u767b\u5f55", None))
        self.titleLabel.setText(QCoreApplication.translate("LoginDialog", u"\u8bbe\u5907\u767b\u5f55", None))
        self.deviceLabel.setText(QCoreApplication.translate("LoginDialog", u"\u8bbe\u5907\uff1a", None))
        self.usernameLabel.setText(QCoreApplication.translate("LoginDialog", u"\u7528\u6237\u540d\uff1a", None))
        self.passwordLabel.setText(QCoreApplication.translate("LoginDialog", u"\u5bc6\u7801\uff1a", None))
        self.cancelButton.setText(QCoreApplication.translate("LoginDialog", u"\u53d6\u6d88", None))
        self.loginButton.setText(QCoreApplication.translate("LoginDialog", u"\u767b\u5f55", None))
    # retranslateUi

