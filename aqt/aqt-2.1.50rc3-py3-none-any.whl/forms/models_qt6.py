# Form implementation generated from reading ui file 'qt/aqt/forms/models.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from aqt.utils import tr



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Dialog.resize(396, 255)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.modelsList = QtWidgets.QListWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modelsList.sizePolicy().hasHeightForWidth())
        self.modelsList.setSizePolicy(sizePolicy)
        self.modelsList.setObjectName("modelsList")
        self.gridLayout_2.addWidget(self.modelsList, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Close|QtWidgets.QDialogButtonBox.StandardButton.Help)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout_5.setStretch(0, 100)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(tr.notetypes_note_types())