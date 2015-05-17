from django.conf.urls import include, url, patterns
from django.contrib import admin
from lists.views import HomePageView

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'superlists.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     #url(r'^admin/', include(admin.site.urls)),
#     url(r'^$', 'superlists.views.home_page', name='home'),
# ]

urlpatterns = patterns('',
                       url(r'^$', HomePageView.as_view(), name='home'),
                       # url(r'^$', 'lists.views.home_page', name='home'),
                       url(r'^lists/', include('lists.urls')),

                    )

