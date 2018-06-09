from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from .models import *
# Create your views here.

def index(request):
    #temp=loader.get_template('booktest/index.html')
    bookList = BookInfo.objects.all()
    context ={'list':bookList}
    return render(request, 'booktest/index.html',context)
def show(request,id):
    book = BookInfo.objects.get(pk=id)
    heroList= book.heroinfo_set
    context ={'list':heroList}
    return render(request,'booktest/show.html',context)
    