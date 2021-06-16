from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Sofa, Bed, Table


def redir(request):
    return redirect('home/')


def home_page(request):
    return render(request, "home.html")


def store_page(request):
    return render(request, "store.html")


def aboutus_page(request):
    return render(request, "about_us.html")



class ProductDetailView(DetailView):
    CT_MODEL_MODEL_CLASS = {
        'sofa': Sofa,
        'bed': Bed,
        'table': Table,
    }


    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'


