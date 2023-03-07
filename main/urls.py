from django.urls import path
from .views import *

urlpatterns = [
    path("get-info/", get_info_social),
    path("create-order/", create_order),
    path("get-discount/", get_discount),
    path("get-product/", get_product),
    path("get-about-product/", get_about_product),
    path("get-about-company/", get_about_company),
    path("get-who-use/", get_how_use),
    path("get-how-to-use/", get_how_use),
    path("get-fact/", get_fact),
]