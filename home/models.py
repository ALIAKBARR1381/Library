from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE,related_name='scategory',null=True,blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'my_Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category_filter', args=[self.slug, ])


class Book(models.Model):
    category = models.ManyToManyField(Category, related_name="Book")
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        self.slug = "-".join([slugify(self.name), slugify(self.created)])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home:book_detail", args=[self.slug, ])
