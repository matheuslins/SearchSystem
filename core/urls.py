from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='home'),
]
