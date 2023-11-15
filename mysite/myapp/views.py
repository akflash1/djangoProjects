from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator

from .models import Article, Comment
from .forms import RegisterForm, AuthenticationForm, CommentCreateForm, CreateArticleFrom
from django.utils import timezone
from .models import Topic


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print("Form is not valid")  # добавьте этот вывод для отладки
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'myapp/User/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/')
        else:
            print("Form is not valid")  # добавьте этот вывод для отладки
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/User/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def index(request):
    return render(request, 'myapp/post/list.html')


def main_page(request):
    articles = Article.objects.all()
    topics = Topic.objects.all()
    return render(request, 'myapp/post/list.html', {'articles': articles})


def about(request):
    return render(request, 'myapp/about.html')


def create(request):
    return HttpResponse('Create')


def topic_list(request):
    topic_list = Topic.objects.all()
    paginator = Paginator(topic_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        topics = paginator.page(page_number)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)
    return render(request, 'myapp/topic/topic_list.html', {'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic,
                              pk=topic_id)
    articles = topic.articles_on_topic.all()
    return render(request,
                  'myapp/topic/topic_detail.html',
                  {
                      'topic': topic,
                      'articles': articles})


def set_password(request):
    return HttpResponse('Set Password')


def set_userdata(request):
    return HttpResponse('Set Userdata')


def deactivate(request):
    return HttpResponse('Deactivate')


def show_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article)
    return render(request, 'myapp/post/detail.html', {'article': article,
                                                      'comments': comments})


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'myapp/post/list.html', {'articles': articles})


def update_article(request, article_id):
    return render(request, 'myapp/post/update_article.html')


def delete_article(request, article_id):
    return render(request, 'myapp/post/delete_article.html')

@method_decorator(login_required, name='dispatch')

def create_article(request):
    if request.method == 'POST':
        form = CreateArticleFrom(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            topics = form.cleaned_data['topics']
            author = request.user
            article = Article.objects.create(title=title, content=content, author=author)
            return redirect(reverse('article_detail', args=[article.id]))
    else:
        form = CreateArticleFrom()
    return render(request, 'myapp/post/create_article.html', {'form': form})

@method_decorator(login_required, name='dispatch')

def add_comment(request, article_id):
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            article = Article.objects.get(pk=article_id)
            author = request.user
            Comment.objects.create(message=message, article=article, author=author)
            return redirect(reverse('article_detail', args=[article_id]))
    else:
        form = CommentCreateForm()
        return render(request, 'myapp/post/add_comment.html', {'form': form})


def topics_subscribe(request, topic):
    return HttpResponse(f'Topics Subscribe: {topic}')


def topics_unsubscribe(request, topic):
    return HttpResponse(f'Topics Unsubscribe: {topic}')


def profile_username(request, username):
    return HttpResponse(f'User Profile {username}')


def archive(request, year, month):
    if year < 2010 or year > 2023 or month < 1 or month > 12:
        raise Http404('Incorrect date')

    return HttpResponse(f'year: {year}, month: {month}')
