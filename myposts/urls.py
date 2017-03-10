from django.conf.urls import url
from .import views

urlpatterns=[
url(r'^$',views.my_profile, name='profile'),
url(r'^gallery/$',views.post_list, name='postlist'),
url(r'^post/(?P<id>\d+)/$',views.post_detail,name='postdetail'),
url(r'^post/new$',views.new_post,name='newpost'),
url(r'^post/(?P<id>\d+)/edit/$',views.edit_post,name='editpost'),
url(r'^projects/$',views.projects, name='projects'),
url(r'^about/$',views.about,name='about'),
#url(r'^post/add/$',views.Add_images.as_view(),name='addimage'),
]