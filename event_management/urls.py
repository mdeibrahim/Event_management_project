
from django.contrib import admin
from django.urls import path, include
from tasks.views import dashboard, add_new,event
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', dashboard, name='dashboard'),
    path('event/', event, name='event'),
    path('add_new/', add_new, name='add_new'),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
