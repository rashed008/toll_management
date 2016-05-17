from django.contrib import admin
from .models import tollcounter
from .models import TollTransaction
from .models import Accounts


class tolladmin(admin.ModelAdmin):
    list_display=('counter_no','counter_rate')

class TollTransactionadmin(admin.ModelAdmin):
    list_display=('counterno', 'Registration_no', 'counter_rate', 'Date_time')

class Accountsadmin(admin.ModelAdmin):
    list_display=( 'Registration_no', 'Payments', 'Receive', 'Date_time', 'Balance')

admin.site.register(tollcounter,tolladmin)
admin.site.register(TollTransaction,TollTransactionadmin)
admin.site.register(Accounts,Accountsadmin)
admin.site.site_header= 'TOLL MANAGEMENT SYSTEM'
