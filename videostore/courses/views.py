from .models import Course, Product
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
        ctx['title'] = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['shops'] = Product.objects.filter(product=ctx['title']).order_by('number')
        print(ctx['shops'].query)
        return ctx


class ShopSlugDetailPage(DetailView):
    model = Course
    template_name = 'courses/shop-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ShopSlugDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        shops = list(Product.objects.filter(product=course).filter(slug=self.kwargs['shop_slug']).values())
        print(shops)
        ctx['title'] = shops[0]['title']
        ctx['desc'] = shops[0]['description']
        ctx['video'] = shops[0]['video_url'].split("=")[1]
        return ctx
