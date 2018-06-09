from django.shortcuts import render,redirect
from hashlib import sha1
from  models import *
from django.http import HttpResponse ,HttpResponseRedirect,JsonResponse
from df_user import user_decorator
from df_user.models import UserInfo
from df_cart.models import *
from django.db import transaction
from datetime  import datetime
from decimal import Decimal


@user_decorator.login
def Order(request):
    user = UserInfo.objects.get(id =request.session['user_id'])
    get  = request.GET 

    cart_ids = get.getlist('cart_id')
    cart_idsl=[int(item) for item in cart_ids]
    carts = CartInfo.objects.filter(id__in=cart_idsl)
    
    context={'title':'',
             'page_name':1,
             'carts':carts,
             'user':user,
             'cart_ids':','.join(cart_ids)}
    return render(request,'df_order/order.html',context)
# Create your views here.

# @transaction.atomic()
# @user_decorator.login
# def order_handle():
# 	tran_id = transaction.savepoint()
# 	cart_ids = request.POST.get('cart_ids')
# 	try:
# 		order = OrderInfo()
# 		now = datetime.now()
# 		uid = request.session['user_id']
# 		order.oid ='%s%d' % (now.strftime('%Y%m%H%M%S'),uid)
# 		order.user_id = uid
#       order.odate = now
#       order.ototal = DeCimal(request.POST.get('total'))
#       order.save()

#       cart_idsl=[int(item)for item in cart_ids.split(',')]
#       for idl in cart_idsl:
#           detail = OrderDetailInfo()
#         	detail.order = order
#         	cart = CratInfo.objects.get(id =idl)
#         	goods = cart.goods
#         	if goods.gkucun >= cart.count
#             	goods.gkucun =cart.goods.gkucun - cart.count
#             	good.save()

#             	detail.goods_id = goods.id
#               detail.price = goods.gprice
#               detail.count =cart.count
#               detail.save()
#               cart.delete()
#           else:
#               transaction.savepoint_rollback(tran_id)
#               return redirect('/cart/')
#       transaction.savepoint_commit(tran_id)           
#    except Exception as e:
# 	    print   '================%s'% e
# 		transaction.savepoint_rollback(tran_id)

# 	return  redirect('/user/order/')


# @user_decorator.login
# def pay(request.oid):
# 	order = OrderInfo.objects.get(oid=oid)
# 	order.oIsPay= True
# 	order.save()
# 	context={'order':order}
# 	return render(request,'df_order/pay.html',context)

			
# 	