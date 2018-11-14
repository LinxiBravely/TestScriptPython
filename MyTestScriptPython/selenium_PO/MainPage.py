# coding=utf-8
'''
Created on 2016-8-13
@author: Jennifer
Project:页面基本操作方法：如open，input_username，input_password，click_submit
'''
from selenium.webdriver.common.by import By
#from test_8_3_2_BasePage import BasePage
from BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
#
# driver.find_element(By.XPATH,'//button[text()="Some Text"]')
# driver.find_elements(By.XPATH,'//button')
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag_name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"
# 继承BasePage类
class MainPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    username_loc = (By.NAME, 'email')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.ID, 'dologin')
    span_loc = (By.CSS_SELECTOR, "div.error-tt>p")
    dynpw_loc = (By.ID, "lbDynPw")
    userid_loc = (By.ID, "spnUid")

    ID_sousuoKuang='kw'
    ID_sousuoBtn='su'

    ClassNameMain='pg-title3'     #主页认证审核断言 “欢迎使用 动能保险助手服务对接平台”
    XpathRealName='//*[@id="app"]/div/div[1]/ul/li[1]/ul/li[1]' #实名认证
    XpathCertifi='//*[@id="app"]/div/div[1]/ul/li[1]/div/span'  #认证审核
    XpathManage='//*[@id="app"]/div/div[1]/ul/li[2]/div/span'#预约管理
    XpathPerManage='//*[@id="app"]/div/div[1]/ul/li[3]'#权限Sub管理
    XpathMyExport='//*[@id="app"]/div/div[1]/ul/li[4]' #我的导出

    IdCer="examine" #认证审核
    Idexamine_real_name='examine_real_name'#实名认证
    Idexamine_profession="examine_profession"  #职业认证
    Idexamine_mdrt="examine_mdrt"#MDRT认证
    Idbespoke='bespoke'#预约管理
    Idbespoke_medical='bespoke_medical'#医疗预约
    Idbespoke_hotel='bespoke_hotel' #酒店预约
    Idbespoke_car='bespoke_car'#专车预约
    Idbespoke_bank='bespoke_bank'#银行开户
    Idauth='auth'#权限管理
    Idaudit='audit'#操作日志

    Idlogout='logout'#退出登录

    ClassButton='el-button'#查看按钮的样式
    ClassButtonLookSuccess="el-button--success"#查看
    ClassButtonrimary='el-button--primary'#审核
    ClassButtonDanger='el-button--danger'#未通过的查看

    ClassNumber='number'


    #点击数字
    def ClickNumber(self):
        # WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        try:
            # WebDriverWait(self.driver, 10).until(EC.visibility_of(self.driver.find_elements_by_class_name(self.ClassNumber)))
            NumberList=self.driver.find_elements_by_class_name(self.ClassNumber)

            if NumberList:
                last=0
                for iNumber in NumberList:
                    last=last+1
                NumberList[1].click()
                NumberList[last].click()
            else:
                print "并没有number"
        except NoSuchElementException as e:
            self.saveScreen()

    #点击按钮
    def ClickClassButtonrimary(self):
        try:
            # WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of(self.driver.find_elements_by_class_name(self.ClassButtonrimary)))

            ButtonRimary=self.driver.find_elements_by_class_name(self.ClassButtonrimary)
            if ButtonRimary:
                ButtonRimary[1].click()
            else:
                    print "ButtonRimary 失败"
        except NoSuchElementException as e:
            self.saveScreen()

    #返回
    def driverBack(self):
        self.driver.back()


    #点击button
    def ClickButton(self):
        try:
            # WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of(self.driver.find_elements_by_class_name(self.ClassButton)))

            ButtonList=self.driver.find_elements_by_class_name(self.ClassButton)
            if ButtonList:
                i=0
                for i in ButtonList:
                    i=i+1;
                t = random.randint(1,i)
                # 随机取一个结果点击鼠标
                ButtonList[t].click()
                return t
            else:
                print "并没有Button"
        except NoSuchElementException as e:
            self.saveScreen()




    def AssertTitle(self,asserttext):
        try:
            self.assertEqual(asserttext,self.driver.title)#
        except AssertionError as e:
            print '找不到这个标题'

    # 点击退出登录
    def clickIdlogout(self):
        try:
            self.driver.find_element_by_id(self.Idlogout).click()
        except NoSuchElementException as e:
            print 'Idlogout'

    # 点击操作日志
    def clickIdaudit(self):
        try:
            self.driver.find_element_by_id(self.Idaudit).click()
        except NoSuchElementException as e:
            print 'Idaudit'

    # 点击权限管理
    def clickIdauth(self):
        try:
            self.driver.find_element_by_id(self.Idauth).click()
        except NoSuchElementException as e:
            print 'Idauth'

    # 点击银行开户预约
    def clickIdbespoke_bank(self):
        try:
            self.driver.find_element_by_id(self.Idbespoke_bank).click()
        except NoSuchElementException as e:
            print 'Idbespoke_bank'

    # 点击专车预约
    def clickIdbespoke_car(self):
        try:
            self.driver.find_element_by_id(self.Idbespoke_car).click()
        except NoSuchElementException as e:
            print 'Idbespoke_car'

    # 点击酒店预约
    def clickIdbespoke_hotel(self):
        try:
            self.driver.find_element_by_id(self.Idbespoke_hotel).click()
        except NoSuchElementException as e:
            print 'Idbespoke_hotel'

    # 点击医疗预约
    def clickIdbespoke_medical(self):
        try:
            self.driver.find_element_by_id(self.Idbespoke_medical).click()
        except NoSuchElementException as e:
            print 'Idbespoke_medical'

    #点击预约管理
    def clickIdbespoke(self):
        try:
            self.driver.find_element_by_id(self.Idbespoke).click()
        except NoSuchElementException as e:
            print 'Idbespoke'

    #点击MDRT认证
    def clickIdexamine_mdrt(self):
        try:
            self.driver.find_element_by_id(self.Idexamine_mdrt).click()
        except NoSuchElementException as e:
            print 'Idexamine_mdrt'

    #点击职业信息认证
    def clickIdexamine_profession(self):
        try:
            self.driver.find_element_by_id(self.Idexamine_profession).click()
        except NoSuchElementException as e:
            print 'Idexamine_profession'


    def clickIdCer(self):
        try:
            print self.IdCer
            #self.Wait(self.IdCer)
            self.driver.find_element_by_id(self.IdCer).click()
        except NoSuchElementException as e:
            print 'IdCer'

    # 点击实名认证
    def clickIdexaminerealname(self):
        try:
            self.driver.find_element_by_id(self.Idexamine_real_name).click()
        except NoSuchElementException as e:
            print 'Idexamine_real_name'


    #封装ByXpath
    def FindElementByXpath(self,value):
        try:
            self.driver.find_element_by_xpath(value)
        except NoSuchElementException as e:
            print 'NoSuchElementException: Message: Unable to locate element'

    #封装 By
    def FindElementBy(self,value):
        try:
            Element=self.driver.find_element(By.XPATH, value)
            return Element
        except NoSuchElementException as e:
            print value
            print 'eee'



    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    #百度搜索框输入selenium
    def input_sousuoKuang(self):
        self.driver.find_element_by_id(self.ID_sousuoKuang).send_keys("Semenium")
    #点击百度按钮
    def click_sousuoBtn(self):
        self.driver.find_element_by_id(self.ID_sousuoBtn).click()

    # 输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        #        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        #        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    # 点击登录：调用send_keys对象，点击登录
    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    # 用户名或密码不合理是Tip框内容展示
    def show_span(self):
        return self.find_element(*self.span_loc).text

    # 切换登录模式为动态密码登录（IE下有效）
    def swich_DynPw(self):
        self.find_element(*self.dynpw_loc).click()

    # 登录成功页面中的用户ID查找
    def show_userid(self):
        return self.find_element(*self.userid_loc).text