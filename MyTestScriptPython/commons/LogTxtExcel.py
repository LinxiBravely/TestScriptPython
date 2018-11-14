# coding=utf-8
# coding=utf-8
import time
import xlsxwriter
import os
from PhoneInfo import PhoneInfo

class Loginfo(object):
	def __init__(self, path = '', mode = 'w'):
		fname = path + time.strftime('%Y-%m-%d', time.gmtime())
		self.log = open(path + fname + '.txt', mode)

	def log_init(self, sheetname, *title):
		pass

	def log_write(self, msg):
		self.log.write(msg)

	def log_close(self):
		self.log.close()

class Xlloginfo(object):
	def __init__(self, path=''):
		fname = path + time.strftime('%Y-%m-%d', time.gmtime())
		self.row = 0
		self.xl = xlsxwriter.Workbook(path+fname+'.xls')
		self.style = self.xl.add_format({'bg_color':'red'})
	def xl_write(self, *args):
		col = 0
		style =''
		if 'Error' in args:
			style = self.style
		for val in args:
			self.sheet.write_string(self.row, col, val, style)
			col += 1
		self.row+=1
	def log_init(self, sheetname, *title):
		self.sheet = self.xl.add_worksheet(sheetname)
		self.sheet.set_column('A:E', 30)
		self.xl_write(*title)
        print("1111111111")

	def log_write(self, *args):
		self.xl_write(*args)
	def log_close(self):
		self.xl.close()

class txt(object):
	# Filename : test.py
	# author by : www.runoob.com
	def __init__(self, path = '', mode = 'w'):
		fname = path + time.strftime('%Y-%m-%d', time.gmtime())
		self.log = open(path + fname + '.txt', mode)

	# 写文件
	def writeTxt(self):
		with open("test.txt", "wt") as out_file:
			out_file.write("该文本会写入到文件中\n看到我了吧！")

	# Read a file
	def readTxt(self):
		with open("test.txt", "rt") as in_file:
			text = in_file.read()
			print(text)


if __name__ == '__main__':

	x=txt()
	x.ReadTxt()
	# device = "127.0.0.1:62001"
	# os.system("adb connect " + device)
	# x=PhoneInfo()
	# y=x.get_phone_info(device)
	# log = Loginfo()
	# log.log_write('test Loginfo 测试')
	# print (y)
	# log.log_close()




    # xinfo = Xlloginfo()
    # xinfo.log_init('test', 'uname', 'pwd', 'result', 'info')
    # xinfo.log_write('123', '123', 'Err111or', 'e111rror')
    # xinfo.log_write('123', '123', 'Error', 'error')
    # xinfo.log_close()
