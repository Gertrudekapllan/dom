from django.contrib import admin

from post.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'image')
    list_display_links = ('id', 'text')
    search_fields = ('text',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
