from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.user_list, name='users'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
