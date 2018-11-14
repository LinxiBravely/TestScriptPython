# coding=utf-8
import yagmail
import os
# import mysql
from mysql import *
class sendmail(object):
    # def __init__(self):
        #链接邮箱服务器
    def check_file(self):
        if not os.path.isfile(self.file):
            # print('文件不存在' + self.file)
            # sys.exit()
            return False
        else:
            return True
        # print("文件存在！")

    # 发送正文，不带附件
    def sendmail(self,users,subjecttitle,contents):
        yag = yagmail.SMTP(user="15088132074@163.com", password="15088132074wj", host='smtp.163.com')

        # 发送邮件
        yag.send(users, subjecttitle, contents)
        # #发送带附件的邮件
    def sendmailFile(self, users,subjecttitle,contents,file):
        yag = yagmail.SMTP(user="15088132074@163.com", password="15088132074wj", host='smtp.163.com')

        # 发送邮件
        yag.send(users, subjecttitle, contents,file)
        # yag.send('15088132074@163.com', '发送附件', contents, ["d://testresult.html"])






x=sendmail()
# # 邮箱正文
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']
x.sendmail('15088132074@163.com', '发送邮件', contents)
# x.sendmailFile('15088132074@163.com', '发送带附件的邮件', contents, ["D:/htmlOut2018-06-22.html"])

m=mysql()
m.insertSql()




        # 成功的例子
        # yag = yagmail.SMTP(user="15088132074@163.com", password="15088132074wj", host='smtp.163.com')
        #
        #
        # # 邮箱正文
        # contents = ['This is the body, and here is just text http://somedomain/image.png',
        #             'You can find an audio file attached.', '/local/path/song.mp3']
        #
        # # 发送邮件
        # yag.send('15088132074@163.com', 'subject', contents)
        #
        # #给多个用户发送邮件#
        # # 发送邮件
        # yag.send(['15088132074@163.com','730162062@qq.com'], 'subject', contents)
        # #发送带附件的邮件
        #yag.send('15088132074@163.com', '发送带附件的邮件', contents, ["d://testresult.html"])
