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
    list_display = ('id', 'text', 'image_preview', )
    list_display_links = ('id',)
    search_fields = ('text',)

    def image_preview(self, obj):
        first_image = obj.image_set.first()
        if first_image:
            return mark_safe('<img src="{}" width="100" />'.format(first_image.image_i.url))
        else:
            return 'No Image'

    image_preview.short_description = 'Image Preview'

    image_preview.short_description = 'Image Preview'


admin.site.register(Image)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
