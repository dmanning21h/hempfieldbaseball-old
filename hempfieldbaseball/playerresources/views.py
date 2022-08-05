from django.shortcuts import render

from . import services as rs


def index(request):
    context = {}

    return render(request, 'playerresources/resources.html', context)


def diet(request):
    diet_documents = rs.get_all_diet_documents()
    diet_website_links = rs.get_all_diet_articles()

    context = {
        'diet_documents':
            diet_documents,
        'diet_website_links':
            diet_website_links
    }

    return render(request, 'playerresources/diet.html', context)


def mental_baseball(request):
    books = rs.get_mental_baseball_books()

    context = {
        'books': books,
    }

    return render(request, 'playerresources/mental-baseball.html', context)


def hitting_videos(request):
    hitting_videos = rs.get_all_hitting_videos()

    context = {
        'hitting_video_links': hitting_videos
    }

    return render(request, 'playerresources/hitting-videos.html', context)


def hitting_articles(request):
    hitting_articles = rs.get_all_hitting_articles()

    context = {
        'hitting_article_links': hitting_articles
    }

    return render(request, 'playerresources/hitting-articles.html', context)