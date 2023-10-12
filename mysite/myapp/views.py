from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
<<<<<<< HEAD


def index(request):
    return render(request, 'myapp/post/list.html')
=======
>>>>>>> 0b7259f23bf659fb3b919fbb40cbde12f988b7da


def main_page(request):
    return HttpResponse('Main page')


def about(request):
    return render(request, 'myapp/about.html')


def registration(request):
    return HttpResponse('Register')


def create(request):
    return HttpResponse('Create')


def topics(request):
    return HttpResponse('Topics')


def set_password(request):
    return HttpResponse('Set Password')


def set_userdata(request):
    return HttpResponse('Set Userdata')


def deactivate(request):
    return HttpResponse('Deactivate')


def register(request):
    return render(request, 'myapp/user/login.html')


def login(request):
    return render(request, 'myapp/user/login.html')


def logout(request):
    return render(request, 'myapp/user/login.html')


def show_article(request, article_id):
    return render(request, 'myapp/post/detail.html')


def update_article(request, article_id):
    return render(request, 'myapp/post/update_article.html')


def delete_article(request, article_id):
    return render(request, 'myapp/post/delete_article.html')


def create_article(request):
    return render(request, 'myapp/post/create_article.html')


def add_comment(request, article_id):
    return render(request, 'myapp/post/add_comment.html')


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
