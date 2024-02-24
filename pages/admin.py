from django.contrib import admin
from pages.models import Page


class PageImageInline(admin.TabularInline):
    model = Page
    extra = 0
    # readonly_fields = ('preview', 'modified')
    # fields = ('preview', 'modified', '')


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    Inlines = [PageImageInline]


admin.site.register(Page, PageAdmin)
