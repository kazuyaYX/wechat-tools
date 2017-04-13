# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!
import sys
from itchat.content import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from wechat_tools import WechatTools


class Ui_MainWindow(object):
    wechat = WechatTools()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(479, 500)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 481, 501))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lW_friends_list = QtWidgets.QListWidget(self.tab)
        self.lW_friends_list.setEnabled(True)
        self.lW_friends_list.setGeometry(QtCore.QRect(40, 70, 171, 192))
        self.lW_friends_list.setObjectName("lW_friends_list")
        item = QtWidgets.QListWidgetItem()
        self.lW_friends_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lW_friends_list.addItem(item)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(260, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lW_mass_list = QtWidgets.QListWidget(self.tab)
        self.lW_mass_list.setGeometry(QtCore.QRect(260, 70, 171, 192))
        self.lW_mass_list.setObjectName("lW_mass_list")
        item = QtWidgets.QListWidgetItem()
        self.lW_mass_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lW_mass_list.addItem(item)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(40, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tE_msg = QtWidgets.QTextEdit(self.tab)
        self.tE_msg.setGeometry(QtCore.QRect(40, 300, 391, 91))
        self.tE_msg.setObjectName("tE_msg")
        self.pB_mass_msg = QtWidgets.QPushButton(self.tab)
        self.pB_mass_msg.setGeometry(QtCore.QRect(190, 410, 91, 31))
        self.pB_mass_msg.setObjectName("pB_mass_msg")
        self.pB_add_friends = QtWidgets.QPushButton(self.tab)
        self.pB_add_friends.setGeometry(QtCore.QRect(220, 130, 31, 31))
        self.pB_add_friends.setObjectName("pB_add_friends")
        self.pB_reduce_friends = QtWidgets.QPushButton(self.tab)
        self.pB_reduce_friends.setGeometry(QtCore.QRect(220, 170, 31, 31))
        self.pB_reduce_friends.setObjectName("pB_reduce_friends")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(100, 160, 111, 41))
        self.label_9.setObjectName("label_9")
        self.tE_remind_time = QtWidgets.QTimeEdit(self.tab_2)
        self.tE_remind_time.setGeometry(QtCore.QRect(220, 170, 118, 22))
        self.tE_remind_time.setObjectName("tE_remind_time")
        self.pB_set_remind_time = QtWidgets.QPushButton(self.tab_2)
        self.pB_set_remind_time.setGeometry(QtCore.QRect(170, 230, 81, 31))
        self.pB_set_remind_time.setObjectName("pB_set_remind_time")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pB_set_withdraw_settings = QtWidgets.QPushButton(self.tab_3)
        self.pB_set_withdraw_settings.setGeometry(QtCore.QRect(190, 370, 81, 31))
        self.pB_set_withdraw_settings.setObjectName("pB_set_withdraw_settings")
        self.cB_friend_text = QtWidgets.QCheckBox(self.tab_3)
        self.cB_friend_text.setGeometry(QtCore.QRect(80, 140, 91, 21))
        self.cB_friend_text.setObjectName("cB_friend_text")
        self.cB_friend_voice = QtWidgets.QCheckBox(self.tab_3)
        self.cB_friend_voice.setGeometry(QtCore.QRect(80, 170, 91, 21))
        self.cB_friend_voice.setObjectName("cB_friend_voice")
        self.cB_friend_img = QtWidgets.QCheckBox(self.tab_3)
        self.cB_friend_img.setGeometry(QtCore.QRect(80, 200, 91, 21))
        self.cB_friend_img.setObjectName("cB_friend_img")
        self.cB_friend_video = QtWidgets.QCheckBox(self.tab_3)
        self.cB_friend_video.setGeometry(QtCore.QRect(80, 230, 91, 21))
        self.cB_friend_video.setObjectName("cB_friend_video")
        self.cB_friend_sharing = QtWidgets.QCheckBox(self.tab_3)
        self.cB_friend_sharing.setGeometry(QtCore.QRect(80, 260, 91, 21))
        self.cB_friend_sharing.setObjectName("cB_friend_sharing")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(50, 110, 151, 221))
        self.groupBox.setObjectName("groupBox")
        self.cB_friend_file = QtWidgets.QCheckBox(self.groupBox)
        self.cB_friend_file.setGeometry(QtCore.QRect(30, 180, 91, 21))
        self.cB_friend_file.setObjectName("cB_friend_file")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 110, 151, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.cB_group_file = QtWidgets.QCheckBox(self.groupBox_2)
        self.cB_group_file.setGeometry(QtCore.QRect(30, 180, 91, 21))
        self.cB_group_file.setObjectName("cB_group_file")
        self.cB_group_sharing = QtWidgets.QCheckBox(self.groupBox_2)
        self.cB_group_sharing.setGeometry(QtCore.QRect(30, 150, 91, 21))
        self.cB_group_sharing.setObjectName("cB_group_sharing")
        self.cB_group_text = QtWidgets.QCheckBox(self.groupBox_2)
        self.cB_group_text.setGeometry(QtCore.QRect(30, 30, 91, 21))
        self.cB_group_text.setObjectName("cB_group_text")
        self.cB_group_video = QtWidgets.QCheckBox(self.groupBox_2)
        self.cB_group_video.setGeometry(QtCore.QRect(30, 120, 91, 21))
        self.cB_group_video.setObjectName("cB_group_video")
        self.cB_group_voice = QtWidgets.QCheckBox(self.groupBox_2)
        self.cB_group_voice.setGeometry(QtCore.QRect(30, 60, 91, 21))
        self.cB_group_voice.setObjectName("cB_group_voice")
        self.cB_group_img = QtWidgets.QCheckBox(self.groupBox_2)
        self.cB_group_img.setGeometry(QtCore.QRect(30, 90, 91, 21))
        self.cB_group_img.setObjectName("cB_group_img")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(40, 20, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.pB_set_withdraw_settings.raise_()
        self.cB_friend_text.raise_()
        self.cB_friend_voice.raise_()
        self.cB_friend_img.raise_()
        self.cB_friend_video.raise_()
        self.cB_friend_sharing.raise_()
        self.label_10.raise_()
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.pB_set_remind_time.clicked.connect(self.set_remind_time)
        self.pB_mass_msg.clicked.connect(self.mass_msg)
        self.pB_add_friends.clicked.connect(self.add_friends)
        self.pB_reduce_friends.clicked.connect(self.reduce_friends)
        self.pB_set_withdraw_settings.clicked.connect(self.set_withdraw_setting)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        title = self.wechat.start()
        MainWindow.setWindowTitle(_translate("MainWindow", '微信小工具（当前微信号：' + title + '）'))
        __sortingEnabled = self.lW_friends_list.isSortingEnabled()
        self.lW_friends_list.setSortingEnabled(False)
        item = self.lW_friends_list.item(0)
        item.setText(_translate("MainWindow", "kazuya"))
        item = self.lW_friends_list.item(1)
        item.setText(_translate("MainWindow", "victorique"))
        self.lW_friends_list.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "好友名单："))
        self.label_2.setText(_translate("MainWindow", "群发对象："))
        __sortingEnabled = self.lW_mass_list.isSortingEnabled()
        self.lW_mass_list.setSortingEnabled(False)
        item = self.lW_mass_list.item(0)
        item.setText(_translate("MainWindow", "kazuya"))
        item = self.lW_mass_list.item(1)
        item.setText(_translate("MainWindow", "victorique"))
        self.lW_mass_list.setSortingEnabled(__sortingEnabled)
        # 设置好友列表
        self.set_friend_list(self.wechat.get_friend_list())
        self.label_5.setText(_translate("MainWindow", "群发内容："))
        self.pB_mass_msg.setText(_translate("MainWindow", "发送"))
        self.pB_add_friends.setText(_translate("MainWindow", "+"))
        self.pB_reduce_friends.setText(_translate("MainWindow", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "群发助手"))
        self.label_9.setText(_translate("MainWindow", "每日提醒时间："))
        self.pB_set_remind_time.setText(_translate("MainWindow", "确定"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "签到提醒"))
        self.pB_set_withdraw_settings.setText(_translate("MainWindow", "确定"))
        self.cB_friend_text.setText(_translate("MainWindow", "文字"))
        self.cB_friend_voice.setText(_translate("MainWindow", "语音"))
        self.cB_friend_img.setText(_translate("MainWindow", "图片"))
        self.cB_friend_video.setText(_translate("MainWindow", "视频"))
        self.cB_friend_sharing.setText(_translate("MainWindow", "分享"))
        self.groupBox.setTitle(_translate("MainWindow", "好友消息"))
        self.cB_friend_file.setText(_translate("MainWindow", "文件"))
        self.groupBox_2.setTitle(_translate("MainWindow", "群消息"))
        self.cB_group_file.setText(_translate("MainWindow", "文件"))
        self.cB_group_sharing.setText(_translate("MainWindow", "分享"))
        self.cB_group_text.setText(_translate("MainWindow", "文字"))
        self.cB_group_video.setText(_translate("MainWindow", "视频"))
        self.cB_group_voice.setText(_translate("MainWindow", "语音"))
        self.cB_group_img.setText(_translate("MainWindow", "图片"))
        self.label_10.setText(_translate("MainWindow", "撤回的文字信息会发到自己的微信上，其他文件信息会保存到\n本程序目录下的"
                                                       "withdraw文件夹中并发消息到自己微信上提醒"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "防撤回"))

    def mass_msg(self):
        if self.lW_mass_list.count() == 0:
            QMessageBox.information(self.centralWidget, '提示', '请选择要群发的对象')
            return
        if self.tE_msg.toPlainText() == '':
            QMessageBox.information(self.centralWidget, '提示', '请输入要群发的内容')
            return
        mass_list = []
        for i in range(self.lW_mass_list.count()):
            print(self.lW_mass_list.item(i).text())
            mass_list.append(self.lW_mass_list.item(i).text())
        WechatTools.mass_msg(self.tE_msg.toPlainText(), mass_list)
        QMessageBox.information(self.centralWidget, '提示', '发送成功')

    def set_remind_time(self):
        self.wechat.set_sign_time(self.tE_remind_time.text())
        QMessageBox.information(self.centralWidget, '提示', '设置成功')

    def set_withdraw_setting(self):
        withdraw_friend_setting = []
        withdraw_group_setting = []
        if self.cB_friend_file.isChecked():
            withdraw_friend_setting.append(ATTACHMENT)
        if self.cB_friend_img.isChecked():
            withdraw_friend_setting.append(PICTURE)
        if self.cB_friend_sharing.isChecked():
            withdraw_friend_setting.append(SHARING)
        if self.cB_friend_text.isChecked():
            withdraw_friend_setting.append(TEXT)
        if self.cB_friend_video.isChecked():
            withdraw_friend_setting.append(VIDEO)
        if self.cB_friend_voice.isChecked():
            withdraw_friend_setting.append(RECORDING)

        if self.cB_group_file.isChecked():
            withdraw_group_setting.append(ATTACHMENT)
        if self.cB_group_img.isChecked():
            withdraw_group_setting.append(PICTURE)
        if self.cB_group_sharing.isChecked():
            withdraw_group_setting.append(SHARING)
        if self.cB_group_text.isChecked():
            withdraw_group_setting.append(TEXT)
        if self.cB_group_video.isChecked():
            withdraw_group_setting.append(VIDEO)
        if self.cB_group_voice.isChecked():
            withdraw_group_setting.append(RECORDING)

        print(withdraw_friend_setting)
        print(withdraw_group_setting)
        self.wechat.set_withdraw_setting(withdraw_friend_setting, withdraw_group_setting)
        QMessageBox.information(self.centralWidget, '提示', '设置成功')

    def add_friends(self):
        if self.lW_friends_list.currentItem() is None:
            return
        item = self.lW_friends_list.takeItem(self.lW_friends_list.currentRow())
        self.lW_mass_list.addItem(item.text())
        item = None

    def reduce_friends(self):
        if self.lW_mass_list.currentItem() is None:
            return
        item = self.lW_mass_list.takeItem(self.lW_mass_list.currentRow())
        self.lW_friends_list.addItem(item.text())
        self.lW_friends_list.sortItems()
        item = None

    # 设置好友列表的方法
    def set_friend_list(self, friends_list):
        self.lW_friends_list.clear()
        self.lW_mass_list.clear()
        for friend in friends_list:
            self.lW_friends_list.addItem(friend)
        self.lW_friends_list.sortItems()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

