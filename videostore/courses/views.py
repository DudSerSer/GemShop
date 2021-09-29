from .models import Course
from django.views.generic import ListView, DetailView


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        return ctx


class ShopDetailPage(DetailView):
    model = Course
    template_name = 'courses/gems.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ShopDetailPage, self).get_context_data(**kwargs)
        ctx['title'] = Course.objects.filter(slug=self.kwargs['slug']).first
        return ctx
