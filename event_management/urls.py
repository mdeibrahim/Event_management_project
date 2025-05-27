from django.contrib import admin
from django.urls import path, include
from tasks.views import dashboard, add_new,event, update_event, delete_event
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', dashboard, name='dashboard'),
    path('event/', event, name='event'),
    path('add_new/', add_new, name='add_new'),
    path('update_event/<str:event_type>/<int:event_id>/', update_event, name='update_event'),
    path('delete_event/<str:event_type>/<int:event_id>/', delete_event, name='delete_event'),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
