# coding=utf-8
from django.http import HttpResponse
from models import test
def test(request):
    test1=test(name="TOM")
    test1.save()
    return  HttpResponse("<p>数据添加成功！</p>")