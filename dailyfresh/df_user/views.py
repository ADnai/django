#coding=utf-8
from django.shortcuts import render,redirect
from hashlib import sha1
from  models import *
from django.http import HttpResponse ,HttpResponseRedirect,JsonResponse
from . import user_decorator
from df_goods.models import *

# Create your views here.
def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):
    #接受用户
    
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    #判断二次密码
    if upwd !=upwd2:
        return redirect('/user/resgister')
    #密码加密
    s1=sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()
    #创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail

    user.save()
    #注册成功到登录界面
    return redirect('/user/login/')

def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.object.filter(uname=uname).count()
    return JsonResponse ({'conut':count})
    

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'','error_name':0,'uname':uname,'error_pwd':0}
    return render(request,'df_user/login.html',context)
   

def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    users = UserInfo.objects.filter(uname=uname)
    print uname

    if len(users)==1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest()==users[0].upwd:
            red = HttpResponseRedirect('/user/info/')

            if jizhu != 0:
                red.set_cookie('uname',uname)

            else:
                red.set_cookie('uanme','',max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
             context ={'title':'用户登录','error_name':0,'error_pwd':'1','uname':uname,'upwd':upwd}
             return  render(request,'df_user/login.html',context)
  
    else:
        context ={'title':'用户登录','error_name':1,'error_pwd':'0','uname':uname,'upwd':upwd}
        return  render(request,'df_user/login.html',context)

@user_decorator.login
def info(request):
    user_email = UserInfo.objects.get(id = request.session['user_id']).uemail
    user_name  = UserInfo.objects.get(id = request.session['user_id']).uname
    #goods_ids = request.COOKIES.get('goods_ids','')
    #goods_idsl = goods_ids.split(',')
    #goods_list=[]
    #for goods_id in goods_idsl:
        #goods_list.append(GoodsInfo.objects.get(id =int(goods_id)))
    context ={'title':'abc',
              'user_email':user_email,
              'user_name':user_name
              }
    print context
    return  render(request,'df_user/profile.html',context)
          


def site(request):
    user = UserInfo.objects.get(id =request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        yser.save() 
    
    

    context = {
               'title': '用户中心',
               'user': user,
               'page_name':1
     }

    return render(request,'df_user/user_center_site.html',context)
    


def order(request):
    context = {'title':''}

    return render(request,'df_user/user_center_order.html',context)
      
def logout():
    request.session.flush()
    return redirect('/')     
   