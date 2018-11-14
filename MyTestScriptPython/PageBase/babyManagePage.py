# coding=utf-8
# coding=utf-8
import basePageReal
from selenium.common.exceptions import NoSuchElementException
import time
class babyManagePage(basePageReal):
    #返回宝贝管理
    def babyManageBtn(self):
        try:
            time.sleep(5)
            self.by_id("")
            self.by_text("宝贝管理")
        except  NoSuchElementException as  msg:
            print "查找宝贝管理元素异常"%msg
        else:
            return self.by_text("宝贝管理")

    #返回宝贝管理界面元素

    #安全区域
    def securityAreaBtn(self):
        try:
            self.by_text("安全区域")
        except NoSuchElementException as msg:
            print "查找安全区域元素异常"%msg
        else:
            return self.by_text("安全区域")

    def ClickSecurityBtn(self):
        self.securityAreaBtn().click()
    #家庭成员
    def familyBtn(self):
        try:
            self.by_text("家庭成员")
        except NoSuchElementException   as  msg:
            print "查找家庭成员元素异常"%msg
        else:
            return self.by_text("家庭成员")

    #通讯录
    def contactListBtn(self):
        try:
            self.by_text("通讯录")
        except NoSuchElementException   as  msg:
            print "查找通讯录元素异常"%msg
        else:
            return self.by_text("通讯录")

    #手表设置
    def watchSetBtn(self):
        try:
            self.by_text("手表设置")
        except NoSuchElementException   as  msg:
            print "查找手表设置元素异常"%msg
        else:
            return self.by_text("手表设置")

    #上课禁用
    def classNoUseBtn(self):
        try:
            self.by_text("上课禁用")
        except NoSuchElementException   as  msg:
            print "查找上课禁用元素异常"%msg
        else:
            return self.by_text("上课禁用")

    #定位频率
    def positionFreBtn(self):
        try:
            self.by_text("定位频率")
        except NoSuchElementException   as  msg:
            print "查找定位频率元素异常"%msg
        else:
            return self.by_text("定位频率")

    #手表wifi
    def watchWifiBtn(self):
        try:
            self.by_text("手表WiFi")
        except NoSuchElementException   as  msg:
            print "查找手表WiFi元素异常"%msg
        else:
            return self.by_text("手表WiFi")

    #实名认证
    def certificationBtn(self):
        try:
            self.by_text("实名认证")
        except NoSuchElementException   as  msg:
            print "查找实名认证元素异常"%msg
        else:
            return self.by_text("实名认证")


    def clickbabyManageBtn(self):
        self.babyManageBtn().click()

    def clicksecurityAreaBtn(self):
        self.securityAreaBtn().click()



