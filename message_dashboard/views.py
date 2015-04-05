from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
import logging



logger = logging.getLogger(__name__)

'''
This is the base_view for login page
'''
def base_view(request):

    logger.debug("Entering login_view method")
    c={}
    c.update(csrf(request))

    redirectUrl= isUserLogged(request)
    if redirectUrl is not None:
        return redirectUrl

    logger.debug("Exiting login_view method")
    return render_to_response('base.html',c)


'''
This is the method to authenticate user credentials
'''
def auth_view(request):

    logger.debug("Entering auth_view method")
    logger.debug(request.body)

    redirectUrl= isUserLogged(request)
    if redirectUrl is not None:
        return redirectUrl

    if request.method == "POST":
       user_name=request.POST.get('email','')
       pass_word=request.POST.get('password','')

       logger.debug("user_name:"+user_name)
       logger.debug("password:"+pass_word)
       user=auth.authenticate(username=user_name, password=pass_word)

       if user is not None:
            auth.login(request,user)
            logger.debug("Logged in")
            logger.debug("Exiting auth_view method")
            return HttpResponseRedirect('/msg_board')

    logger.debug("not logged in")
    logger.debug("Exiting auth_view method")
    return HttpResponseRedirect('/msg_board')

'''
This is a helper method to check if the user was already logged in
'''
def isUserLogged(request):
    logger.debug("Entering isUserLogged method")
    if request.user.is_authenticated():
       c={}
       c.update(csrf(request))
       c['isLogged']=True
       c['username']=request.user.username
       logger.debug("Exiting isUserLogged method method")
       return render_to_response('base.html',c)


'''
This is the logout view
'''
def logout_view(request):
    logger.debug('Entering the logout_view')
    #logger.debug(request._get_request)
    auth.logout(request)
    logger.debug('Exiting the logout_view')
    return HttpResponseRedirect('/msg_board')







