# coding=utf-8
import unittest
from PageBase import babyManagePage
from PageBase import loginPage
from appium import webdriver
class babyManageCase(unittest.TestCase):
    def setUp(self):
        print("开始运行")
        if(self.logintest.driver):
            self.logintest.driver.quite()
        # #重新启动Appium
        self.babyMangePage=self.babyMangePage()
        self.logintest.qidongApp()
        #游客模式登录
        self.logintest.login("15088132545","123456")

        self.mbabyManagePage=babyManagePage.babyManagePage()
        #跳转到宝贝管理activity
        self.driver.start_activity('com.person.buddy', "com.person.buddy/.ui.app.MainActivity")
    def tearDown(self):
        print("结束测试用例")

    def testcase0001(self):
        #y游客模式点击宝贝管理按钮
        mbabyManagePage=self.mbabyManagePage
        mbabyManagePage.clickbabyManageBtn()
        #关闭弹框
        mbabyManagePage.clickCloseNoWatch()

    def testcase0002(self):
        self.mbabyManagePage.clicksecurityAreaBtn()
        self.mbabyManagePage.click







