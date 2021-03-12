from django.urls import path
from .views import redir, home_page, store_page, aboutus_page, support_page
urlpatterns = [
    path('', redir),
    path('home/', home_page),
    path('store/', store_page),
    path('about_us/', aboutus_page),
    path('support/', support_page),
]

