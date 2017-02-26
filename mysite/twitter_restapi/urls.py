from django.conf.urls import url
from . import views
from django.conf import settings

app_name='twitter_restapi'

urlpatterns=[
url(r'^$',views.home,name='home'),
url(r'^initial_cloud/$',views.initial_cloud,name='initial_cloud'),
url(r'^home/$',views.initial,name='initial'),
url(r'^fetch/$',views.index,name='index'),
url(r'^cloud/$',views.cloud,name='cloud'),
# url(r'^image/$',views.image,name='image'),
url(r'^initial_network/$',views.initial_network,name='initial_network'),

url(r'^network/$',views.network,name='network'),
url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
]

