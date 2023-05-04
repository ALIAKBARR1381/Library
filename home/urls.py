from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('category/<slug:category_slug>/', views.HomeView.as_view(), name='category_filter'),
    path('bucket/', views.BucketHome.as_view(), name='bucket'),
    path('delete_obj_bucket/<key>', views.DeleteBucketObject.as_view(), name='delete_object_bucket'),
    path('<slug:slug>/', views.BookDetailView.as_view(), name="book_detail")
]
