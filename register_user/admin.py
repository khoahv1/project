from django.contrib import admin
from register_user.models import Nguoidung
# Register your models here.
class NguoidungAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    list_display_links = ('username','email')
    list_filter = ('username','email')
    search_fields = ('username','email')
    list_per_page = 25
    
admin.site.register(Nguoidung, NguoidungAdmin)