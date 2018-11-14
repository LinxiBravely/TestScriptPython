# coding=utf-8
'''
Created on 2016-8-13
@author: Jennifer
Project:使用unittest框架编写测试用例。
'''
import unittest
import  sys
from MainPage import MainPage
from selenium import webdriver
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class testCase(unittest.TestCase):
    """
          登录126邮箱的case
    """
    #所有test运行前执行
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = "https://apiadmin.bitkinetic.com/auto?wx=ZhangLiYe"
        self.urlDenglu = "https://admin.bitkinetic.com/"
        self.a_page = MainPage(self.driver, self.url, u"baidu")

    @classmethod
    def  tearDownClass(self):
        self.driver.quit()
        self.driver.close()
    def setUp(self):
        print("begin")


    #认证审核
    def test0001(self):
        self.a_page.myOpen(self.url)
        self.a_page.myOpen(self.urlDenglu)
        #点击认证审核
        self.a_page.clickIdCer()

        #实名认证
        self.a_page.clickIdexaminerealname()
        # self.a_page.AssertTitle("实名认证")
        self.a_page.ClickNumber()
        self.a_page.ClassButton()


        #职业信息认证
        self.a_page.clickIdexamine_profession()
        #MdRT 认证
        self.a_page.clickIdexamine_mdrt()

        self.driver.quit()

    def test0002(self):
        self.a_page.myOpen(self.url)
        self.a_page.myOpen(self.urlDenglu)

        self.a_page.clickIdbespoke()
        self.a_page.clickIdbespoke_medical()
        # self.a_page.AssertTitle("医疗预约")
        self.a_page.clickIdbespoke_hotel()
        # self.a_page.AssertTitle("酒店预约")
        self.a_page.clickIdbespoke_car()
        # self.a_page.AssertTitle("专车预约")
        self.a_page.clickIdbespoke_bank()
        # self.a_page.AssertTitle("银行预约")

        self.driver.quit()

    def test0003(self):
        self.a_page.myOpen(self.url)
        self.a_page.myOpen(self.urlDenglu)

        self.a_page.clickIdauth()
        # self.a_page.AssertTitle("权限管理")
        self.driver.quit()

    def test0004(self):
        self.a_page.myOpen(self.url)
        self.a_page.myOpen(self.urlDenglu)
        self.a_page.clickIdlogout()
        # self.a_page.AssertTitle()


        # self.driver.find_element_by_xpath(a_page.mXpathCerti)
        # 用例执行体
    # def test_login_mail(self):
    #     # 声明LoginPage类对象

    #     login_page = MainPage(self.driver, self.url, u"网易")
    #     # 调用打开页面组件
    #     login_page.open()
    #     # 切换到登录框Frame
    #     login_page.switch_frame('x-URS-iframe')
    #     # 调用用户名输入组件
    #     login_page.input_username(self.username)
    #     # 调用密码输入组件
    #     login_page.input_password(self.password)
    #     # 调用点击登录按钮组件
    #     login_page.click_submit()

    def tearDown(self):
        print("close")





def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(testCase("test0001"))
    return suiteTest






if __name__ == "__main__":
    print '--------------'
    filepath = 'D:\\pyresult.html'
    fp = file(filepath, 'wb')
    print "suceess"
    # 定义测试报告的标题与描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'我是测试报告的标题')
    runner.run(suite())
    fp.close()