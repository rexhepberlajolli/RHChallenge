from django.conf.urls import include, url

urlpatterns = [
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^', include('user_administration.urls', namespace="UserAdministration")),
]
