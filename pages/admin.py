from django.contrib import admin
from django.utils.safestring import mark_safe

from pages.models import Page, PageSpecial


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text_1', 'image_preview')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="100" />'.format(obj.image.url))
        else:
            return 'No Image'


class PageSpecialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Page, PageAdmin)
admin.site.register(PageSpecial, PageSpecialAdmin)
