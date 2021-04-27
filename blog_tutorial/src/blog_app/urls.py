from django.urls import path

from .views import(
    BlogListView, 
    BlogDetailView,
    BlogCreateView, 
    BlogUpdateView,
    BlogDeleteView,
    HomePageView,
)
urlpatterns=[
    path('', HomePageView.as_view() , name = 'homepage'),
    path('home', BlogListView.as_view() , name = 'home'),
    path('post/<int:pk>/', BlogDetailView.as_view() , name = 'blog_details' ),
    path('post/new/', BlogCreateView.as_view(), name = 'new_post'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name = 'edit_post'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete_post'),
]