from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('category/<cat>/<subCat>', views.category, name='subcategory'),
    path('category/<cat>', views.category, name='category'),
    path('checkout', views.checkout, name='checkout'),
    path('product/<id>', views.product, name='product'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('search', views.search, name='search'),
    path('blog', views.blog, name='blog'),
    path('remove/<id_cart>', views.remove, name='remove'),
    path('write', views.write, name='write'),
    path('account', views.account, name='account'),
    path('empty', views.empty, name='empty'),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('order', views.order, name="order"),
    path('display_orders', views.display_orders, name="display_orders"),

]







