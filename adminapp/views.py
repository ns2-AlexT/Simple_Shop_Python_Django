from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
# CBV
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from adminapp.forms import AdminShopUserUpd, ProductCatCreatForm, ProductUpdForm
from adminapp.forms import ShopUserUserChangeForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda user: user.is_superuser)
def index(request):
    all_users = get_user_model().objects.all()
    context = {
        'page_title': 'adm/users',
        'all_users': all_users,
    }
    return render(request, 'adminapp/index.html', context)


# all for product fbc
@user_passes_test(lambda user: user.is_superuser)
def cat_products(request, pk):
    p_num = request.GET.get('page', 1)

    category = get_object_or_404(ProductCategory, pk=pk)
    object_list = category.product_set.all()

    prod_paginator = Paginator(object_list, 2)
    try:
        object_list = prod_paginator.page(p_num)
    except PageNotAnInteger:
        object_list = prod_paginator.page(1)
    except EmptyPage:
        object_list = prod_paginator.page(prod_paginator.num_pages)

    context = {
        'page_title': f'category {category.name}/products',
        'category': category,
        'object_list': object_list
    }
    return render(request, 'mainapp/cat_products_list.html', context)


@user_passes_test(lambda user: user.is_superuser)
def cat_product_create(request, cat_pk):
    category = get_object_or_404(ProductCategory, pk=cat_pk)
    if request.method == 'POST':
        form = ProductUpdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(
                'adminapp:cat_products',
                kwargs={'pk': category.pk}
            ))
    else:
        form = ProductUpdForm(
            initial={
                'category': category,
            }
        )
    context = {
        'page_title': 'product/create',
        'form': form,
        'category': category,
    }
    return render(request, 'mainapp/product_upd.html', context)


#
@user_passes_test(lambda user: user.is_superuser)
def user_del(request, user_pk):
    user_d = get_object_or_404(get_user_model(), pk=user_pk)
    if not user_d.is_active or request.method == 'POST':
        if user_d.is_active:
            user_d.is_active = False
            user_d.save()
        else:
            user_d.is_active = True
            user_d.save()
        return HttpResponseRedirect(reverse('adminapp:index'))
    context = {
        'page_title': 'admin/user/deleting',
        'user_del': user_d
    }
    return render(request, 'adminapp/user_del.html', context=context)


# @user_passes_test(lambda user: user.is_superuser)
# def user_upd(request, user_pk):
#     user_u = get_object_or_404(get_user_model(), pk=user_pk)
#     if request.method == 'POST':
#         user_form = AdminShopUserUpd(request.POST, request.FILES, instance=user_u)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('adminshop:index'))
#     else:
#         user_form = AdminShopUserUpd(instance=user_u)
#     context = {
#         'page_title': 'root/user/editing',
#         'form': user_form
#     }
#     return render(request, 'adminapp/user_upd.html', context)


# @user_passes_test(lambda user: user.is_superuser)
# def categories(request):
#     context = {
#         'page_title': 'admin/categories',
#         'cat_list': ProductCategory.objects.all()
#     }
#     return render(request, 'adminapp/categories.html', context=context)


# CVB
class SuperUserOnlyMixin:
    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PageTitleMixin:
    p_title = 'page_title'
    p_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.p_title] = self.p_context
        return context


class CategoriesList(SuperUserOnlyMixin, PageTitleMixin, ListView):
    p_context = 'admin/cat'
    model = ProductCategory


class ProductCatCreate(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = ProductCategory
    form_class = ProductCatCreatForm
    success_url = reverse_lazy('adminshop:categories')
    p_context = 'admin/cat/create'

    # left for examples
    # fields = '__all__'
    # fields = ('name', 'is_active')
    # template_name = 'adminapp/templates/mainapp/productCategory_form.html'


class ProductCatUpd(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = ProductCategory
    form_class = ProductCatCreatForm
    success_url = reverse_lazy('adminshop:categories')
    p_context = 'admin/cat/upd'


class ProductCatDel(SuperUserOnlyMixin, PageTitleMixin, DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('adminshop:categories')
    p_context = 'admin/cat/del'
    # for memory reload url
    # def get_success_url(self):
    #     self.object.pk =


class UserUpd(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = get_user_model()
    form_class = AdminShopUserUpd
    success_url = reverse_lazy('adminshop:index')
    pk_url_kwarg = 'user_pk'
    p_context = 'admin/usr/upd'

    # @user_passes_test(lambda user: user.is_superuser)
    # user_u = get_object_or_404(get_user_model(), pk=user_pk)
    # if request.method == 'POST':
    #     user_form = AdminShopUserUpd(request.POST, request.FILES, instance=user_u)
    #     if user_form.is_valid():
    #         user_form.save()
    #         return HttpResponseRedirect(reverse('adminshop:index'))
    # else:
    #     user_form = AdminShopUserUpd(instance=user_u)
    # context = {
    #     'page_title': 'root/user/editing',
    #     'form': user_form
    # }
    # return render(request, 'adminapp/user_upd.html', context)


class ProductDetail(SuperUserOnlyMixin, PageTitleMixin, DetailView):
    model = Product
    p_context = 'admin/product/detail'
