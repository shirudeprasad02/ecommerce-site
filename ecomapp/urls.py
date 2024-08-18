from django.urls import path
from ecomapp import views
from django.conf import settings
from django.conf.urls.static import static #this can be use to covert image path in static

urlpatterns = [
    path('product',views.product),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sort),
    path('pricefilter',views.pricefilter),
    path('search',views.search),
    path('product_detail/<pid>',views.product_detail),
    path('addtocart/<pid>',views.addtocart),
    path('cart',views.viewcart),
    path('update/<x>/<cid>',views.update),
    path('remove/<cid>',views.removecart),
    path('place_order',views.place_order),
    path('fetchorder',views.fetchorder),
    path('makepayment',views.makepayment),
    path('paymentsuccess',views.success),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)