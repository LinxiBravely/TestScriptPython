# coding=utf-8
# -*- coding: utf-8 -*-
import subprocess
import re, os


import time
# 常用的性能监控
#看到这，也就能明白，top跟dump cpuinfo的区别在于：top分母有的是总测CPU jiffies，而dump cpuinfo是uptime，是时间，而并非jiffies，也能解释为什么top出来的cpu，大部分时间会比dump cpuinfo的原因。
#查看cpu使用情况

#冷启动：首次打开应用时间
#热启动 ：程序被杀死后重新启动的时间
class appPerformance:
    #单个应用的最大内存限制
    def heapgrowthlimit(self):
        cmd='adb shell "getprop | grep heapgrowthlimit"'
        get_cmd=os.system(cmd)
        return get_cmd

    #应用启动后分配的初始内存
    def heapstartsize(self):
        cmd='adb shell "getprop|grep dalvik.vm.heapstartsize"'
        get_cmd=os.system(cmd)
        return get_cmd
    #单个java虚拟机的最大内存限制
    def heapstartsize(self):
        cmd='adb shell "getprop|grep dalvik.vm.heapsize"'
        get_cmd=os.system(cmd)
        return get_cmd

    def monkey(self,device):
        #清理日志
        #可加忽略崩溃异常
        #可加忽略ANR
# adb shell monkey -p com.bitkinetic.eptool  -s 5000 -v -v  -v  40000 -throttle 5000
#         adb shell monkey - p
#         com.mvp - -pct - touch
#        –ignore - timeouts - -throttle
#         800 - v
#         10000
        cmd_clear='adb logcat -c'
        get_cmd_clear = os.system(cmd_clear)
        cmd='adb  -s '+device+' shell monkey -p com.bitkinetic.eptool  -s 3000 -v -v  -v  400000 -throttle 500 '
        get_cmd=os.system(cmd)
        print(cmd)
        #将手机的日志打印到test.log
        cmd_log='adb shell "logcat|grep eptool">D:/bitkinetic.txt'
        get_cmd_log=os.system(cmd_log)
        return get_cmd_log




    # 两种方法直接区别在于，top是持续监控状态，而dumpsys
    # cpuinfo获取的实时CPU占用率数据
    def dumps_cpu(self,device):
        cmd='adb -s' +device+'shell "dumpsys cpuinfo|grep -w com.bitkinetic.eptool" '
        get_cmd=os.popen(cmd).readline()
        for info in get_cmd:
            dumpsTop=float(info.split()[2].split("%")[0])
            return dumpsTop


    def top_cpu(self,device):
        cmd='adb -s '+device+' shell "top cpuinfo|grep -w com.bitkinetic.eptool">D:cpu.txt'
        #cmd = "adb -s "+devices+" shell dumpsys cpuinfo | grep -w " + pkg_name+":"
        get_cmd = os.popen(cmd).readlines()
        for info in get_cmd:
            print("top_cpu结果为：")
            print (float(info.split()[2].split("%")[0]))
            cpuTop=float(info.split()[2].split("%")[0])
            # return float(info.split()[2].split("%")[0])
            return cpuTop



    # 得到men的使用情况
    #查看系统内存情况
    def get_men(self,device):
        cmd='adb -s'+device+' shell "dumpsys meminfo com.bitkinetic.eptool">D:men.txt'
        #cmd = "adb -s "+devices+" shell  dumpsys  meminfo %s"  %(pkg_name)
        total = "TOTAL"
        get_cmd = os.popen(cmd).readlines()
        for info in get_cmd:
            info_sp = info.strip().split()
            for item in range(len(info_sp)):
                if info_sp[item] == total:
                   print("get_men结果是：")
                   men=int(info_sp[item+1])
                   print (int(info_sp[item+1]))
                   # return int(info_sp[item+1])
                   return men
        return 0


    #获取该APP的帧率，然后写入到D:fps.txt文件中
    # 帧率值在什么范围可认定为流畅？
    # # 理想状态每秒展示60帧时人眼感受不到卡顿，1000ms/60帧，即每帧绘制时间不应超过16.67ms。
    # 细计算方法如下：
    # 首先获取执行一次命令打印出来的结果, 重点关注Draw
    # Prepare
    # Process
    # Execute
    # 行下面的数据
    # Draw:是消耗在构建java显示列表DisplayList的时间。说白了就是执行每一个View的onDraw方法, 创建或者更新每一个View的DisplayList对象的时间。
    # Process：表示是消耗在Android的2D渲染器执行显示列表的时间，view越多，要执行的绘图命令就越多，时间就越长
    # Execute：消耗在排列每个发送过来的帧的顺序的时间.或者说是CPU告诉GPU渲染一帧的时间, 这是一个阻塞调用, 因为CPU会一直等待GPU发出接到命令的回复。所以这个时间，一般都很短。
    # Draw + Prepare + Process + Execute = 完整显示一帧 ，这个时间要小于16ms才能保存每秒60帧。
    # 计算总数据的行数
    # frame_count = row_num, 计算每行渲染时间render_time = Draw + Prepare + Process + Execute, 当渲染时间 > 16.67
    # ms(1000 / 60), 按照垂直同步机制，该帧已经渲染超时
    def get_myfps(self):
        adb_fps="adb shell dumpsys gfxinfo com.bitkinetic.eptool>D:fps.txt"
        get_fps=os.popen(adb_fps).readlines()

    def testprint(self):
        print("test")

    # 得到fps
    def get_fps(self,device):
        print("fps-")
        _adb_fps='adb -s '+device+' shell dumpsys gfxinfo com.bitkinetic.eptool>D:fps.txt'
       # _adb = "adb -s  "+devices+" shell dumpsys gfxinfo %s | grep -A 128 'Execute'  | grep -v '[a-Z]' "%pkg_name
        result = os.popen(_adb_fps).read().strip()
        #print result
        result = result.split('\r\n')
        for i in result:
            l_result = i.split('\t')[-3:]
            f_sum = 0
            for j in l_result:
                r = re.search(r"\d+\.\d+", str(j))
                if r:
                    f_sum += float(r.group())
                # t_result.append('%.2f'%f_sum)
            fps=float('%2f'%f_sum)
            # return float('%.2f'%f_sum)
            return fps



#启动时间：adb shell am start -W -n com.person.buddy/com.person.buddy.ui.app.LogoActivity
#点击home停止app：adb shell input keyevent 3
#冷启动停止： #cmd = 'adb shell am force-stop com.android.browser'

if __name__ == '__main__':
#    print(top_cpu(devices="DU2YYB1535002913", pkg_name="com.person.buddy"))
  #  device='127.0.0.1:62001'
    device='ac269631'
    app = appPerformance()
    app.monkey(device)
    # print(app.get_fps(device))
    # print(app.get_men(device))
    # print(app.top_cpu(device))
   #  device='DU2YYB1535002913   '

    # app.monkey(device)
   # print(get_fps())
   #  app.postman()
    pass