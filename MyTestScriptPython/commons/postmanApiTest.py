# coding=utf-8
import time
import os
class postmanApiTest:
    #运行postman生成报告
    #通过newman

    def postman(self):
        jSONfname = 'D:/htmlOut' + time.strftime('%Y-%m-%d', time.gmtime())+'.html'
        # C:\Users\73016\AppData\Roaming\npm\newman  -c C:/Users/73016/Desktop/YunShuTest.postman_collection.json -e  C:/Users/73016/Desktop/YunShuTest.postman_environment.json -r  --reporters cli,html,json,junit -r   --reporter-html-export
        cmd = 'newman run  C:/Users/73016/Desktop/YunShuTest.postman_collection.json -e  C:/Users/73016/Desktop/YunShuTest.postman_environment.json -r   --reporters cli,html,json,junit -r   --reporter-html-export '+jSONfname
        #cmd='newman run D:/Buddy_Product_Enviroment.postman_collection.json --reporters cli,html,json,junit --reporter-json-export D:/jsonOut.json --reporter-junit-export D:/xmlOut.xml --reporter-html-export D:/htmlOut.html'
        #cmd='newman run  D:/Postman Echo.postman_collection.json  --reporters cli,html,json,junit --reporter-json-export D:/jsonOut.json --reporter-junit-export D:/xmlOut.xml --reporter-html-export D:/htmlOut.html'
        os.system(cmd)
        print('------------------------------------------------------------')
        print(jSONfname)
        if  os.path.isfile(jSONfname):
            return jSONfname
            print(jSONfname)
        else:
            return False
if __name__ == '__main__':
    a=postmanApiTest()
    a.postman()