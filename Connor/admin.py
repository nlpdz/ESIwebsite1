from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Connor.models import UserInfo,EsiDissertation

admin.site.register(UserInfo)
admin.site.register(EsiDissertation)