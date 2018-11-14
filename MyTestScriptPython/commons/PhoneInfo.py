# coding=utf-8
# coding=utf-8

import os
import math
import subprocess
import mysql
import sys
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class PhoneInfo(object):
    # 得到手机信息
    def getPhoneRelease(self,devices):
        cmd = "adb -s "+ devices +" shell cat /system/build.prop "
        # phone_info = os.popen(cmd, mode="r").readlines()
        phone_info =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        print phone_info
        l_list = {}
        release = "ro.build.version.release=" # 版本
        model = "ro.product.model=" #型号
        brand = "ro.product.brand=" # 品牌
        device = "ro.product.device=" # 设备名
        for line in phone_info:
             for i in line.split():
                temp = i.decode()
                print(temp)
                if temp.find(release) >= 0:
                    l_list["release"] = temp[len(release):]
                    release=l_list["release"]
                    return release

    def getPhoneModel(self,devices):
        cmd = "adb -s "+ devices +" shell cat /system/build.prop "
        # phone_info = os.popen(cmd, mode="r").readlines()
        phone_info =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        l_list = {}
        model = "ro.product.model=" #型号
        for line in phone_info:
             for i in line.split():
                temp = i.decode()
                print(temp)
                if temp.find(model) >= 0:
                    l_list["model"] = temp[len(model):]
                    model=l_list["model"]
                    return model
    def getPhoneBrand(self,devices):
        cmd = "adb -s "+ devices +" shell cat /system/build.prop "
        # phone_info = os.popen(cmd, mode="r").readlines()
        phone_info =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        l_list = {}
        brand = "ro.product.brand=" # 品牌
        for line in phone_info:
             for i in line.split():
                temp = i.decode()
                print(temp)
                if temp.find(brand) >= 0:
                    l_list["brand"] = temp[len(brand):]
                    brand=l_list["brand"]
                    return brand
    def getPhoneDevice(self,devices):
        cmd = "adb -s "+ devices +" shell cat /system/build.prop "
        # phone_info = os.popen(cmd, mode="r").readlines()
        phone_info =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        l_list = {}
        device = "ro.product.device=" # 设备名
        for line in phone_info:
             for i in line.split():
                temp = i.decode()
                print(temp)
                if temp.find(device) >= 0:
                    l_list["device"] = temp[len(device):]
                    device=l_list["device"]
                    return device

    def get_phone_info(devices):
        cmd = "adb -s "+ devices +" shell cat /system/build.prop "
        # phone_info = os.popen(cmd, mode="r").readlines()
        phone_info =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()

        l_list = {}
        release = "ro.build.version.release=" # 版本
        model = "ro.product.model=" #型号
        brand = "ro.product.brand=" # 品牌
        device = "ro.product.device=" # 设备名

        print(release)
        print(model)
        print(brand)
        print(device)
        for line in phone_info:
             for i in line.split():
                temp = i.decode()
                print(temp)
                if temp.find(release) >= 0:
                    l_list["release"] = temp[len(release):]
                    print(l_list["release"])
                    break
                if temp.find(model) >= 0:
                    l_list["model"] = temp[len(model):]
                    print(l_list["model"])
                    break
                if temp.find(brand) >= 0:
                    l_list["brand"] = temp[len(brand):]
                    print(l_list["brand"])
                    break
                if temp.find(device) >= 0:
                    l_list["device"] = temp[len(device) :]
                    print(l_list["device"])
                    break
        print("-------------设备信息-----------")
        print(l_list)
        return l_list

    # 得到最大运行内存
    def get_men_total(devices):
        cmd = "adb -s "+devices+ " shell cat /proc/meminfo"
        get_cmd = os.popen(cmd).readlines()
        men_total = 0
        men_total_str = "MemTotal"
        for line in get_cmd:
            if line.find(men_total_str) >= 0:
                men_total = line[len(men_total_str) +1:].replace("kB", "").strip()
                break
        print("-------------内存-----------")
        print(men_total)
        return int(men_total)
    # 得到几核cpu
    def get_cpu_kel(devices):
        cmd = "adb -s " +devices +" shell cat /proc/cpuinfo"
        get_cmd = os.popen(cmd).readlines()
        find_str = "processor"
        int_cpu = 0
        for line in get_cmd:
            if line.find(find_str) >= 0:
                int_cpu += 1
        print(str(int_cpu))
        print('-----几核cpu----')
        return str(int_cpu) + "核"

    # 得到手机分辨率
    def get_app_pix(devices):
        result = os.popen("adb -s " + devices+ " shell wm size", "r")
        print("-------------分辨率-----------")
        print(result.readline().split("Physical size:")[1])
        return result.readline().split("Physical size:")[1]
    # get_phone_info("DU2TAN15AJ049163")
    # get_phone_info("MSM8926")

    def get_avg_raw(l_men, devices):

        # :param l_men: 内存使用列表
        # :param devices: 设备名
        # :return:

        l_men = [math.ceil(((l_men[i])/PhoneInfo.get_men_total(devices))*1024) for i in range(len(l_men))]  # 获取每次占用内存多少
        if len(l_men) > 0 :
                print("-------------内存使用-----------")
                print(str(math.ceil(sum(l_men)/len(l_men))) + "%")
                return str(math.ceil(sum(l_men)/len(l_men))) + "%"
        return "0%"

    def get_sql_deviceInfo(self,device):
        release=PhoneInfo.getPhoneRelease(device)
        brand=PhoneInfo.getPhoneBrand(device)
        deviceInfo=PhoneInfo.getPhoneDevice(device)
        model=PhoneInfo.getPhoneModel(device)
        sqlDeviceInfo = release + brand + deviceInfo + model

    def get_screen_size(self):
        size_str = os.popen('adb shell wm size').read()
        if not size_str:
            print('请安装 ADB 及驱动并配置环境变量')
            sys.exit()
        m = re.search(r'(\d+)x(\d+)', size_str)
        return m

    #安装APP
    def installApp(self,path):
        cmd="adb install "+path
        get_cmd=os.popen(cmd).read()

    #删除APP
    def unInstallAPP(self,package):
        cmd="adb unstall"+package
        get_cmd=os.open(cmd).read()

    #清除Logcat缓存
    def clearLocat(self):
        os.popen('adb wait-for-device')
        os.popen('adb logcat -c')


    # 查看单个应用内存占用量
    #
    # # 单个应用的最大内存限制
    #
    # adb
    # shell
    # "getprop|grep heapgrowthlimit"
    #
    # # 应用启动后分配的初始内存
    #
    # adb
    # shell
    # "getprop|grep dalvik.vm.heapstartsize"
    #
    # # 单个java虚拟机的最大内存限制
    #
    # adb
    # shell
    # "getprop|grep dalvik.vm.heapsize"

    if __name__=="__main__":
        #get_phone_info("DU2TAN15AJ049163")
        # device="127.0.0.1:62001"
        # os.system("adb connect "+device)
        device="RUXBB17A27208850   "
        get_phone_info(device)
        get_men_total(device)
        get_cpu_kel(device)
        get_avg_raw(device)



