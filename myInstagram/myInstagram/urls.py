from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myInstagram.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'account.views.mylogin', name='default'),
    url(r'^login/$', 'account.views.mylogin', name='login'),
    url(r'^logout/$', 'account.views.mylogout', name='logout'),
    url(r'^home/$', 'account.views.home', name='home'),
    url(r'^searchuser/$', 'account.views.autocomplete', name='userautocomplete')

) + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
