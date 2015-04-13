from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import personal_page.urls

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^msg/send$', 'personal_page.views.post_message'),
    #url(r'^((msg/send)*)$', include(personal_page.urls)),
    url(r'^$', include(personal_page.urls)),
    url(r'^download/resume$', 'personal_page.views.download_resume'),
    #url(r'^msg_board/base$', 'message_dashboard.views.login_view'),
    url(r'^msg_board/$', 'message_dashboard.views.base_view'),
    url(r'^msg_board/authenticate$', 'message_dashboard.views.auth_view'),
    url(r'^msg_board/logout$', 'message_dashboard.views.logout_view'),
    #url(r'^msg_board/logged_in$', 'message_dashboard.views.login_view'),
    #url(r'^msg_board/not_logged_in$', 'message_dashboard.views.login_view'),
    url(r'^search/email$', 'message_dashboard.views.searchEmail_view'),
    url(r'^search/org$', 'message_dashboard.views.searchCompany_view'),
    url(r'^search/name$', 'message_dashboard.views.searchName_view'),

)
