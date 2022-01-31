from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from shop.settings import LOGIN_URL


@login_required
def index(request):
    basket = request.user.basket.all()
    context = {
        'page_title': 'basket',
        'basket': basket,
    }
    return render(request, 'basketapp/index.html', context)


@login_required
def add(request, product_pk):
    if LOGIN_URL in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('mainshop:page_of_product', kwargs={'pk': product_pk}))
    basket, _ = Basket.objects.get_or_create(user=request.user, product_id=product_pk)
    basket.quantity_p += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove(request, basket_pk):
    basket_pk_remove = get_object_or_404(Basket, pk=basket_pk)
    basket_pk_remove.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def upd(request, basket_pk, quantity_p):
    if request.is_ajax():
        item_b = Basket.objects.filter(pk=basket_pk).first()
        if not item_b:
            return JsonResponse({'status': False})
        if quantity_p == 0:
            item_b.delete()
        else:
            item_b.quantity_p = quantity_p
            item_b.save()
        basket_change_html = render_to_string('basketapp/includes/basket_summary_base.html', request=request)
        return JsonResponse({'status': True,
                             'basket_summary_': basket_change_html,
                             'quantity_p': quantity_p})
