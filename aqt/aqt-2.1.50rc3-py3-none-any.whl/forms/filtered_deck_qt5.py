# Form implementation generated from reading ui file 'qt/aqt/forms/filtered_deck.ui'
#
# Created by: PyQt5 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from aqt.utils import tr



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(757, 589)
        Dialog.setWindowTitle("Dialog")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.groupBox_3)
        self.name.setText("")
        self.name.setPlaceholderText("")
        self.name.setObjectName("name")
        self.gridLayout_4.addWidget(self.name, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.search_button = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy)
        self.search_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.search_button.setAutoDefault(False)
        self.search_button.setFlat(True)
        self.search_button.setProperty("label", "search")
        self.search_button.setObjectName("search_button")
        self.gridLayout.addWidget(self.search_button, 1, 0, 1, 1)
        self.search = QtWidgets.QLineEdit(self.groupBox)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 1, 2, 1, 4)
        self.limit = QtWidgets.QSpinBox(self.groupBox)
        self.limit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.limit.setMinimum(1)
        self.limit.setMaximum(99999)
        self.limit.setObjectName("limit")
        self.gridLayout.addWidget(self.limit, 2, 2, 1, 1)
        self.order = QtWidgets.QComboBox(self.groupBox)
        self.order.setObjectName("order")
        self.gridLayout.addWidget(self.order, 2, 4, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.filter2group = QtWidgets.QGroupBox(Dialog)
        self.filter2group.setObjectName("filter2group")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.filter2group)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.search_2 = QtWidgets.QLineEdit(self.filter2group)
        self.search_2.setObjectName("search_2")
        self.gridLayout_3.addWidget(self.search_2, 0, 1, 1, 4)
        self.search_button_2 = QtWidgets.QPushButton(self.filter2group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_button_2.sizePolicy().hasHeightForWidth())
        self.search_button_2.setSizePolicy(sizePolicy)
        self.search_button_2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.search_button_2.setAutoDefault(False)
        self.search_button_2.setFlat(True)
        self.search_button_2.setProperty("label", "search")
        self.search_button_2.setObjectName("search_button_2")
        self.gridLayout_3.addWidget(self.search_button_2, 0, 0, 1, 1)
        self.order_2 = QtWidgets.QComboBox(self.filter2group)
        self.order_2.setObjectName("order_2")
        self.gridLayout_3.addWidget(self.order_2, 1, 3, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.filter2group)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.limit_2 = QtWidgets.QSpinBox(self.filter2group)
        self.limit_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.limit_2.setMinimum(1)
        self.limit_2.setMaximum(99999)
        self.limit_2.setObjectName("limit_2")
        self.gridLayout_3.addWidget(self.limit_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.filter2group)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.filter2group)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.resched = QtWidgets.QCheckBox(self.groupBox_2)
        self.resched.setChecked(True)
        self.resched.setObjectName("resched")
        self.gridLayout_2.addWidget(self.resched, 0, 0, 1, 2)
        self.secondFilter = QtWidgets.QCheckBox(self.groupBox_2)
        self.secondFilter.setObjectName("secondFilter")
        self.gridLayout_2.addWidget(self.secondFilter, 2, 0, 1, 1)
        self.previewDelayWidget = QtWidgets.QWidget(self.groupBox_2)
        self.previewDelayWidget.setObjectName("previewDelayWidget")
        self.previewDelayBox = QtWidgets.QHBoxLayout(self.previewDelayWidget)
        self.previewDelayBox.setObjectName("previewDelayBox")
        self.label_7 = QtWidgets.QLabel(self.previewDelayWidget)
        self.label_7.setObjectName("label_7")
        self.previewDelayBox.addWidget(self.label_7)
        self.previewDelay = QtWidgets.QSpinBox(self.previewDelayWidget)
        self.previewDelay.setObjectName("previewDelay")
        self.previewDelayBox.addWidget(self.previewDelay)
        self.label_8 = QtWidgets.QLabel(self.previewDelayWidget)
        self.label_8.setObjectName("label_8")
        self.previewDelayBox.addWidget(self.label_8)
        self.gridLayout_2.addWidget(self.previewDelayWidget, 1, 0, 1, 1)
        self.steps = QtWidgets.QLineEdit(self.groupBox_2)
        self.steps.setEnabled(False)
        self.steps.setText("1 10")
        self.steps.setObjectName("steps")
        self.gridLayout_2.addWidget(self.steps, 4, 0, 1, 1)
        self.stepsOn = QtWidgets.QCheckBox(self.groupBox_2)
        self.stepsOn.setObjectName("stepsOn")
        self.gridLayout_2.addWidget(self.stepsOn, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.hint_button = QtWidgets.QPushButton(Dialog)
        self.hint_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.hint_button.setAutoDefault(False)
        self.hint_button.setFlat(True)
        self.hint_button.setProperty("label", "hint")
        self.hint_button.setObjectName("hint_button")
        self.horizontalLayout.addWidget(self.hint_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Help|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore  # type: ignore
        self.secondFilter.toggled['bool'].connect(self.filter2group.setVisible) # type: ignore  # type: ignore
        self.stepsOn.toggled['bool'].connect(self.steps.setEnabled) # type: ignore  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.name, self.search_button)
        Dialog.setTabOrder(self.search_button, self.search)
        Dialog.setTabOrder(self.search, self.limit)
        Dialog.setTabOrder(self.limit, self.order)
        Dialog.setTabOrder(self.order, self.search_button_2)
        Dialog.setTabOrder(self.search_button_2, self.search_2)
        Dialog.setTabOrder(self.search_2, self.limit_2)
        Dialog.setTabOrder(self.limit_2, self.order_2)
        Dialog.setTabOrder(self.order_2, self.resched)
        Dialog.setTabOrder(self.resched, self.previewDelay)
        Dialog.setTabOrder(self.previewDelay, self.secondFilter)
        Dialog.setTabOrder(self.secondFilter, self.stepsOn)
        Dialog.setTabOrder(self.stepsOn, self.steps)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox_3.setTitle(tr.decks_deck())
        self.label_2.setText(tr.actions_name())
        self.groupBox.setTitle(tr.actions_filter())
        self.search_button.setToolTip(tr.search_view_in_browser())
        self.search_button.setText(tr.actions_search())
        self.label.setText(tr.decks_cards_selected_by())
        self.label_5.setText(tr.decks_limit_to())
        self.filter2group.setTitle(tr.decks_filter_2())
        self.search_button_2.setToolTip(tr.search_view_in_browser())
        self.search_button_2.setText(tr.actions_search())
        self.label_6.setText(tr.decks_limit_to())
        self.label_4.setText(tr.decks_cards_selected_by())
        self.groupBox_2.setTitle(tr.actions_options())
        self.resched.setText(tr.decks_reschedule_cards_based_on_my_answers())
        self.secondFilter.setText(tr.decks_enable_second_filter())
        self.label_7.setText(tr.decks_repeat_failed_cards_after())
        self.label_8.setText(tr.decks_minutes())
        self.stepsOn.setText(tr.decks_custom_steps_in_minutes())
        self.hint_button.setToolTip(tr.search_view_in_browser())
        self.hint_button.setText(tr.decks_unmovable_cards())