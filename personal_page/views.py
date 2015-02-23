from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponse
from forms import MessageForm
import mimetypes
import os
import urllib
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def render_landing_page(request):
    logger.debug("Entering landing page");
    c = {}
    c.update(csrf(request))
    logger.debug("Exiting landing page");
    return render_to_response('index.html',c)


def post_message(request):
    logger.debug("Entering post message");
    c = {}
    c.update(csrf(request))

    if request.POST:
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
            logger.debug("Exiting post message");

    return render_to_response('index.html',c)

def download_resume(request):
    file_path='personal_page/static/data/Rahul_Sharma_Resume.pdf'
    original_filename='Rahul_Sharma_Resume.pdf'
    logger.debug("Entering download file");

    fp = open(file_path, 'rb')
    response = HttpResponse(fp.read())
    fp.close()
    type, encoding = mimetypes.guess_type(original_filename)

    if type is None:
        type = 'application/octet-stream'
    response['Content-Type'] = type
    response['Content-Length'] = str(os.stat(file_path).st_size)
    if encoding is not None:
        response['Content-Encoding'] = encoding

    # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
    if u'WebKit' in request.META['HTTP_USER_AGENT']:
        # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
        filename_header = 'filename=%s' % original_filename.encode('utf-8')
    elif u'MSIE' in request.META['HTTP_USER_AGENT']:
        # IE does not support internationalized filename at all.
        # It can only recognize internationalized URL, so we do the trick via routing rules.
        filename_header = ''
    else:
        # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
        filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(original_filename.encode('utf-8'))
    response['Content-Disposition'] = 'attachment; ' + filename_header

    logger.debug("Exiting download file");
    #logger.debug(response);
    return response

