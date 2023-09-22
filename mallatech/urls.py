from django.contrib import admin
from django.urls import include, path

routes = {"home": "", "encuesta": 'polls/', "admin": 'admin/'}

urlpatterns = [
    path(routes["home"], include("hello.urls")),
    path(routes["encuesta"], include("polls.urls")),
    path(routes["admin"], admin.site.urls),
]
