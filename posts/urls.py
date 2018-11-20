from posts import views
from django.urls import path


# app_name = 'posts'


urlpatterns = [
    path('<slug:slug>/', views.PostDetailAPIView.as_view(), name = 'post-detail'),
    path('', views.PostListAPIView.as_view(), name = 'post-list'),
]
