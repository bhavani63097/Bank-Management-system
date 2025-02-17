from django.contrib import admin
from application.models import account,announcement

class account_admin(admin.ModelAdmin):
    list_display=['id','Account_number','First_name','Middle_name','Last_name','Email','Password','Pin','Current_balance','Created_at','Updated_at','Deposit_amount','Dep_date','Withdraw_amount','With_date','Transfor_amount_from']
admin.site.register(account,account_admin)

class announcement_admin(admin.ModelAdmin):
    list_display=['id','Title','Announcement','Date_created','Date_updated']
admin.site.register(announcement,announcement_admin)
    