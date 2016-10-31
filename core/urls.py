from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', views.ListBoxView.as_view(), name='list_box'),
	url(r'^log/$', views.LogView.as_view(), name='log'),
	url(r'^create/$', views.CreateBoxView.as_view(), name="create_box"),
	url(r'^edit/(?P<pk>\d+)/$', views.UpdateBoxView.as_view(), name='update_box'),
	url(r'^delete/(?P<pk>\d+)/$', views.DeleteBoxView.as_view(), name='delete_box'),
	url(r'^view/(?P<pk>\d+)/$', views.DetailBoxView.as_view(), name='detail_box'),
]

# from django.conf.urls import url, include
# from django.contrib.auth import views as auth_views
# from . import views


# urlpatterns = [
# 	url(r'^$', views.ListBox.as_view(), name='box'),
# 	url(r'^box/(?P<slug>[\w_-]+)/$', views.BoxDetail.as_view(), name='detail_box'),
# ]