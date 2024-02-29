from django.contrib import admin

from post.models import Post, Category, Image


class PostImageInline(admin.TabularInline):
    model = Image
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    list_display = ('id', )
    list_display_links = ('id',)
    search_fields = ('text',)


admin.site.register(Image)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
