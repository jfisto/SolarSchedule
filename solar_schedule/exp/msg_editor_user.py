# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'msg_editor_user.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_EditorEngineerDialog(object):
    def setupUi(self, EditorEngineerDialog):
        if not EditorEngineerDialog.objectName():
            EditorEngineerDialog.setObjectName(u"EditorEngineerDialog")
        EditorEngineerDialog.resize(390, 400)
        EditorEngineerDialog.setMinimumSize(QSize(390, 400))
        self.list_widget = QWidget(EditorEngineerDialog)
        self.list_widget.setObjectName(u"list_widget")
        self.list_widget.setGeometry(QRect(0, 0, 391, 401))
        self.list_widget.setStyleSheet(u"/* Style For QWidget create Engineers */\n"
"\n"
"#list_widget {\n"
"	border: 1px solid #dfdfdf;\n"
"	border-radius: 5px;\n"
"	background-color: #ffffff;\n"
"}\n"
"\n"
"#list_widget QFrame {\n"
"	background-top: 1px solid #dfdfdf;\n"
"}\n"
"\n"
"#list_widget QLineEdit {\n"
"	background-color: #f5f5f5;\n"
"	border: 1px solid #c0c0c0;\n"
"	border-radius: 5px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"#list_widget Qpush {\n"
"	background-color: #f5f5f5;\n"
"	border: 1px solid #c0c0c0;\n"
"	border-radius: 5px;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"#create_engineer {\n"
"	background-color: #f5f5f5;\n"
"	border: 1px solid #c0c0c0;\n"
"	border-bottom-left-radius: 5;\n"
"	padding: 1px;\n"
"}\n"
"\n"
"#delete_engineer {\n"
"	background-color: #f5f5f5;\n"
"	border: 1px solid #c0c0c0;\n"
"	border-bottom-right-radius: 5px;\n"
"	padding: 1px;\n"
"}\n"
"")
        self.frame = QFrame(self.list_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 391, 61))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.surname_engineer = QLineEdit(self.frame)
        self.surname_engineer.setObjectName(u"surname_engineer")
        self.surname_engineer.setGeometry(QRect(20, 20, 351, 21))
        self.frame_2 = QFrame(self.list_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 60, 391, 61))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.name_engineer = QLineEdit(self.frame_2)
        self.name_engineer.setObjectName(u"name_engineer")
        self.name_engineer.setGeometry(QRect(20, 20, 351, 21))
        self.frame_3 = QFrame(self.list_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 120, 391, 61))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.second_name_engineer = QLineEdit(self.frame_3)
        self.second_name_engineer.setObjectName(u"second_name_engineer")
        self.second_name_engineer.setGeometry(QRect(20, 20, 351, 21))
        self.frame_5 = QFrame(self.list_widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 300, 391, 61))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.job_engineer = QLineEdit(self.frame_5)
        self.job_engineer.setObjectName(u"job_engineer")
        self.job_engineer.setGeometry(QRect(20, 20, 351, 21))
        self.create_engineer = QPushButton(self.list_widget)
        self.create_engineer.setObjectName(u"create_engineer")
        self.create_engineer.setGeometry(QRect(0, 360, 196, 41))
        self.delete_engineer = QPushButton(self.list_widget)
        self.delete_engineer.setObjectName(u"delete_engineer")
        self.delete_engineer.setGeometry(QRect(195, 360, 196, 41))
        self.frame_6 = QFrame(self.list_widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 180, 391, 61))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.phone = QLineEdit(self.frame_6)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(20, 20, 351, 21))
        self.frame1 = QFrame(self.list_widget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setGeometry(QRect(0, 240, 391, 61))
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.email_engineer = QLineEdit(self.frame1)
        self.email_engineer.setObjectName(u"email_engineer")
        self.email_engineer.setGeometry(QRect(20, 20, 351, 21))

        self.retranslateUi(EditorEngineerDialog)

        QMetaObject.connectSlotsByName(EditorEngineerDialog)
    # setupUi

    def retranslateUi(self, EditorEngineerDialog):
        EditorEngineerDialog.setWindowTitle(QCoreApplication.translate("EditorEngineerDialog", u"Dialog", None))
        self.surname_engineer.setPlaceholderText(QCoreApplication.translate("EditorEngineerDialog", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.name_engineer.setPlaceholderText(QCoreApplication.translate("EditorEngineerDialog", u"\u0418\u043c\u044f", None))
        self.second_name_engineer.setPlaceholderText(QCoreApplication.translate("EditorEngineerDialog", u"\u041e\u0442\u0447\u0435\u0442\u0441\u0442\u0432\u043e", None))
        self.job_engineer.setPlaceholderText(QCoreApplication.translate("EditorEngineerDialog", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.create_engineer.setText(QCoreApplication.translate("EditorEngineerDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.delete_engineer.setText(QCoreApplication.translate("EditorEngineerDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.phone.setPlaceholderText(QCoreApplication.translate("EditorEngineerDialog", u"Phone", None))
        self.email_engineer.setPlaceholderText(QCoreApplication.translate("EditorEngineerDialog", u"Email", None))
    # retranslateUi

