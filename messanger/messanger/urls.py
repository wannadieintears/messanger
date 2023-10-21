from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chats.urls')),
    path('account/', include('account.urls')),
    path('dialogue/', include('dialogue.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
]
