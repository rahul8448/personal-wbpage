from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
import logging
#import json
from models import DashBoard_Messages
from django.core import serializers
from django.http import HttpResponse






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


'''
This is the view for the searching email term.
'''

@csrf_exempt
def searchEmail_view(request):

    logger.debug("Entering search email method")

    if request.method=="POST":
        #data=json.loads(request.body)
        #logger.debug(data)
        #search_term=data['search_term']
        search_term=request.POST.get('search_term')
        logger.debug('TERM:'+search_term);
    else:
     search_term=''

    emails= DashBoard_Messages.objects.filter(sender_email__contains=search_term)

    json_response = serializers.serialize('json', emails,fields=('sender_email'))
    logger.debug(json_response)
    logger.debug("Exiting search email method")
    return HttpResponse(json_response, content_type='application/json')



'''
This is the view for the searching company term.
'''

@csrf_exempt
def searchCompany_view(request):

    logger.debug("Entering search org method")

    if request.method=="POST":
        #data=json.loads(request.body)
        #logger.debug(data)
        search_term=request.POST.get('search_term')
        logger.debug('TERM:'+search_term);
    else:
     search_term=''

    orgs= DashBoard_Messages.objects.filter(sender_organization__contains=search_term)

    json_response = serializers.serialize('json', orgs,fields=('sender_organization'))
    logger.debug(json_response)
    logger.debug("Exiting search org method")
    return HttpResponse(json_response, content_type='application/json')

'''
This is the view for the searching person term.
'''

@csrf_exempt
def searchName_view(request):

    logger.debug("Entering search name method")

    if request.method=="POST":
        #data=json.loads(request.body)
        #logger.debug(data)
        search_term=request.POST.get('search_term')
        logger.debug('TERM:'+search_term);
    else:
     search_term=''

    name= DashBoard_Messages.objects.filter(sender_name__contains=search_term)

    json_response = serializers.serialize('json', name,fields=('sender_name'))
    logger.debug(json_response)
    logger.debug("Exiting search name method")
    return HttpResponse(json_response, content_type='application/json')

