from django.urls import path
from . import views

urlpatterns = [
    path('', views.archive, name='archive'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),  # Add this line
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('search/', views.search_results, name='search_results'),
]
