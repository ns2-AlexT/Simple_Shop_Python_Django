from random import random, choice

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory
from mainapp.models import Product


# //***//
def get_type_p():
    return ProductCategory.objects.exclude(is_active=False)


def get_sale_product():
    return choice(Product.objects.exclude(sale_atr=0))
    # return random.choice(Product.objects.exclude(sale_atr=0)) <- choice в связке с random - не опознался(((


def get_same_products(s_product):
    return Product.objects.filter(category=s_product.category).exclude(pk=s_product.pk)[:2]


def index(request):
    context = {
        'page_title': 'main'
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    locations = [
        {'city': 'Krasnoyarsk',
         'phone': '7 999 999 99 99',
         'email': 'email_1@gmail.com'},
        {'city': 'New York',
         'phone': '7 555 555 99 99',
         'email': 'email_2@gmail.com'},
    ]
    context = {
        'page_title': 'contact',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    s_product = get_sale_product()
    context = {
        'page_title': 'product',
        'type_of_product': get_type_p(),
        's_product': s_product,
        'same_product': get_same_products(s_product),
    }
    return render(request, 'mainapp/products.html', context)


def page_of_product(request, pk):
    p_product = get_object_or_404(Product, pk=pk)
    context = {
        'page_title': 'page of product',
        'type_of_product': get_type_p(),
        'p_product': p_product,
    }
    return render(request, 'mainapp/page_of_product.html', context)


def category(request, pk):
    p_num = request.GET.get('page', 1)
    if pk == 0:
        category = {'pk': 0, 'name': 'all'}
        products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = category.product_set.all()

    prod_paginator = Paginator(products, 2)
    try:
        products = prod_paginator.page(p_num)
    except PageNotAnInteger:
        products = prod_paginator.page(1)
    except EmptyPage:
        products = prod_paginator.page(prod_paginator.num_pages)

    context = {
        'page_title': 'products of category',
        'type_of_product': get_type_p(),
        'category': category,
        'product_t': products,
    }
    return render(request, 'mainapp/category_of_products.html', context)

# //***//
