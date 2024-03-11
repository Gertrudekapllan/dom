from django.contrib import admin
from django.utils.safestring import mark_safe

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
    list_display = ('id', 'text', 'image_preview', 'get_category',)
    list_display_links = ('id',)
    search_fields = ('text',)

    def image_preview(self, obj):
        images = obj.image_set.all()
        if images:
            image_tags = ''.join('<img src="{}" width="100" />'.format(image.image_i.url) for image in images)
            return mark_safe(image_tags)
        else:
            return 'No Images'

    image_preview.short_description = 'Image Preview'

    def get_category(self, obj):
        return ', '.join(category.name for category in obj.category.all())
    get_category.short_description = 'Category'


admin.site.register(Image)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
