# Form implementation generated from reading ui file 'qt/aqt/forms/clayout_top.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from aqt.utils import tr



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.card_type_label = QtWidgets.QLabel(Form)
        self.card_type_label.setText("CARD TYPE:")
        self.card_type_label.setObjectName("card_type_label")
        self.horizontalLayout.addWidget(self.card_type_label)
        self.templatesBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.templatesBox.sizePolicy().hasHeightForWidth())
        self.templatesBox.setSizePolicy(sizePolicy)
        self.templatesBox.setMaxVisibleItems(30)
        self.templatesBox.setObjectName("templatesBox")
        self.horizontalLayout.addWidget(self.templatesBox)
        spacerItem = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.templateOptions = QtWidgets.QPushButton(Form)
        self.templateOptions.setText("")
        self.templateOptions.setAutoDefault(False)
        self.templateOptions.setDefault(False)
        self.templateOptions.setObjectName("templateOptions")
        self.horizontalLayout.addWidget(self.templateOptions)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(tr.card_templates_form())