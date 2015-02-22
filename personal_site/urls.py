from django.conf.urls import patterns, include, url
from django.contrib import admin
import personal_page.urls

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^msg/send$', 'personal_page.views.post_message'),
    #url(r'^((msg/send)*)$', include(personal_page.urls)),
    url(r'^$', include(personal_page.urls)),
    url(r'^download/resume$', 'personal_page.views.download_resume'),

)
