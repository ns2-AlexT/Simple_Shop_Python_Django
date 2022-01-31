from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('user/del/<int:user_pk>', adminapp.user_del, name='user_del'),
    path('user/upd/<int:user_pk>', adminapp.UserUpd.as_view(), name='user_upd'),
    path('cat/<int:pk>/products/', adminapp.cat_products, name='cat_products'),
    path('cat/<int:cat_pk>/products/create', adminapp.cat_product_create, name='cat_product_create'),
    # path('cat/', adminapp.categories, name='categories'),
    # CBV
    path('cat/create/', adminapp.ProductCatCreate.as_view(), name='cat_create'),
    path('cat/upd/<int:pk>/', adminapp.ProductCatUpd.as_view(), name='cat_upd'),
    path('cat/', adminapp.CategoriesList.as_view(), name='categories'),
    path('cat/del/<int:pk>/', adminapp.ProductCatDel.as_view(), name='cat_del'),
    path('product/<int:pk>/', adminapp.ProductDetail.as_view(), name='product_details'),
]
