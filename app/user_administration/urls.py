from django.conf.urls import url
from .views import LoginPage, ClientCreateView, ClientListView, ClientDetailView
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^$', ClientListView.as_view(), name='ClientListView'),
    url(r'^add$', ClientCreateView.as_view(), name='ClientCreateView'),
    url(r'^clients/(?P<pk>[^/]+)/', ClientDetailView.as_view(), name='ClientDetailView'),
    url(r'^login/', LoginPage.as_view(), name='LoginPage'),
    url(r'^logout/', logout_then_login, name='LogoutPage'),
]
