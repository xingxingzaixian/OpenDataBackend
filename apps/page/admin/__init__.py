from django.contrib import admin

from page.models import TblPage, TblPageGroup

from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    list_display = ( "name", "is_home", "id", 'group')


class PageGroupAdmin(admin.ModelAdmin):
    list_display = ( "remark", "name", "id")


admin.site.register(TblPage,PageAdmin)
admin.site.register(TblPageGroup,PageGroupAdmin)