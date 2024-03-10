from django.contrib import admin
from pages.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text_1', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Page, PageAdmin)
