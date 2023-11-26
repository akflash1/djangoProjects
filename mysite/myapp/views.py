from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import Article, Comment, Topic
from .forms import CommentCreateForm, CreateArticleFrom, RegisterForm, AuthenticationForm


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'myapp/User/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print("Form is not valid")
            print(form.errors)
            return render(request, 'myapp/User/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'myapp/User/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/')
        else:
            print("Form is not valid")
            return render(request, 'myapp/User/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class MainPageView(View):
    def get(self, request):
        articles = Article.objects.all()
        topics = Topic.objects.all()
        return render(request, 'myapp/post/list.html', {'articles': articles})


class AboutView(View):
    def get(self, request):
        return render(request, 'myapp/about.html')


class CreateView(View):
    def get(self, request):
        return HttpResponse('Create')

class IndexView(TemplateView):
    template_name = 'myapp/post/list.html'


class TopicListView(ListView):
    model = Topic
    template_name = 'myapp/topic/topic_list.html'
    paginate_by = 3
    context_object_name = 'topics'


class TopicDetailView(View):
    def get(self, request, topic_id):
        topic = get_object_or_404(Topic, pk=topic_id)
        articles = topic.articles_on_topic.all()
        return render(request, 'myapp/topic/topic_detail.html', {'topic': topic, 'articles': articles})


class SetPasswordView(View):
    def get(self, request):
        return HttpResponse('Set Password')


class SetUserDataView(View):
    def get(self, request):
        return HttpResponse('Set Userdata')


class DeactivateView(View):
    def get(self, request):
        return HttpResponse('Deactivate')


class ShowArticleView(View):
    def get(self, request, article_id):
        article = get_object_or_404(Article, pk=article_id)
        comments = Comment.objects.filter(article=article)
        form = CommentCreateForm()
        return render(request, 'myapp/post/detail.html', {'article': article, 'comments': comments})


class ArticleListView(ListView):
    model = Article
    template_name = 'myapp/post/list.html'
    context_object_name = 'articles'


class UpdateArticleView(View):
    def get(self, request, article_id):
        return render(request, 'myapp/post/update_article.html')


class DeleteArticleView(View):
    def get(self, request, article_id):
        return render(request, 'myapp/post/delete_article.html')


@method_decorator(login_required, name='dispatch')
class CreateArticleView(View):
    def get(self, request):
        form = CreateArticleFrom()
        return render(request, 'myapp/post/create_article.html', {'form': form})

    def post(self, request):
        form = CreateArticleFrom(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            topics = form.cleaned_data['topics']
            author = request.user
            article = Article.objects.create(title=title, content=content, author=author)
            return redirect(reverse('article_detail', args=[article.id]))
        return render(request, 'myapp/post/create_article.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class AddCommentView(View):
    def get(self, request, article_id):
        form = CommentCreateForm()
        return render(request, 'myapp/post/add_comment.html', {'form': form})

    def post(self, request, article_id):
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            article = Article.objects.get(pk=article_id)
            author = request.user
            Comment.objects.create(message=message, article=article, author=author)
            return redirect(reverse('article_detail', args=[article_id]))
        return render(request, 'myapp/post/add_comment.html', {'form': form})


class TopicsSubscribeView(View):
    def get(self, request, topic):
        return HttpResponse(f'Topics Subscribe: {topic}')


class TopicsUnsubscribeView(View):
    def get(self, request, topic):
        return HttpResponse(f'Topics Unsubscribe: {topic}')


class ProfileUsernameView(View):
    def get(self, request, username):
        return HttpResponse(f'User Profile {username}')


class ArchiveView(View):
    def get(self, request, year, month):
        if year < 2010 or year > 2023 or month < 1 or month > 12:
            raise Http404('Incorrect date')
        return HttpResponse(f'year: {year}, month: {month}')
