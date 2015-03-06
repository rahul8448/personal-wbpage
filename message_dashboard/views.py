from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf


#Create your views here.
def login_view(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)


#Create auth_view
def auth_view(request):
    user_name=request.POST.get('username','')
    pass_word=request.POST.get('password','')
    user=auth.authenticate(username=user_name, password=pass_word)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('dashboard.html')

    else:
        c={}
        c.update(csrf(request))
        return HttpResponseRedirect('login.html',c)








