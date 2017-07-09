# # -*- coding:utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ESIwebsite.settings")
import django
django.setup()
from Connor.models import Dissertation,refer
from django.db.models import Count, Min, Max, Sum
count = Dissertation.objects.filter(DATE__contains='2016').aggregate(Sum('REFERCOUNT'))
print count['REFERCOUNT__sum']






