from django.shortcuts import render,get_object_or_404
from .models import Blog

def allblogs(request):
    allblogs = Blog.objects.all()
    return render(request,"blog/allblogs.html",{"allblogs":allblogs})


def detailblog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'blog/detailblog.html',{'blog':blog})
