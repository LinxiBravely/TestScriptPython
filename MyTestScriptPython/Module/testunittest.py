# coding=utf-8
import unittest
import HTMLTestRunner
import threading
import thread
import time
from time import sleep, ctime

class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('111')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('22222')

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次

        print('4444444')

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('33333')

    def test_1_run(self):
        print('test_1_run')
        self.assertEqual(1+1+3,3)


    def test_2_run(self):
        print ('test_2_run')
        self.assertEqual("www", 3)



class thread(object):
    def loop0(self):
        test_suite=unittest.TestCase()
        test_suite.addTest(MyTest('test_1_run'))  # 测试套件中添加测试用例
        return test_suite

    def loop1(self):
        test_suite=unittest.TestCase()
        test_suite.addTest(MyTest('test_2_run'))  # 测试套件中添加测试用例
        return test_suite



    def main(self):

        print "程序开始时间："+ctime()
        t = threading.Thread(target=self.loop0)
        t.start()
        # thread.start_new_thread(self.loop0, ())  # 第二个参数是必不可少的，即使loope没有传递参数，仍然要写一个空元组
        # thread.stant_new_thnead(self.loopl, ())

        filename = 'D:/testresult' +  '.html'
        fp = open(filename, 'w')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
        runner.run(self.loop0)
        fp.close()
        print("-----------------")
        filename1 = 'D:/testresult' + time.strftime('%Y-%m-%d', time.gmtime()) + '.html'
        fp = open(filename1, 'w')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
        runner.run(self.loop1)
        fp.close()
        print("-----------------")
        sleep(6)  # 这里休眠6秒的原因是确保两个线程己经执行完毕，主线程才接着执行下面的语句
        print "程序结束时间：", ctime()



#
#
# if __name__=='__main__':
#     mthred=thread()
#     mthred.main()

if __name__=='__main__':
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(MyTest))
    filename1 = 'D:/testresult' + time.strftime('%Y-%m-%d', time.gmtime()) + '.html'
    fp = open(filename1, 'w')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
    runner.run(suit)
    fp.close()

# if __name__ == '__main__':
#     test_suite = unittest.TestSuite()  # 创建一个测试集合
#     # test_suite.addTest(MyTest('test_a_run'))  # 测试套件中添加测试用例
#     # test_suite.addTest(MyTest('test_b_run'))
#
#     test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
#     filename = "D:\\testresult.html"
#     fp = open(filename, 'w')
#     # fp=open("D:\log"+"result"+now+".html",'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
#     runner.run(test_suite)
#     fp.close()
#     # fp = open('res.html', 'wb')  # 打开一个保存结果的html文件
#     # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='api测试报告', description='测试情况')
#     # # 生成执行用例的对象
#     # runner.run(test_suite)
#     # # 执行测试套件