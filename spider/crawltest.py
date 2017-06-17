# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ESIwebsite.settings")
# import django
# django.setup()
# from Connor.models import EsiDissertation
# EsiDissertation.objects.create(title='t1', author='t1', context='t1', publication='t1')
# with open('breakpoint.log') as f:
#     log = f.read()
#     log = eval(log)
#     print log['page'], log['item']
#
# with file('breakpoint.log','w') as f:
#     log = {
#         'page':1,
#         'item':1
#     }
#     f.write(str(log))
import traceback
def bbs():
    try:
        try:
            print '1'
            1/0
            print '2'
        finally:
            print '3'
    except:
        traceback.print_exc()
        bbs()

bbs()