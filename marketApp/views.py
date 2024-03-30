from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from marketApp.forms import ProductForm, CategoryForm, VersionForm
from marketApp.models import Product, Category, Version


def main(request):
    return render(request, 'marketApp/main.html')


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('marketApp:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('marketApp:category_list')


class CategoryListView(ListView):
    model = Category


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('marketApp:category_list')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('marketApp:product_detail', kwargs={'pk': object_id})
        return detail_url


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('marketApp:product_detail', kwargs={'pk': object_id})
        return detail_url

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset

        return context_data

    def form_valid(self, form):

        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return Product.objects.filter(category__pk=category_pk)


class ProductDetailView(DetailView):
    model = Product

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('marketApp:product_detail', kwargs={'pk': object_id})
        return detail_url


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('marketApp:category_list')
