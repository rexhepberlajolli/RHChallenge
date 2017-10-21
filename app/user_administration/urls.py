from django.conf.urls import url
from .views import LoginPage, ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^$', ClientListView.as_view(), name='ClientListView'),
    url(r'^add$', ClientCreateView.as_view(), name='ClientCreateView'),
    url(r'^clients/(?P<pk>[^/]+)$', ClientDetailView.as_view(), name='ClientDetailView'),
    url(r'^clients/(?P<pk>[^/]+)/edit$', ClientUpdateView.as_view(), name='ClientUpdateView'),
    url(r'^clients/(?P<pk>[^/]+)/delete', ClientDeleteView.as_view(), name='ClientDeleteView'),
    url(r'^login/', LoginPage.as_view(), name='LoginPage'),
    url(r'^logout/', logout_then_login, name='LogoutPage'),
]
