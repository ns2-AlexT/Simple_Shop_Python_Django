from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    # //***//
    path('', mainapp.index, name='index'),
    path('contacts/', mainapp.contact, name='contact'),
    path('catalog/', mainapp.products, name='products'),
    path('category/<int:pk>/', mainapp.category, name='category'),
    path('product/<int:pk>/', mainapp.page_of_product, name='page_of_product'),
    # //***//
]
