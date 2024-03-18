from django.shortcuts import render, get_object_or_404

from post.models import Post, Image


def post_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_images = {}
    post_images[post] = Image.objects.filter(post=post)
    return render(request, 'post_page.html', {'post': post, 'post_images': post_images})
