# Form implementation generated from reading ui file 'qt/aqt/forms/taglimit.ui'
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
        Dialog.resize(361, 394)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.activeCheck = QtWidgets.QCheckBox(Dialog)
        self.activeCheck.setObjectName("activeCheck")
        self.verticalLayout.addWidget(self.activeCheck)
        self.activeList = QtWidgets.QListWidget(Dialog)
        self.activeList.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.activeList.sizePolicy().hasHeightForWidth())
        self.activeList.setSizePolicy(sizePolicy)
        self.activeList.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.activeList.setObjectName("activeList")
        self.verticalLayout.addWidget(self.activeList)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.inactiveList = QtWidgets.QListWidget(Dialog)
        self.inactiveList.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.inactiveList.sizePolicy().hasHeightForWidth())
        self.inactiveList.setSizePolicy(sizePolicy)
        self.inactiveList.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.inactiveList.setObjectName("inactiveList")
        self.verticalLayout.addWidget(self.inactiveList)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore  # type: ignore
        self.activeCheck.toggled['bool'].connect(self.activeList.setEnabled) # type: ignore  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(tr.custom_study_selective_study())
        self.activeCheck.setText(tr.custom_study_require_one_or_more_of_these())
        self.label.setText(tr.custom_study_select_tags_to_exclude())