from django.contrib import admin
from django.urls import path
from .views import support_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('support/', support_page),
]

