from django.contrib import admin

from images.models import TblImage

class ImageAdmin(admin.ModelAdmin):
    list_display = ( "name", "md5", "show_pic")


admin.site.register(TblImage,ImageAdmin)