from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles import views
from django.urls import path, re_path, include

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include('main.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]