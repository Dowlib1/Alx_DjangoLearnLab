from django.shortcuts import render #dipensable
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post, Like
from rest_framework import permissions  # Add/adjust this if not already using qualified 'permissions'

# ... (your other imports and code)

serializer.save(author=self.request.user)

class FeedView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

@action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
def like(self, request, pk=None):
    post = self.get_object()
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )
    return Response({'status': 'liked'})

@action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
def unlike(self, request, pk=None):
    post = self.get_object()
    Like.objects.filter(post=post, user=request.user).delete()
    return Response({'status': 'unliked'})

class IsOwnerOrReadOnly:
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)                     # ← this is required
        like, created = Like.objects.get_or_create(                        # ← this exact order
            user=request.user, post=post
        )
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
        return Response({'status': 'liked'})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        post = generics.get_object_or_404(Post, pk=pk)                     # ← optional but good to add
        Like.objects.filter(post=post, user=request.user).delete()
        return Response({'status': 'unliked'})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
def like(self, request, pk=None):
    post = self.get_object()
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if created:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )
    return Response({'status': 'liked'})

@action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
def unlike(self, request, pk=None):
    post = self.get_object()
    Like.objects.filter(post=post, user=request.user).delete()
    return Response({'status': 'unliked'})
