from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404


def main_page(request):
    return HttpResponse('Main page')


def about(request):
    return HttpResponse('About')


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
    return HttpResponse('Register')


def login(request):
    return HttpResponse('Login')


def logout(request):
    return redirect('main_page')


def article_show(request, article):
    return HttpResponse(f'Article: {article}')


def article_update(request, article):
    return HttpResponse(f'Article Update: {article}')


def article_delete(request, article):
    return HttpResponse(f'Article Delete: {article}')


def article_comment(request, article):
    return HttpResponse(f'Article Comment: {article}')


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
