from django.db import models
from django.urls import reverse


class Course(models.Model):
    slug = models.SlugField()  # для создания своего адреса URL
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(default='default.png', upload_to='course_images')
    free = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse('gems', kwargs={'slug': self.slug})


class Product(models.Model):
    slug = models.SlugField()  # для создания своего адреса URL
    title = models.CharField(max_length=120)
    description = models.TextField()
    product = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    number = models.IntegerField()
    video_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop-detail', kwargs={'slug': self.product.slug, 'shop_slug': self.slug})
