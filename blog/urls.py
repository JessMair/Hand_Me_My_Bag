from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('edit', views.PostUpdate.as_view(), name='post_edit'),
    path('delete', views.PostDelete.as_view(), name='post_delete'),
]