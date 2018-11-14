# coding=utf-8
#驼峰处理
#StringA_b 代表有_
#StringAb  代表驼峰字符形式
def tuoFeng(StringA_b):
    StringLIst=str(StringA_b).split("_")
    # print StringLIst
    for x in StringLIst:
        oneString=x.capitalize()
        StringAb=''.join(oneString)
        print oneString



As_dddd="As_dddd"
tuoFeng(As_dddd)
