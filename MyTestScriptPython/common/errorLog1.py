# coding=utf-8

import os,time
import subprocess

def get_error(log="d:\log.txt"):
    cmd_logcat='adb  shell "logcat|grep buddy" > D: / buddylog.txt'
   # handle = subprocess.Popen("adb -s "+devices+ "-d  logcat >" +log, shell=True)
    handle = subprocess.Popen(cmd_logcat, shell=True)
    time.sleep(1)
    os.system("adb logcat -s DU2YYB1535002913 -c")
    subprocess.Popen("taskkill /F /T /PID " + str(handle.pid) , shell=True)


def save_log(log="d:\log.txt", pack=""):
    os.system('adb  shell "logcat|grep buddy" > D: / buddylog.txt')

if __name__ == '__main__':
    save_log()
    #get_error()