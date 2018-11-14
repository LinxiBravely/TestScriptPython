# coding=utf-8

from django.http import HttpResponse

from TestModel.models import TestReport,test


# 数据库操作
#添加数据
def testdbAdd(request):
    test1 = test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

#数据修改


#显示数据
# 数据库操作
def testdbShow(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = TestReport.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = TestReport.objects.filter(id=1)

    # 获取单个对象
    response3 = TestReport.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    TestReport.objects.order_by('name')[0:2]

    # 数据排序
    TestReport.objects.order_by("id")

    # 上面的方法可以连锁使用
    TestReport.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


# 数据库操作修改
def testdbXiugai(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = TestReport.objects.get(id=1)
    test1.name = 'Google'
    test1.save()

    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")