
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.main.urls")),
    path("", include("apps.company.urls")),
    path('accounts/', include('allauth.urls')),
    
    
]
