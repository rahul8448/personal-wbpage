from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date, timedelta
from django.utils import timezone
import logging
import json
from message_dashboard.models import DashBoard_Messages
from message_dashboard.serializers import DashBoard_MessagesSerializer




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



'''
This is the view for the searching company term.
'''
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
'''''

'''
This is the view for the searching person term.
'''
''''
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
'''


'''
This is method is in favor of searchName_view which will eventually be phased out.
'''

@csrf_exempt
def searchDB_view(request):

    logger.debug("Entering DB view method")

    if request.method=="POST":
       name= DashBoard_Messages.objects.all()

    json_response = serializers.serialize('json', name,fields=('sender_name','sender_organization','sender_email'))
    logger.debug(json_response)
    logger.debug("Exiting DB view method")
    return HttpResponse(json_response, content_type='application/json')

###Below are Rest methods############################################
'''
 Get messages from database and return a json response.
'''

@api_view(['GET'])
def get_messages(request):

    logger.debug("Entering get_messages method")
    period=request.GET.get('period')
    logger.debug(request.GET        )
    logger.debug(period)
    if period=='All':
        messages=DashBoard_Messages.objects.all()
    elif period=='30days':
        #d = date.today() - timedelta(days=30)
        d = timezone.now()- timedelta(days=30)
        logger.debug(d)
        messages=DashBoard_Messages.objects.filter(create_time__gte=d)
    elif period=='7days':
        #d = date.today() - timedelta(days=7)
        d = timezone.now()- timedelta(days=7)
        logger.debug(d)
        messages=DashBoard_Messages.objects.filter(create_time__gte=d)
    elif period=='24hours':
        d = timezone.now() - timedelta(hours=24)
        logger.debug(d)
        messages=DashBoard_Messages.objects.filter(create_time__gte=d)
    else:
        messages=DashBoard_Messages.objects.all()

    serialized_output=DashBoard_MessagesSerializer(messages,many=True)

    logger.debug("Exiting get_messages method")
    return Response(serialized_output.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def search_messages(request):

    logger.debug("Entering search_messages method")

    email=request.GET.get('email','')
    organization=request.GET.get('organization','')
    person=request.GET.get('person','')
    keyword=request.GET.get('keyword','')
    start_date=request.GET.get('start_date','')
    end_date=request.GET.get('end_date','')

    logger.debug(email)
    logger.debug(organization)
    logger.debug(person)
    logger.debug(keyword)
    logger.debug(start_date)
    logger.debug(end_date)

    messages=DashBoard_Messages.objects.filter(sender_email__iexact=email,
                                               sender_organization__contains=organization,
                                               sender_name__iexact=person,message_subject__contains=keyword,
                                               message_body__contains=keyword,create_time__gte=start_date,
                                               create_time__lte=end_date)

    serialized_output=DashBoard_MessagesSerializer(messages,many=True)

    logger.debug("Exiting get_messages method")
    return Response(serialized_output.data,status=status.HTTP_200_OK)


