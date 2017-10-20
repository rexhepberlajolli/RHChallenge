from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('user_administration.urls', namespace="UserAdministration")),
]
