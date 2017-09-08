from django.contrib import admin
from rango.models import Category, Page, UserProfile


#Add classes to customize the admin page
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_Fields = {'slug':('name',)}

#Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)