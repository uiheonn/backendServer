from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('accounts.urls')),
    path('', include('boards.urls')),
    path('', include('filter.urls')),
    path('', include('emaillist.urls')),
    path('', include('emaillist2.urls')),
    path('', include('myfolders.urls')),
    path('', include('keywords.urls')),
]