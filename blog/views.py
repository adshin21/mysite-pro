from django.shortcuts import render , get_object_or_404     #404 object is for show errors in case if any

# Create your views here.
from .models import Blog
def allblogs(request):
    blog = Blog.objects
    return render(request, 'blog/allblogs.html',{'allblogs' : blog})

def detail(request,blog_id):
    detail_of_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/detail.html',{'blog': detail_of_blog} )
