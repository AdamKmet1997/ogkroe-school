from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('account.urls')),
    path('account', include("django.contrib.auth.urls")),
    path('account', include('account.urls')),
    path('school/', include('school.urls')),
    path('admin/', admin.site.urls),
]