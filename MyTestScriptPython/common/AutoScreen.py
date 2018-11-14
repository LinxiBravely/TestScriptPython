# coding=utf-8
import os
import time
import xlrd








class AutoScreen(object):
        def screenshotNG(self,caseName, driver, resultPath):
                # resultPath = "d:\\appium"
                logPath = time.strftime('%Y%m%d%H%M%S', time.localtime())
                # screenshotPath = os.path.join(logPath, caseName)
                screenshotName = "CheckPoint_NG.png"
                screen_img = resultPath+caseName+"_"+logPath +"_"+screenshotName
                # screen_img = os.path.join(screenshotPath, screenshotName)
                driver.get_screenshot_as_file(screen_img)
                return screen_img

        def __generateTestCases(self):
                data = xlrd.open_workbook(u".\\login.xls")
                #通过索引顺序获取Excel数据
                table = data.sheets()[0]
                #通过for循环生产多个 test_login_ 函数
                for args in range(1, table.nrows):
                    txt = table.row_values(args)
                    #生成test_login函数后，调用 getTestFunc 进行传参
                    print(txt)

                #__generateTestCases()
