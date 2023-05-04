from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Book, Category
from . import tasks
from django.contrib import messages


# Create your views here.
class HomeView(View):
    def get(self, request, category_slug=None):
        books = Book.objects.filter(available=True)
        categories = Category.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            books = books.filter(category=category)
        return render(request, 'home/home.html', {'books': books, 'categories': categories})


class BookDetailView(View):

    def get(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        return render(request, 'home/detail.html', {'book': book})


class BucketHome(View):
    template_name = 'home/bucket.html'

    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        return render(request, self.template_name, {'objects': objects})


class DeleteBucketObject(View):
    def get(self, request, key):
        tasks.delete_object_task(key)
        messages.success(request, 'your object will be delete soon.' 'info')
        return redirect('home:bucket')
