from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devon_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
   
    url(r'^home/', include('devon.urls')), # ADD THIS NEW TUPLE!
    url(r'^journal/', 'devon.views.journal'),
    url(r'^tutorials/', 'devon.views.tutorials'),
    url(r'^projects/', 'devon.views.projects'),
    url(r'^ComputerScience/', 'devon.views.cs'),
    url(r'^MentalHealthProject/', 'devon.views.mh'),
    url(r'^Stories/', 'devon.views.stories'),
   
    url(r'^admin/', include(admin.site.urls)),

   
                       
)
