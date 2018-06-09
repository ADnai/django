#coding = utf-8
from django.shortcuts import render
from models import *
from  django.core.paginator  import  Paginator , Page
 

def index(request):

    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2= typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    context= {'title':'','guest_cart':1,
              'type0':type0,'type01':type01,
              'type1':type1,'type11':type11,
              'type2':type2,'type21':type21,
              'type3':type3,'type31':type31,
              'type4':type4,'type41':type41,
              'type5':type5,'type51':type51,}
    return render(request,'df_goods/index.html',context)


def list(request,tid,pindex,sort):
  typeinfo = TypeInfo.objects.get(pk=int(tid))
  news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
  if  sort == 1:
      goods_list = Goodsinfo.objects.fiter(gtype_id = int(tid)).order_by('-id')
      
      #elif sort == 2:
         # goods_list = Goodsinfo.objects.fiter(gtype_id = int(tid)).order_by('-price')
      #elif sort == 3:
          #goods_list = Goodsinfo.objects.fiter(gtype_id = int(tid)).order_by('-gclick')
    
  paginator = Paginator(goods_list,10)
  page = paginator.page(int(pindex))
  context = {
               title:typeinfo.ttiltle,'guest_cart':1,
               'page':page,
               'paginator':paginator,
               'typeinfo':typeinfo,
               'sort':sort,
               'new':news}

  return render(request,'df_goods/list.html',context)

def detail(request,id):
  goods = Goodsinfo.objects.get(pk= int(id))
  goods.gclick = goods.gclick +1
  goods.save()
  news = goods.gtype.goodsinfo_set.order_by('_id')[0:2]
  context = {
             title:goods.gtype.ttitle,'guest_cart':1,
               
               'g':goods,
               
               'id':id,
               'new':news
  }

  return render(request, 'df_goods/detail.html',context)


  goods_ids = request.COOKIES.get('goods_ids','')
  goods_ids = '%d'%goods.id
  if goods_ids != '':
      goods_idsl = goods_ids.split(',')
      if goods_idsl.conut(goods_id)>=1:
          goods_idsl.remove(goods_id)
      goods_idsl.insert(0,goods_id)
      if len(goods_idsl) >=6:
          del goods_idsl[5]
  else:
    goods_ids = goods_id
  response.set.cookie('goods_ids',goods_ids)
  

  return response


from haystack.views import SearchView

class MySearchView(SearchView):
  
  def extra_context(self):
    context = super(MySearchView,self).extra_context()
    context['title']=''
    context['guest_cart']=1
    context['cart_count'] = cart_count(self.request)

    return context
 




# Create your views here.


