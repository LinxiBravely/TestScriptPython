# coding=utf-8
import os
import time
from appium import webdriver
from  selenium.common.exceptions import NoSuchElementException
# {'release': u'4.4.2', 'device': u'samsung', 'brand': u'samsung'}
class basePageReal(object):

    def qidongApp(self):

        PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

        # 设置手机设备信息
        # 初始化
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '4.4.2'  # 设备系统版本
        desired_caps['deviceName'] = 'samsung'  # 设备名称
        # 设置APP信息，进入启动页
        desired_caps['app'] = PATH(r"D:\BaiduNetdiskDownload\buddy21.apk")
        desired_caps['appPackage'] = 'com.bitkinetic.eptool'
        desired_caps['appActivity'] = 'com.bitkinetic.eptool.mvp.SplashActivity'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        time.sleep(5)
        time.sleep(5)
        self.driver.start_activity('com.bitkinetic.eptool', "com.bitkinetic.eptool.mvp.SplashActivity")
        time.sleep(5)





    def by_id(self,the_id):
        return self.driver.find_element_by_id(the_id)
        # print(driver.current_activity())

    def by_className(self,the_className):
        return self.driver.find_element_by_class_name(the_className)
    def by_text(self,the_text):
        return self.driver.find_element_by_name(the_text)



    def guidePage(self, driver):
        if(self.driver.find_element_by_id("com.person.buddy:id/imageview_icon")):
            # 点击引导页1
            self.driver.find_element_by_id("com.person.buddy:id/imageview_icon").click()
            time.sleep(5)
            # 点击引导页2
            driver.find_element_by_id("com.person.buddy:id/imageview_icon").click()
            time.sleep(5)
        else:
            print(driver.current_activity())
#打印当前activity
    def printCurrentAct(self,driver):
        CurrentAct=self.driver.current_activity
        print("当前的Activity为："+CurrentAct)

    def isAppStalled(self):
        if self.driver.is_app_installed("")=="TRUE":
            print("APP当前已被安装")
        else:
            print("APP当前未被安装")
       # print self.driver.is_app_installed("com.person.buddy")


#让APP在后台运行second秒
    def backgroundApp(self,second):
        self.driver.background_app(second)

    # 安装APP,path为APP所在路径
    def installApp(self,path):
        self.driver.install_app(path)

    #卸载APP
    def removeApp(self,appPackageName):
        self.driver.remove_app(appPackageName)

    #启动APP和关闭APP可能会出错
    #启动APP
    def launchAPP(self):
        self.driver.launch_app()
    #关闭APP
    def closeApp(self):
        self.driver.close_app()

    #shake APP
    def shakeAPP(self):
        self.driver.shakeAPP()

    #获取屏幕宽度
    def getWindowsWidth(self):
        #获取屏幕宽度和高度
        size=self.driver.get_window_size()
        #获取宽度
        width=size['width']
        return width

    #获取屏幕高度
    def getWindowsHeigth(self):
        size=self.driver.get_window_size()
        height=size['height']
        return height

  #下面是没有绑定手表的弹框
    #返回绑定手表
    def bindWatch(self):
        try:
            self.by_text("绑定手表")
        except NoSuchElementException :
            print("查找异常")
        else:
            return self.by_text("绑定手表")


    #返回领取定手表
    def notBindWatch(self):
        try:
            self.by_text("领取手表")
        except NoSuchElementException as msg :
            print "异常"%msg
        else:
            return self.by_text("领取手表")

    #返回点击关闭按钮
    def closeNoWatch(self):
        try:
            self.by_id("com.person.buddy:id/iv_close")
        except NoSuchElementException as msg:
            print "异常"%msg
        else:
            return self.by_id("com.person.buddy:id/iv_close")

    #点击绑定手表
    def clickBindWatch(self):
        self.bindWatch().click()
    #点击领取手表
    def clickNotBindWatch(self):
        self.notBindWatch().click()
    #点击关闭
    def clickCloseNoWatch(self):
        self.closeNoWatch().click()

    #返回text值
    def bangdingWatchText(self):
        self.bindWatch().text()



    #游客模式去绑定手表弹框
    #绑定手表按钮
    def toBindBtn(self):
        return self.by_id("com.person.buddy:id/tv_cancel")
    #领取手表按钮
    def toGetWatchBtn(self):
        return self.by_id("com.person.buddy:id/tv_confirm")

    #关闭按钮
    def XXBtn(self):
        return self.by_id("com.person.buddy:id/iv_close")


