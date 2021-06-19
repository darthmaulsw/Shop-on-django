from django.urls import path, include
from .views import redir, home_page, Store_Page, aboutus_page, ProductDetailView, CategoryDetailView, CartView, AddToCartView, DeleteFromCartView,ChangeQTYView,CheckoutView,MakeOrderView
urlpatterns = [
    path('', redir),
    path('home/', home_page, name="home"),
    path('store/', Store_Page.as_view()),
    path('about_us/', aboutus_page),
    path('store/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name="product_detail"),
    path('', include('contact.urls')),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),


]

