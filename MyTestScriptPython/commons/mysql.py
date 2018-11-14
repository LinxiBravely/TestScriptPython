# coding=utf-8
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

class mysql(object):

    def insertSqlPerformmance(self):
        # 打开数据库连接
        db = MySQLdb.connect("127.0.0.1", "root", "O0Vkki1Un0W", "zentao", charset='utf8' )

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        perFormmanceSql="INSERT INTO testmodel_phonePerformance(cpuTop,cpuDump,men,fps)"+"  "+"VALUE( "+value+ ")"
        try:
           # 执行sql语句
           cursor.execute(perFormmanceSql)
           print("insert success")
           # 提交到数据库执行
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()
        # 关闭数据库连接
        db.close()

    def insertSqlPhoneInfo(self,value):
        # 打开数据库连接
        db = MySQLdb.connect("127.0.0.1", "root", "O0Vkki1Un0W", "zentao", charset='utf8' )

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 插入语句

        relsql="INSERT INTO testmodel_mphoneinfo(phoneName,mrelease,model,brand,device,introdution,mstatus)"+"  "+"VALUE( "+value+ ")"
        print ("--------------------------------------------------------")
        print (relsql)
        #
        # sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
        #          LAST_NAME, AGE, SEX, INCOME)
        #          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        #
        sql = """INSERT INTO testmodel_test(name) VALUES (' Mac ')"""
        # print ("--------------------------------------------------------")
        # print (sql)
        try:
           # 执行sql语句
           cursor.execute(relsql)
           print("insert success")
           # 提交到数据库执行
           db.commit()
        except:
           # Rollback in case there is any error
           db.rollback()

        # 关闭数据库连接
        db.close()

m=mysql()
# valueName=['phoneName','release','model','brand','device','introdution']
value="'phoneName','release','model','brand','device','introdution','1'"
m.insertSqlPhoneInfo(value)
