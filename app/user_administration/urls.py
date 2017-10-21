from django.conf.urls import url
from .views import LoginPage, ClientCreateView, ClientListView
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^$', ClientListView.as_view(), name='ClientListView'),
    url(r'^add$', ClientCreateView.as_view(), name='ClientCreateView'),
    url(r'^login/', LoginPage.as_view(), name='LoginPage'),
    url(r'^logout/', logout_then_login, name='LogoutPage'),
]
