from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls # pyright: ignore[reportMissingImports]
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('', views.index, name='index'),
    path('', login_required(views.IndexView.as_view()), name='all_posts'),
    path('post/<int:pk>/', login_required(views.DetailView.as_view()), name='post_detail'),
    path('create/',login_required(views.create_post), name = 'create_post'),
    path('edit/<int:pk>/', login_required(views.edit_post), name= 'edit_post'),
    path('delete/<int:pk>', login_required(views.delete_post), name='delete_post'),
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    # api token
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    # api
    path("api/posts/", views.PostListCreateAPI.as_view()),
    path('api/posts/<int:pk>/', views.PostUpdateAPI.as_view()),

    
    

] + debug_toolbar_urls()