from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Connor.models import *

class DissertationAdmin(admin.ModelAdmin):
    list_display = ('TITLE','DATE','AUWUST','PUBLICATION', 'CATECORY',
                   'WOSID','WOSCATE','RESEARCHDIR','REFERCOUNT','AULIST')
    list_editable = ('AULIST',)
    search_fields = ('TITLE','DATE','AUWUST','PUBLICATION', 'CATECORY',
                   'WOSID','WOSCATE','RESEARCHDIR','REFERCOUNT','AULIST')
    list_per_page=100

class referAdmin(admin.ModelAdmin):
    list_display = ('TITLE','REFERENCE_TITLE')
    search_fields = ('TITLE','REFERENCE_TITLE')
    list_per_page = 100
admin.site.register(UserInfo)
admin.site.register(EsiDissertation)
admin.site.register(locationconf)
admin.site.register(Dissertation,DissertationAdmin)
admin.site.register(refer,referAdmin)