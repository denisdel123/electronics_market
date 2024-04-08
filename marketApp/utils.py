from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View

from marketApp.models import Product


@permission_required('product.set_published')
def published(request, pk):
    product = Product.objects.get(pk=pk)
    product.is_published = True
    product.save()
    return redirect(reverse('marketApp:product_detail', kwargs={'pk': pk}))


@permission_required('product.set_published')
def unpublished(request, pk):
    product = Product.objects.get(pk=pk)
    product.is_published = False
    product.save()
    return redirect(reverse('marketApp:product_detail', kwargs={'pk': pk}))
