from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

# Register your models here.

#admin.sites.AdminSite.site_header = "پنل مدیریتی جنگو"
#admin.sites.AdminSite.site_title = "پنل"
#admin.sites.AdminSite.index_title = "پنل مدیریت"
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'auther', 'publish', 'status']
    ordering = ['title', 'publish']
    list_filter = ['title', ('publish', JDateFieldListFilter), 'auther']
    search_fields = ['title','description']
    date_hierarchy ='publish'
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['status']
    list_display_links = ['auther']