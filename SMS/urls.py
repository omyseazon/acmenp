
from django.contrib import admin
from django.urls import path
from django.urls.conf import include


admin.site.site_header = "SMS Admin"
admin.site.site_title = "SMS Admin Portal"
admin.site.index_title = "Welcome to SMS Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SchoolApp.urls')),
]
