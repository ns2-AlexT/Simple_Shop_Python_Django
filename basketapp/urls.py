from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('index/', basketapp.index, name='index'),
    path('add/<int:product_pk>/', basketapp.add, name='add'),
    path('remove/<int:basket_pk>/', basketapp.remove, name='remove'),
    path('upd/<int:basket_pk>/<int:quantity_p>/', basketapp.upd),
]
