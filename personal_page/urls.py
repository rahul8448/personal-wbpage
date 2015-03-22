from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Jerico.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'personal_page.views.render_landing_page'),
    url(r'^msg/send$', 'personal_page.views.post_message'),
    url(r'^download/resume$', 'personal_page.views.download_resume'),
    #url(r'^msg_board/index$', 'message_dashboard.views.login_view'),
    #url(r'^msg_board/authenticate$', 'message_dashboard.views.login_view'),
    #url(r'^msg_board/logout$', 'message_dashboard.views.logout_view'),
 )
