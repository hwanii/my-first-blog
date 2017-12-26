from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse
from .models import Post, LoginForm, UserForm
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth import login, authenticate
from django.template import RequestContext
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) #우선 텍스트와 제목만 작성되어있는 것을 commit을 안 한 상태로 저장하고
            post.author = request.user
            post.published_date = timezone.now() #나머지 작성자와 날짜를 정해줘서
            post.save() #세이브
            #return HttpResponseRedirect(reverse('post_detail', args=(post.pk,)))
            return redirect('post_detail',pk=post.pk)#특정 view 함수로 돌아감. post_detail 뷰는 pk를 필요로 하기 때문에 명시해줘야 함.
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html',{'form':form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = UserForm.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('post_list')
    else:
        form = UserForm()
        return render(request, 'blog/adduser.html',{'form':form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'blog/login.html', {'form':form})
