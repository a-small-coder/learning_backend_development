from django.shortcuts import render
from django.views.generic import DetailView

from .models import Treadmill, Ball, TennisTable


def test_view(request):
    return render(request, 'index.html', {})


class ProductDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'treadmill': Treadmill,
        'ball': Ball,
        'tennis_table': TennisTable,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product.html'
    slug_url_kwarg = 'slug'
