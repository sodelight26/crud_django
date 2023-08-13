from django.contrib import admin
from myapp.models import STK_USER
from myapp.models import STK_TYPE
from myapp.models import STK_SIZE
from myapp.models import STK_PRD
from myapp.models import STK_ORD
from myapp.models import STK_ORDD
from myapp.models import STK_ADDP 
from myapp.models import STK_ADDPD 

# Register your models here.

admin.site.register(STK_USER)
admin.site.register(STK_TYPE)
admin.site.register(STK_SIZE)
admin.site.register(STK_PRD)
admin.site.register(STK_ORD)
admin.site.register(STK_ORDD)
admin.site.register(STK_ADDP)
admin.site.register(STK_ADDPD)