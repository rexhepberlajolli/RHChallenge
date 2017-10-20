from django.conf.urls import url
from .views import HomePage, LoginPage
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^$', HomePage.as_view(), name='HomePage'),
    url(r'^login/', LoginPage.as_view(), name='LoginPage'),
    url(r'^logout/', logout_then_login, name='LoginPage'),
]
