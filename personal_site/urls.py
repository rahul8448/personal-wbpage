from django.conf.urls import patterns, include, url
from django.contrib import admin
import personal_page.urls

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^msg/send$', 'personal_page.views.post_message'),
    #url(r'^((msg/send)*)$', include(personal_page.urls)),
    url(r'^$', include(personal_page.urls)),
    url(r'^download/resume$', 'personal_page.views.download_resume'),
    url(r'^msg_board/login$', 'message_dashboard.views.login_view'),
    url(r'^msg_board/$', 'message_dashboard.views.login_view'),
    url(r'^msg_board/authenticate$', 'message_dashboard.views.login_view'),
    url(r'^msg_board/logout$', 'message_dashboard.views.logout_view'),


)
