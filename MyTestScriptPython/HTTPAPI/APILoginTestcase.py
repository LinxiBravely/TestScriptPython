# coding=utf-8
from openpyxl import load_workbook
import sys
import  json
reload(sys)
sys.setdefaultencoding('utf8')
from requestConfig import testClass
import  unittest
class testApi(unittest.TestCase):
    def setUp(self):
        self.test=testClass()
        print ("开始")

    def tearDown(self):
        print ("结束")

    def test0000101(self):
        test=self.test
        host=test.readSheetdata('D2')
        path=test.readSheetdata('E2')
        data=test.readSheetdata('F2')
        method=test.readSheetdata('G2')
        url=host+path
        print url
        print data
        print method
        res=test.httpGetOrPost(method,url,data)
        print res
        testCode=res['code']

    def test0000201(self):
        test=self.test
        host=test.readSheetdata('D12')
        path=test.readSheetdata('E12')
        data=test.readSheetdata('F12')
        method=test.readSheetdata('G12')
        url=host+path+test.getAfterUrl()

        res = test.httpGetOrPost(method, url, data)
        print res
        test.assertResponseCode(res['code'],'H12')

if __name__ == "__main__":
    unittest.main()