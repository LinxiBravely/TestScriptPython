# coding=utf-8
import sys
import time
from  selenium.common.exceptions import NoSuchElementException
reload(sys)
sys.setdefaultencoding('utf8')
from basePageReal import basePageReal
class loginPage(basePageReal):


    # 封装username、password、loginButton
    def toLoginActivity(self):

        self.driver.start_activity('com.person.buddy', "com.person.buddy.ui.app.LoginActivity")

    def username(self):
        try:
            time.sleep(5)
            self.by_id('et_userName')
        except NoSuchElementException as msg:
            print "查找异常元素" %msg
        else:
            return self.by_id('et_userName')


    def password(self):
        try:
            time.sleep(5)
            self.by_id('et_password')
        except NoSuchElementException as msg:
            print "查找异常元素" % msg
        else:
            return self.by_id('et_password')

    def login_btn(self):
        return self.by_id('btn_login')
    # 封装清空文本框内容
    def clearUsername(self):
        self.username().clear()

    def clearPassword(self):
        self.password().clear()
    # 封装登录函数
    def login(self,username,password):
        self.username().send_keys(username)
        self.password().send_keys(password)
        self.login_btn().click()



    def visitor(self):
        try:
            time.sleep(5)
            self.by_id("btn_visitor")
        except NoSuchElementException as msg:
            print "查找异常元素" % msg
        else:
            return self.by_id("btn_visitor")

    def clickVisitor(self):
        self.visitor().click()
        self.visitor().click()
        time.sleep(5)

    #用户头像，点击拉出抽屉式个人设置
    def drawee(self):
        drawee=self.by_id("com.person.buddy:id/draweeView")
        return drawee
    #点击用户头像
    def clickDrawee(self):
        self.drawee().click()
        time.sleep(5)
  #设置
    def setting(self):
         setting=self.by_id("com.person.buddy:id/lin_setting")
         return setting

    # 点击抽屉式个人设置的 设置
    def clickSetting(self):
         self.setting().click()
         time.sleep(5)
    #设置界面，退出登录按钮
    def exit(self):
        exit=self.by_id("com.person.buddy:id/btn_exit")
        return  exit
    #设置界面，点击退出登录按钮
    def clickExit(self):
        self.exit().click()
        time.sleep(5)





