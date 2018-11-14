# coding=utf-8
import unittest
import time
from Module  import  longinCase
if __name__=="__main__":

    def testmain(self):
        #unittest.main()
        testunit=unittest.TestSuite()
        #将测试用例加入到测试容器中
        testunit.addTest(loginCase("Login"))
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