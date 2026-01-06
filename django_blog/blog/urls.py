from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_new'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    #add-up
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_new'),  # But since integrated, maybe not needed
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('search/', SearchResultsView.as_view(), name='search'),
path('tags/<str:tag_name>/', TagView.as_view(), name='tag_posts'),
]
