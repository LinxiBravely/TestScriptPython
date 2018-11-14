# coding=utf-8
#coding=utf-8      #防止中文乱码


#加载unittest模块
import unittest
import time
import re
#加载HTMLTestRunner，用于生成HTMLreuslt
import HTMLTestRunner

class BaiduYun(unittest.TestCase):
    def setUp(self):
        print("1")
    def Login(self):
        print("2")
    def Register(self):
        print("3")
    def Link(self):
        print("4")
    def tearDown(self):
        print("5")
#if __name__=="__main__":
    def testmain(self):
        #unittest.main()
        testunit=unittest.TestSuite()
        #将测试用例加入到测试容器中
        testunit.addTest(BaiduYun("Login"))
        testunit.addTest(BaiduYun("Register"))
        testunit.addTest(BaiduYun("Link"))
        #获取当前时间，这样便于下面的使用。
        now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
        #打开一个文件，将result写入此file中
        filename = "D:\\testresult.html"
        fp = open(filename, 'w')
        #fp=open("D:\log"+"result"+now+".html",'wb')
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='test result',description=u'result:')
        runner.run(testunit)
        fp.close()