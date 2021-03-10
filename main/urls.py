from django.urls import path
from .views import redir, home_page
urlpatterns = [
    path('', redir),
    path('home/', home_page)
]

