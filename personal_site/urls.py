from django.conf.urls import patterns, include, url
from django.contrib import admin
import personal_page.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'personal_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(personal_page.urls)),
    url(r'^msg/send$', include(personal_page.urls)),
)
