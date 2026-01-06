from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from .models import Post
from django.views import generic
from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
from django.contrib import messages

from rest_framework import generics
from .serializers import PostListSerializer, PostUpdateSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwnerOrReadOnly


# api
class PostListCreateAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class IndexView(generic.ListView):
    template_name = "all_posts.html"
    context_object_name = "posts" # 指定ListView創建的list名稱，default叫做post_list
    def get_queryset(self):
        """Return the list of a model"""
        return Post.objects.all()
# def all_posts(request):
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request, "all_posts.html", context)
# views.py
class DetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html" # 因為使用DetailView, post這個variable會自動提供
# def post_detail(request, post_id):
#     # try:
#     #     post = Post.objects.get(id=post_id)
#     #     context = {'post': post}
#     # except Post.DoesNotExist:
#     #     raise Http404("Posts does not exist")
#     post =  get_object_or_404(Post, pk=post_id)
#     context = {'post': post}
#     return render(request, "post_detail.html", context)
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content, author = request.user)
        return redirect("all_posts")
    else:
        context = {}
        return render(request, 'create_post.html', context)
    
def edit_post(request, pk):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        p = Post.objects.get(pk=pk)
        p.title = title
        p.content = content
        p.save()

        # return redirect("post_detail", post_id = post_id)
        return HttpResponseRedirect(reverse("post_detail", args=(p.id,)))
    else:
        post =  get_object_or_404(Post, pk=pk)
        context = {'post': post}
        return render(request, "edit_post.html", context)
      
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect("all_posts")
    else: # GET request
        return redirect("all_posts") 

def user_login(request):
    if request.method =="GET":
        return render(request, "login.html")
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            context = {'user':user}
            return render(request,'all_posts.html', context)
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Login success!")
            context= {'messages':messages}
            return render(request,'all_posts.html', context)