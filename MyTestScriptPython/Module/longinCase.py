# coding=utf-8

import unittest
import time
import HTMLTestRunner

from PageBase import loginPage

class loginCase(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.logintest=loginPage.loginPage()
        self.logintest.qidongApp()

    def test0001LoginExit(self):
        print("test")
        # 测试登录
        self.logintest.toLoginActivity()
        self.logintest.login("15088132074", "123456")
        # self.logintest.launchAPP()
        self.logintest.clickDrawee()
        self.assertEqual(self.logintest.driver.by_id("com.person.buddy:id/img_scan"),True)
        self.logintest.clickSetting()
        title=self.logintest.driver.by_id("com.person.buddy:id/text_header_title")
        self.assertEqual(title,"设置")
        self.logintest.clickExit()



    def test0001(self):
        #登录失败
        self.logintest.login("15088132074","")

    def test0002(self):
        self.logintest.login("","123456")

    def testtovisitor(self):
        print("test")
        self.logintest.clickVisitor()

    def tearDown(self):
        print("tearDown")


if __name__=='__main__':
        #unittest.main()
        testunit=unittest.TestSuite()
        #将测试用例加入到测试容器中
        testunit.addTest(loginCase("test0001LoginExit"))
        testunit.addTest(loginCase("test0001"))
        testunit.addTest(loginCase("test0002"))
        #获取当前时间，这样便于下面的使用。
        now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
        #打开一个文件，将result写入此file中
        filename = "D:\\testresult.html"
        fp = open(filename, 'w')
        #fp=open("D:\log"+"result"+now+".html",'wb')
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test result',description=u'result:')
        runner.run(testunit)
        fp.close()





