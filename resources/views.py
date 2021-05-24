from django.shortcuts import render

from . import services as rs


def index(request):
    book_data_exists = rs.does_book_data_exist()

    context = {}

    return render(request, 'resources/resources.html', context)


def diet(request):
    pass


def books(request):
    pass


def hitting_videos(request):
    pass


def hitting_articles(request):
    pass