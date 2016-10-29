from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	url(r'^$', views.ListBoxView.as_view(), name='list_box'),
	url(r'^create/$', views.CreateBoxView.as_view(), name="create_box"),
	url(r'^edit/(?P<slug>[\w_-]+)/$', views.UpdateBoxView.as_view(), name='update_box'),
	url(r'^delete/(?P<slug>[\w_-]+)/$', views.DeleteBoxView.as_view(), name='delete_box'),]
