from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('account.urls')),
    path('account', include("django.contrib.auth.urls")),
    path('account', include('account.urls')),
    path('academy/', include('school.urls')),
    path('youtube/', include('ogkroe_youtube.urls')),
    path('admin/', admin.site.urls),
]