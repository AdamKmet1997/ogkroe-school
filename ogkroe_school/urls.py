from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('school.urls')),
    path('account', include("django.contrib.auth.urls")),
    path('account', include('account.urls')),
    # path('academy/', include('school.urls')),
    path('admin/', admin.site.urls),
]