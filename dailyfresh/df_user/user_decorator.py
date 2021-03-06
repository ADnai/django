#coding=utf-8
from  django.http import HttpResponseRedirect
from    django.shortcuts import redirect


def login(func):
	def login_fun(request,*arg,**kwarge):
		if request.session.has_key('user_id'):
		    return func(request ,*arg,**kwarge)
		else:
			red = HttpResponseRedirect('/user/login/')
			red.set_cookie('url',request.get_full_path())
			return red
    		
	
	return login_fun