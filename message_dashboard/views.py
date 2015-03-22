from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
import logging
import json


logger = logging.getLogger(__name__)

#Create your views here.
def base_view(request):

    logger.debug("Entering login_view method")
    c={}
    #c['isLogged']=False;
    #c['status']="Is not logged in"
    c.update(csrf(request))

    logger.debug("Exiting login_view method")
    return render_to_response('base.html',c)


#Create auth_view
def auth_view(request):

    logger.debug("Entering auth_view method")
    logger.debug(request.body)

    if request.method == "POST":
       #Converting string to json
       #postJson=json.loads(request.body)
       #Extracting username and password
       #user_name=postJson['user_name']
       #pass_word=postJson['pass_word']

       user_name=request.POST.get('email','')
       pass_word=request.POST.get('password','')

       logger.debug("user_name:"+user_name)
       logger.debug("password:"+pass_word)
       user=auth.authenticate(username=user_name, password=pass_word)

       if user is not None:
            auth.login(request,user)
            c={}
            c['isLogged']=True
            c['status']="Is logged in"
            c.update(csrf(request))
            logger.debug(c)
            logger.debug("Logged in")
            logger.debug("Exiting auth_view method")
            #return HttpResponseRedirect('/msg_board/logged_in')
            return render_to_response('base.html',c)

    c={}
    c['isLogged']=False
    c['status']="Is not logged in"
    c.update(csrf(request))
    logger.debug(c)
    logger.debug("not logged in")
    logger.debug("Exiting auth_view method")
    #return HttpResponseRedirect('/msg_board/not_logged_in');
    return render_to_response('base.html',c)



'''
def login_view(request):

    logger.debug("Enter logged in")
    logger.debug("Exiting logged in")
    if request.user.is_authenticated:
      return render_to_response('dashboard.html')
    else:
        return render_to_response('not_logged_in')
'''







