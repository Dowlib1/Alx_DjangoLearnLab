from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "blog"
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', view.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', view.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', view.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/delete/', view.PostDeleteView.as_view(), name='post_delete'),
     path('post/<int:pk>/update/', view.PostUpdateView.as_view(), name='post_edit'),
    #add-up
    path('post/<int:pk>/comments/new/', view.CommentCreateView.as_view(), name='comment_new'),  # But since integrated, maybe not needed
    path('comment/<int:pk>/edit/', view.CommentUpdateView.as_view(), name='comment_edit'),
     path('comment/<int:pk>/update/', view.CommentCreateView.as_view(), name='comment_update'), 
    path('comment/<int:pk>/delete/', view.CommentDeleteView.as_view(), name='comment_delete'),
    path('search/', view.SearchResultsView.as_view(), name='search'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tag_posts'),
#comment or comments will fit in and slug
]
