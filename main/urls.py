from django.urls import path,include
from .views import redir, home_page, store_page, aboutus_page, ProductDetailView, CategoryDetailView
urlpatterns = [
    path('', redir),
    path('home/', home_page, name="home"),
    path('store/', store_page),
    path('about_us/', aboutus_page),
    path('store/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name="product_detail"),
    path('', include('contact.urls')),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),

]

