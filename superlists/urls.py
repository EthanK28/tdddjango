from django.conf.urls import include, url, patterns
from django.contrib import admin

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'superlists.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     #url(r'^admin/', include(admin.site.urls)),
#     url(r'^$', 'superlists.views.home_page', name='home'),
# ]

urlpatterns = patterns('',
                       url(r'^$', 'lists.views.home_page', name='home'),
)
