from django.contrib import admin
from application.models import Product
class item_admin(admin.ModelAdmin):
    list_display=['name','description','price']
admin.site.register(Product,item_admin)
