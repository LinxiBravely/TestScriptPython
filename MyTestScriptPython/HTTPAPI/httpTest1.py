# coding=utf-8

import requests
import  unittest
import  json
from openpyxl import load_workbook
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import csv
reload(sys)
sys.setdefaultencoding('utf8')
import sys
print(sys.getdefaultencoding())
class testClass(object):
    def setUp(self):
        print "初始化"
    def tearDown(self):
        print "结束"
    #
    #
    def testLoginPost(self):
        keyword={"phone":"13590404631","zoneNum":"86","password":"123456"}
        data=json.dumps(keyword)
        headers={"Content-Type":"application/json"}
        res=requests.post("https://testdnapp.bitkinetic.com/api/v1/Login/mpLogin",data=data,headers=headers)
        responsejson=res.json()
        print responsejson
        print responsejson['msg']
        # print responsejson["d-tk"]
        print responsejson['data']['team']['sTeamName']

    #封装http POST 函数，返回请求response
    def httpPost(self,keyword,url):
        # data=json.dumps(keyword)
        headers={"Content-Type":"application/json"}
        res=requests.post(url,data=keyword,headers=headers)
        responseJson=res.json()
        return responseJson

    #封装http Get函数，返回response
    def httpGet(self,keyword,url,data):
        headers={"Content-Type":"application/json"}
        res=requests.get(url,data=data,headers=headers)
        responseJson=res.json()
        return responseJson

    # def test001(self):
    #     keyword=self.keyword={"password":"e10adc3949ba59abbe56e057f20f883e","clientSecret":"a123af4e331cf61c0324cd43cbc2135d","accountId":"13590404631"}
    #     url=self.url="http://apptest.buddyniu.com/api/apps/BUDDY_API_TEST/accounts/login"
    #     res=self.httpPost(keyword,url)
    #     print res


    #封装请求函数
    # @staticmethod
    def httpGetOrPost(self,method,url,data):
      #  global mres
        headers = {"Content-Type": "application/json"}
        if method in "get":
            mres=requests.get(url,data=data,headers=headers)
        elif method == "post":
            # postdata = json.dumps(data)
            mres=requests.post(url,data=data,headers=headers)
        elif method in"put":
            mres=requests.put(url,data=data,headers=headers)
        elif method in "delete":
            mres=requests.delete(url,data=data,headers=headers)
        else:
            mres = requests.post(url, data=data, headers=headers)
            print("错误")
       # responseJson=mres.json()
        return mres.json()



    def readSheetdata(self,cell):
        wb=load_workbook(r'd:\apitestcase.xlsx')
        sheet=wb.active
        value=sheet[cell]
        print(value.value)
        return value.value

    # def test002(self):
    #     self.url=self.readSheetdata('C2')
    #     self.data=self.readSheetdata('D2')
    #     self.method=self.readSheetdata('E2')
    #     res=self.httpGetOrPost(self.method,self.url,self.data)
    #     print res



if __name__ == "__main__":
    # unittest.main()
    testClass=testClass()
    testClass.testLoginPost()