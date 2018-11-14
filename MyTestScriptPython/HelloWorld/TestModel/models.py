# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# models.py
from django.db import models

from django.contrib.auth.models import User

class TestReport(models.Model):
    name = models.CharField(max_length=20)
    testModule=models.CharField(max_length=500)
    testExplain=models.CharField(max_length=500)
    wantResult = models.CharField(max_length=500)
    testResult = models.CharField(max_length=500)
    testTime=models.CharField(max_length=500)

class test(models.Model):
    name=models.CharField(max_length=20)

class testR(models.Model):
    mid=models.CharField(max_length=10)
    time=models.TimeField()
