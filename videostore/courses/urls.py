
from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('shop/<slug>', views.ShopDetailPage.as_view(), name='gems'),
    path('shop/<slug>/<shop_slug>', views.ShopSlugDetailPage.as_view(), name='shop-detail')
]
