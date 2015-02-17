from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from forms import MessageForm
#import logging
#logger = logging.getLogger(__name__)



# Create your views here.


def render_landing_page(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html',c)


def post_message(request):
    c = {}
    c.update(csrf(request))
    #logger.debug("this is a debug message1!");
    if request.POST:
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
            #logger.debug("this is a debug message2!");


    return render_to_response('index.html',c)