from django.contrib import admin
from .models import Product ,Test

class ProductAdmin(admin.ModelAdmin):
          list_display=["name",'price',"content"]
          list_display_links=['name','price']
          list_editable=['content']
          search_fields=['name']
          list_filter=['category']

admin.site.register(Product,ProductAdmin)
admin.site.register(Test)
admin.site.site_header='Lotfy'
admin.site.site_title="Lotfy"